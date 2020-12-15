import multiprocessing as mp
from enum import Enum
import numpy as np
import gi

import time

gi.require_version('Gst', '1.0')
from gi.repository import Gst, GstVideo
import gstreamer.utils as utils


Gst.debug_set_active(True)
Gst.debug_set_default_threshold(2)
# Gst.debug_set_threshold_from_string("*FACTORY*:4", True)
# Gst.GST_DEBUG_DUMP_DOT_DIR='/home/pipe/Desktop'

Gst.init(None)

'''Konwn issues
* if format changes at run time system hangs
'''


class StreamMode(Enum):
    INIT_STREAM = 1
    SETUP_STREAM = 1
    READ_STREAM = 2


class StreamCommands(Enum):
    FRAME = 1
    ERROR = 2
    HEARTBEAT = 3
    RESOLUTION = 4
    STOP = 5


class StreamCapture(mp.Process):

    def __init__(self, link, stop, outQueue, framerate, logger):
        """
        Initialize the stream capturing process
        link - rstp link of stream
        stop - to send commands to this process
        outPipe - this process can send commands outside
        """

        super().__init__()
        self.logger = logger
        self.streamLink = link
        self.stop = stop
        self.outQueue = outQueue
        self.framerate = framerate
        self.currentState = StreamMode.INIT_STREAM
        self.pipeline = None
        self.source = None
        self.metadata_sink = None
        self.frame_sink = None
        self.image_arr = None
        self.newImage = False
        self.newMetadata = False
        self.num_unexpected_tot = 40
        self.unexpected_cnt = 0
        self.flag = True
        self.counter_frame_fps = 0
        self.fps = 0
        self.last_frame_time = time.time()

    def log_fps(self):
        self.counter_frame_fps += 1
        frame_time = time.time()
        if frame_time - self.last_frame_time >= 1:
            self.fps = str(round(self.counter_frame_fps / (frame_time - self.last_frame_time), 2))
            self.counter_frame_fps = 0
            self.last_frame_time = time.time()
            self.logger.info("fps: " + str(self.fps))
    
    def gst_to_opencv(self, sample):
        if self.flag:
            self.flag = False
            self.pipeline.send_event(Gst.Event.new_latency(0))
        
        self.log_fps()

        buffer = sample.get_buffer()
        caps_format = sample.get_caps().get_structure(0)

        (result, mapinfo) = buffer.map(Gst.MapFlags.READ)
        assert result
        
        buffer.unmap(mapinfo)
        
        frmt_str = caps_format.get_value('format') 
        video_format = GstVideo.VideoFormat.from_string(frmt_str)
        
        w, h = caps_format.get_value('width'), caps_format.get_value('height')
        c = utils.get_num_channels(video_format)

        buffer_size = buffer.get_size()
        shape = (h, w, c) if (h * w * c == buffer_size) else buffer_size
        arr = np.ndarray(shape=shape, buffer=buffer.extract_dup(0, buffer_size),
                         dtype=utils.get_np_dtype(video_format))
        return arr
    
    def gst_to_metadata(self, sample):
        buffer = sample.get_buffer()
        
        (result, mapinfo) = buffer.map(Gst.MapFlags.READ)
        assert result
        
        buffer.unmap(mapinfo)
        
        buffer_size = buffer.get_size()
        metadata = buffer.extract_dup(0, buffer_size)
        return metadata

    def new_frame_buffer(self, sink, _):
        sample = sink.emit("pull-sample")
        arr = self.gst_to_opencv(sample)
        self.image_arr = arr
        self.newImage = True
        return Gst.FlowReturn.OK
    
    def new_metadata_buffer(self, sink, _):
        sample = sink.emit("pull-sample")
        metadata = self.gst_to_metadata(sample)
        self.metadata = metadata
        self.newMetadata = True
        return Gst.FlowReturn.OK

    def set_properties(self):
        self.source = self.pipeline.get_by_name('m_uri')
        self.source.set_property('uri', self.streamLink)

        self.frame_sink = self.pipeline.get_by_name('frame_appsink')
        self.metadata_sink = self.pipeline.get_by_name('metadata_appsink')
        if self.sink is not None:
            self.frame_sink.set_property('max-lateness', 1000)

            self.frame_sink.set_property('max-buffers', 1)

            self.frame_sink.set_property('drop', 'true')

            self.frame_sink.set_property('emit-signals', True)

        if self.frame_sink is None or not self.pipeline:
            print("Not all elements could be created.")
            self.stop.set()

        self.frame_sink.connect("new-sample", self.new_frame_buffer, self.frame_sink)
        self.metadata_sink.connect("new-sample", self.new_metadata_buffer, self.metadata_sink)

    def run(self):
        # working VVVVVVVVVVVVVVVVVVVVVVV
        self.pipeline = Gst.parse_launch(
            'uridecodebin name=m_uri ! nvvidconv ! video/x-raw, format=BGRx ! videoconvert ! videorate ! video/x-raw, framerate=20/1, format=BGR ! appsink name=frame_appsink')

        self.set_properties()

        # Start playing
        ret = self.pipeline.set_state(Gst.State.PLAYING)
        if ret == Gst.StateChangeReturn.FAILURE:
            print("Unable to set the pipeline to the playing state.")
            self.stop.set()

        # Wait until error or EOS
        bus = self.pipeline.get_bus()

        while True:

            if self.stop.is_set():
                print('Stopping CAM Stream by main process')
                break

            message = bus.timed_pop_filtered(10000, Gst.MessageType.ANY)
            if self.image_arr is not None and self.newImage is True and self.metadata is not None and self.newMetadata is True:

                if not self.outQueue.full():
                    self.outQueue.put((self.image_arr, self.metadata), block=False)

                self.image_arr = None
                self.metadata = None
                self.unexpected_cnt = 0

            if message:
                if message.type == Gst.MessageType.ERROR:
                    err, debug = message.parse_error()
                    print("Error received from element %s: %s" % (
                        message.src.get_name(), err))
                    print("Debugging information: %s" % debug)
                    break
                elif message.type == Gst.MessageType.EOS:
                    print("End-Of-Stream reached.")
                    break
                elif message.type == Gst.MessageType.STATE_CHANGED:
                    if isinstance(message.src, Gst.Pipeline):
                        old_state, new_state, pending_state = message.parse_state_changed()
                        print("Pipeline state changed from %s to %s." %
                              (old_state.value_nick, new_state.value_nick))
                else:
                    self.unexpected_cnt = self.unexpected_cnt + 1
                    if self.unexpected_cnt == self.num_unexpected_tot:
                        break

        print('terminating cam pipe')
        self.stop.set()
        self.pipeline.set_state(Gst.State.NULL)
