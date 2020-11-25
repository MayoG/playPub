#!/usr/bin/env python

import os
import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst, GObject, Gtk

class GTK_Main(object):

    def __init__(self):
    
        # 'uridecodebin name=m_uri ! nvvidconv ! video/x-raw, format=BGRx ! videoconvert ! videorate ! video/x-raw, framerate=20/1, format=BGR ! appsink name=m_appsink'
        self.player = Gst.Pipeline.new("player")
        
        source = Gst.ElementFactory.make("uridecodebin", "source")
        source.set_property('uri', self.streamLink)
        
        demuxer = Gst.ElementFactory.make("mpegpsdemux", "demuxer")
        demuxer.connect("pad-added", self.demuxer_callback)
        self.video_decoder = Gst.ElementFactory.make("mpeg2dec", "video-decoder")
        self.audio_decoder = Gst.ElementFactory.make("mad", "audio-decoder")
        audioconv = Gst.ElementFactory.make("audioconvert", "converter")
        audiosink = Gst.ElementFactory.make("autoaudiosink", "audio-output")
        videosink = Gst.ElementFactory.make("autovideosink", "video-output")
        self.queuea = Gst.ElementFactory.make("queue", "queuea")
        self.queuev = Gst.ElementFactory.make("queue", "queuev")
        colorspace = Gst.ElementFactory.make("videoconvert", "colorspace")

        self.player.add(source) 
        self.player.add(demuxer) 
        self.player.add(self.video_decoder) 
        self.player.add(self.audio_decoder) 
        self.player.add(audioconv) 
        self.player.add(audiosink) 
        self.player.add(videosink) 
        self.player.add(self.queuea) 
        self.player.add(self.queuev) 
        self.player.add(colorspace)

        source.link(demuxer)

        self.queuev.link(self.video_decoder)
        self.video_decoder.link(colorspace)
        colorspace.link(videosink)

        self.queuea.link(self.audio_decoder)
        self.audio_decoder.link(audioconv)
        audioconv.link(audiosink)

        bus = self.player.get_bus()
        bus.add_signal_watch()
        bus.enable_sync_message_emission()
        bus.connect("message", self.on_message)

    def start_stop(self, w):
        if self.button.get_label() == "Start":
            filepath = self.entry.get_text().strip()
            if os.path.isfile(filepath):
                filepath = os.path.realpath(filepath)
                self.button.set_label("Stop")
                self.player.get_by_name("file-source").set_property("location", filepath)
                self.player.set_state(Gst.State.PLAYING)
            else:
                self.player.set_state(Gst.State.NULL)
                self.button.set_label("Start")

    def on_message(self, bus, message):
        t = message.type
        if t == Gst.MessageType.EOS:
            self.player.set_state(Gst.State.NULL)
            self.button.set_label("Start")
        elif t == Gst.MessageType.ERROR:
            err, debug = message.parse_error()
            print "Error: %s" % err, debug
            self.player.set_state(Gst.State.NULL)
            self.button.set_label("Start")

    def demuxer_callback(self, demuxer, pad):
        if pad.get_property("template").name_template == "video_%02d":
            qv_pad = self.queuev.get_pad("sink")
            pad.link(qv_pad)
        elif pad.get_property("template").name_template == "audio_%02d":
            qa_pad = self.queuea.get_pad("sink")
            pad.link(qa_pad)


Gst.init(None)
GTK_Main()
GObject.threads_init()
Gtk.main()
