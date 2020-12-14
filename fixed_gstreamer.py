# cython: language_level=3, boundscheck=False
import multiprocessing as mp
from enum import Enum
import numpy as np
import gi

import time

gi.require_version('Gst', '1.0')
from gi.repository import Gst

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
        self.decode = None
        self.convert = None
        self.sink = None
        self.image_arr = None
        self.newImage = False
        self.frame1 = None
        self.frame2 = None
        self.num_unexpected_tot = 40
        self.unexpected_cnt = 0
        self.flag = True
        self.counter_frame_fps = 0
        self.fps = 0
        self.last_frame_time = time.time()

    def gst_to_opencv(self, sample):
        if self.flag:
            self.flag = False
            self.pipeline.send_event(Gst.Event.new_latency(0))
            # print("latency: " + str(self.pipeline.getLatency()))
            # print("Delay: " + str(self.pipeline.getDelay()))

        self.counter_frame_fps += 1
        frame_time = time.time()
        if frame_time - self.last_frame_time >= 1:
            self.fps = str(round(self.counter_frame_fps / (frame_time - self.last_frame_time), 2))
            self.counter_frame_fps = 0
            self.last_frame_time = time.time()
            self.logger.info("fps: " + str(self.fps))

        buf = sample.get_buffer()
        caps = sample.get_caps()

        # print("format: {0}".format(caps.get_structure(0).get_value('format')))
        # print("Buffer:   {0}".format(buf))
        # print("Buffer Size:   {0}".format(buf.get_size()))
        memory = buf.get_all_memory()
        # print("Memory dir:   {0}".format(dir(memory)))
        # print("Sample:   {0}".format(sample))
        # print("Buffer dir:   {0}".format(dir(buf)))
        # print("Sample dir:   {0}".format(dir(sample)))
        # print("Height:   {0}".format(caps.get_structure(0).get_value('height')))
        # print("Width:   {0}".format(caps.get_structure(0).get_value('width')))

        (result, mapinfo) = buf.map(Gst.MapFlags.READ)
        assert result

        try:
            # print("DATA:  {0}".format(mapinfo.data))
            pass
        finally:
            buf.unmap(mapinfo)

        arr = np.ndarray(
            (caps.get_structure(0).get_value('height'),
             caps.get_structure(0).get_value('width'),
             3),
            buffer=buf.extract_dup(0, buf.get_size()),
            dtype=np.uint8)
        return arr

    def new_buffer(self, sink, _):
        sample = sink.emit("pull-sample")
        arr = self.gst_to_opencv(sample)
        self.image_arr = arr
        self.newImage = True
        return Gst.FlowReturn.OK

    def set_properties(self):
        self.source = self.pipeline.get_by_name('m_uri')
        self.source.set_property('uri', self.streamLink)

        self.sink = self.pipeline.get_by_name('m_appsink')
        if self.sink is not None:
            self.sink.set_property('max-lateness', 1000)

            self.sink.set_property('max-buffers', 1)

            self.sink.set_property('drop', 'true')

            self.sink.set_property('emit-signals', True)

        # self.sink.set_property('drop', True)
        # self.sink.set_property('sync', False)

        # caps = Gst.caps_from_string(
        #     'video/x-raw, format=(string){BGR, GRAY8}; video/x-bayer,format=(string){rgba,rggb,bggr,grbg,gbrg}')
        # caps = Gst.caps_from_string('video/x-raw, format=(string){I420, YUYU, UYVY, YUY2}')
        # self.sink.set_property('caps', caps)

        if self.sink is None or not self.pipeline:
            print("Not all elements could be created.")
            self.stop.set()

        self.sink.connect("new-sample", self.new_buffer, self.sink)

    def run(self):
        # working VVVVVVVVVVVVVVVVVVVVVVV
        self.pipeline = Gst.parse_launch(
            'uridecodebin name=m_uri ! nvvidconv ! video/x-raw, format=BGRx ! videoconvert ! videorate ! video/x-raw, framerate=20/1, format=BGR ! appsink name=m_appsink')

        # self.pipeline = Gst.parse_launch(
        #     'uridecodebin name=m_uri ! nvvidconv ! video/x-raw, format=BGRx ! videoconvert ! videorate ! video/x-raw, framerate=25/1, format=BGR ! appsink name=m_appsink')

        # Gst.gst_debug_bin_to_dot_file(self.pipeline, Gst.GST_DEBUG_GRAPH_SHOW_ALL, "pipeline")

        # self.pipeline = Gst.parse_launch(
        #     'uridecodebin name=m_uri ! nvvidconv ! video/x-raw, format=BGRx ! videoconvert ! videorate ! video/x-raw, framerate=10/1, format=BGR ! fpsdisplaysink')

        # self.pipeline = Gst.parse_launch(
        #     'rtspsrc location=rtsp://128.9.0.11/test.ts tls-validation-flags=generic-error ! rtpjitterbuffer ! application/x-rtp ! rtph264depay ! appsink name=m_appsink')

        # self.pipeline = Gst.parse_launch(
        #     'rtspsrc location=rtsp://128.9.0.11/test.ts tls-validation-flags=generic-error ! rtpmp2tdepay ! appsink name=m_appsink')

        # self.pipeline = Gst.parse_launch(
        #     'udpsrc rtspsrc location=rtsp://128.9.0.11/test.ts media=video.encoding-name=MP2T latency=0 ! rtpmp2tdepay ! tsdemux ! h264parse ! omxh264dec ! videoconvert ! video/x-raw,fromat=RGB ! appsink name=m_appsink')

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
            # print "image_arr: ", image_arr
            if self.image_arr is not None and self.newImage is True:

                if not self.outQueue.full():
                    # print("\r adding to queue of size{}".format(self.outQueue.qsize()), end='\r')
                    self.outQueue.put((StreamCommands.FRAME, self.image_arr), block=False)

                self.image_arr = None
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
