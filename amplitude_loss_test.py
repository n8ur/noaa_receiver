#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: NOAA Demo based on PFB Channelizer Demo
# Author: Chris Kuethe <chris.kuethe+github@gmail.com>
# Generated: Fri Aug 14 16:33:42 2015
##################################################

from PyQt4 import Qt
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.filter import pfb
from optparse import OptionParser
import sip
import sys
import time

from distutils.version import StrictVersion
class amplitude_loss_test(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "NOAA Demo based on PFB Channelizer Demo")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("NOAA Demo based on PFB Channelizer Demo")
        try:
             self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
             pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "amplitude_loss_test")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.noaa_num_chans = noaa_num_chans = 7
        self.noaa_chan_width = noaa_chan_width = int(25e3)
        self.noaa_band_start = noaa_band_start = 162.4e6
        self.oversampled_width = oversampled_width = noaa_chan_width * (noaa_num_chans + 1)
        self.noaa_fm_dev = noaa_fm_dev = int(5e3)
        self.noaa_band_center = noaa_band_center = noaa_band_start + (noaa_num_chans / 2 * noaa_chan_width)
        self.hardware_rate = hardware_rate = int(1e6)
        self.tuner_freq = tuner_freq = 162.3e6
        self.target_freq = target_freq = noaa_band_center
        self.ppm = ppm = 0
        self.pfb_taps = pfb_taps = firdes.low_pass(2.0, oversampled_width, noaa_fm_dev*2 ,1000, firdes.WIN_HAMMING, 6.76)
        self.lpf_taps = lpf_taps = firdes.low_pass(1.0, hardware_rate, oversampled_width / 2,noaa_chan_width, firdes.WIN_HAMMING, 6.76)
        self.channel_map = channel_map = range(0, noaa_num_chans)
        self.volume = volume = 0
        self.tuner_offset = tuner_offset = target_freq - tuner_freq
        self.ppm_corr = ppm_corr = tuner_freq * (ppm/1e6)
        self.pfb_sizeof_taps = pfb_sizeof_taps = len(pfb_taps)
        self.noaa_band_width = noaa_band_width = noaa_chan_width * noaa_num_chans
        self.noaa_band_end = noaa_band_end = noaa_band_start + (noaa_num_chans * noaa_chan_width)
        self.lpf_sizeof_taps = lpf_sizeof_taps = len(lpf_taps)
        self.fftwidth = fftwidth = 512
        self.fft_interval = fft_interval = 1.0/20
        self.decimation = decimation = hardware_rate / oversampled_width
        self.channelizer_map = channelizer_map = 5,6,7,0,1,2,3
        self.channel_names = channel_names = map(lambda x: "%.3fMHz" % (162.4 + (x*0.025)), channel_map)
        self.chan_num = chan_num = 3

        ##################################################
        # Blocks
        ##################################################
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0.set_clock_source("external", 0)
        self.uhd_usrp_source_0.set_subdev_spec("A:0", 0)
        self.uhd_usrp_source_0.set_samp_rate(hardware_rate)
        self.uhd_usrp_source_0.set_center_freq(tuner_freq, 0)
        self.uhd_usrp_source_0.set_gain(30, 0)
        self.uhd_usrp_source_0.set_antenna("TX/RX", 0)
        self.qtgui_sink_x_0_0 = qtgui.sink_c(
        	1024, #fftsize
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	hardware_rate, #bw
        	"Radio Samples", #name
        	True, #plotfreq
        	False, #plotwaterfall
        	False, #plottime
        	False, #plotconst
        )
        self.qtgui_sink_x_0_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_0_win = sip.wrapinstance(self.qtgui_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_sink_x_0_0_win, 0,0,1,2)
        
        self.qtgui_sink_x_0_0.enable_rf_freq(False)
        
        
          
        self.qtgui_sink_x_0 = qtgui.sink_c(
        	1024, #fftsize
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	hardware_rate/decimation, #bw
        	"Filtered Samples", #name
        	True, #plotfreq
        	False, #plotwaterfall
        	False, #plottime
        	False, #plotconst
        )
        self.qtgui_sink_x_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_sink_x_0_win, 0,2,1,2)
        
        self.qtgui_sink_x_0.enable_rf_freq(False)
        
        
          
        self.pfb_channelizer_ccf_0 = pfb.channelizer_ccf(
        	  noaa_num_chans+1,
        	  (pfb_taps),
        	  1,
        	  1)
        self.pfb_channelizer_ccf_0.set_channel_map((channelizer_map))
        self.pfb_channelizer_ccf_0.declare_sample_delay(0)
        	
        self.freq_xlating_fft_filter_ccc_0 = filter.freq_xlating_fft_filter_ccc(int(decimation), (lpf_taps), tuner_offset  + ppm_corr, hardware_rate)
        self.freq_xlating_fft_filter_ccc_0.set_nthreads(1)
        self.freq_xlating_fft_filter_ccc_0.declare_sample_delay(0)
        self.blocks_null_sink_0_5 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_0_4 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_0_3 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_0_2_0 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_0_2 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_0_1 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_0_0 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_gr_complex*1)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.freq_xlating_fft_filter_ccc_0, 0), (self.pfb_channelizer_ccf_0, 0))    
        self.connect((self.freq_xlating_fft_filter_ccc_0, 0), (self.qtgui_sink_x_0, 0))    
        self.connect((self.pfb_channelizer_ccf_0, 0), (self.blocks_null_sink_0, 0))    
        self.connect((self.pfb_channelizer_ccf_0, 5), (self.blocks_null_sink_0_0, 0))    
        self.connect((self.pfb_channelizer_ccf_0, 1), (self.blocks_null_sink_0_1, 0))    
        self.connect((self.pfb_channelizer_ccf_0, 2), (self.blocks_null_sink_0_2, 0))    
        self.connect((self.pfb_channelizer_ccf_0, 3), (self.blocks_null_sink_0_2_0, 0))    
        self.connect((self.pfb_channelizer_ccf_0, 4), (self.blocks_null_sink_0_3, 0))    
        self.connect((self.pfb_channelizer_ccf_0, 6), (self.blocks_null_sink_0_4, 0))    
        self.connect((self.pfb_channelizer_ccf_0, 7), (self.blocks_null_sink_0_5, 0))    
        self.connect((self.uhd_usrp_source_0, 0), (self.freq_xlating_fft_filter_ccc_0, 0))    
        self.connect((self.uhd_usrp_source_0, 0), (self.qtgui_sink_x_0_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "amplitude_loss_test")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_noaa_num_chans(self):
        return self.noaa_num_chans

    def set_noaa_num_chans(self, noaa_num_chans):
        self.noaa_num_chans = noaa_num_chans
        self.set_channel_map(range(0, self.noaa_num_chans))
        self.set_noaa_band_end(self.noaa_band_start + (self.noaa_num_chans * self.noaa_chan_width))
        self.set_oversampled_width(self.noaa_chan_width * (self.noaa_num_chans + 1))
        self.set_noaa_band_width(self.noaa_chan_width * self.noaa_num_chans)
        self.set_noaa_band_center(self.noaa_band_start + (self.noaa_num_chans / 2 * self.noaa_chan_width))

    def get_noaa_chan_width(self):
        return self.noaa_chan_width

    def set_noaa_chan_width(self, noaa_chan_width):
        self.noaa_chan_width = noaa_chan_width
        self.set_noaa_band_end(self.noaa_band_start + (self.noaa_num_chans * self.noaa_chan_width))
        self.set_oversampled_width(self.noaa_chan_width * (self.noaa_num_chans + 1))
        self.set_noaa_band_width(self.noaa_chan_width * self.noaa_num_chans)
        self.set_lpf_taps(firdes.low_pass(1.0, self.hardware_rate, self.oversampled_width / 2,self.noaa_chan_width, firdes.WIN_HAMMING, 6.76)
        )
        self.set_noaa_band_center(self.noaa_band_start + (self.noaa_num_chans / 2 * self.noaa_chan_width))

    def get_noaa_band_start(self):
        return self.noaa_band_start

    def set_noaa_band_start(self, noaa_band_start):
        self.noaa_band_start = noaa_band_start
        self.set_noaa_band_end(self.noaa_band_start + (self.noaa_num_chans * self.noaa_chan_width))
        self.set_noaa_band_center(self.noaa_band_start + (self.noaa_num_chans / 2 * self.noaa_chan_width))

    def get_oversampled_width(self):
        return self.oversampled_width

    def set_oversampled_width(self, oversampled_width):
        self.oversampled_width = oversampled_width
        self.set_pfb_taps(firdes.low_pass(2.0, self.oversampled_width, self.noaa_fm_dev*2 ,1000, firdes.WIN_HAMMING, 6.76))
        self.set_decimation(self.hardware_rate / self.oversampled_width)
        self.set_lpf_taps(firdes.low_pass(1.0, self.hardware_rate, self.oversampled_width / 2,self.noaa_chan_width, firdes.WIN_HAMMING, 6.76)
        )

    def get_noaa_fm_dev(self):
        return self.noaa_fm_dev

    def set_noaa_fm_dev(self, noaa_fm_dev):
        self.noaa_fm_dev = noaa_fm_dev
        self.set_pfb_taps(firdes.low_pass(2.0, self.oversampled_width, self.noaa_fm_dev*2 ,1000, firdes.WIN_HAMMING, 6.76))

    def get_noaa_band_center(self):
        return self.noaa_band_center

    def set_noaa_band_center(self, noaa_band_center):
        self.noaa_band_center = noaa_band_center
        self.set_target_freq(self.noaa_band_center)

    def get_hardware_rate(self):
        return self.hardware_rate

    def set_hardware_rate(self, hardware_rate):
        self.hardware_rate = hardware_rate
        self.set_decimation(self.hardware_rate / self.oversampled_width)
        self.set_lpf_taps(firdes.low_pass(1.0, self.hardware_rate, self.oversampled_width / 2,self.noaa_chan_width, firdes.WIN_HAMMING, 6.76)
        )
        self.qtgui_sink_x_0.set_frequency_range(0, self.hardware_rate/self.decimation)
        self.qtgui_sink_x_0_0.set_frequency_range(0, self.hardware_rate)
        self.uhd_usrp_source_0.set_samp_rate(self.hardware_rate)

    def get_tuner_freq(self):
        return self.tuner_freq

    def set_tuner_freq(self, tuner_freq):
        self.tuner_freq = tuner_freq
        self.set_ppm_corr(self.tuner_freq * (self.ppm/1e6))
        self.set_tuner_offset(self.target_freq - self.tuner_freq)
        self.uhd_usrp_source_0.set_center_freq(self.tuner_freq, 0)

    def get_target_freq(self):
        return self.target_freq

    def set_target_freq(self, target_freq):
        self.target_freq = target_freq
        self.set_tuner_offset(self.target_freq - self.tuner_freq)

    def get_ppm(self):
        return self.ppm

    def set_ppm(self, ppm):
        self.ppm = ppm
        self.set_ppm_corr(self.tuner_freq * (self.ppm/1e6))

    def get_pfb_taps(self):
        return self.pfb_taps

    def set_pfb_taps(self, pfb_taps):
        self.pfb_taps = pfb_taps
        self.set_pfb_sizeof_taps(len(self.pfb_taps))
        self.pfb_channelizer_ccf_0.set_taps((self.pfb_taps))

    def get_lpf_taps(self):
        return self.lpf_taps

    def set_lpf_taps(self, lpf_taps):
        self.lpf_taps = lpf_taps
        self.set_lpf_sizeof_taps(len(self.lpf_taps))
        self.freq_xlating_fft_filter_ccc_0.set_taps((self.lpf_taps))

    def get_channel_map(self):
        return self.channel_map

    def set_channel_map(self, channel_map):
        self.channel_map = channel_map
        self.set_channel_names(map(lambda x: "%.3fMHz" % (162.4 + (x*0.025)), self.channel_map))

    def get_volume(self):
        return self.volume

    def set_volume(self, volume):
        self.volume = volume

    def get_tuner_offset(self):
        return self.tuner_offset

    def set_tuner_offset(self, tuner_offset):
        self.tuner_offset = tuner_offset
        self.freq_xlating_fft_filter_ccc_0.set_center_freq(self.tuner_offset  + self.ppm_corr)

    def get_ppm_corr(self):
        return self.ppm_corr

    def set_ppm_corr(self, ppm_corr):
        self.ppm_corr = ppm_corr
        self.freq_xlating_fft_filter_ccc_0.set_center_freq(self.tuner_offset  + self.ppm_corr)

    def get_pfb_sizeof_taps(self):
        return self.pfb_sizeof_taps

    def set_pfb_sizeof_taps(self, pfb_sizeof_taps):
        self.pfb_sizeof_taps = pfb_sizeof_taps

    def get_noaa_band_width(self):
        return self.noaa_band_width

    def set_noaa_band_width(self, noaa_band_width):
        self.noaa_band_width = noaa_band_width

    def get_noaa_band_end(self):
        return self.noaa_band_end

    def set_noaa_band_end(self, noaa_band_end):
        self.noaa_band_end = noaa_band_end

    def get_lpf_sizeof_taps(self):
        return self.lpf_sizeof_taps

    def set_lpf_sizeof_taps(self, lpf_sizeof_taps):
        self.lpf_sizeof_taps = lpf_sizeof_taps

    def get_fftwidth(self):
        return self.fftwidth

    def set_fftwidth(self, fftwidth):
        self.fftwidth = fftwidth

    def get_fft_interval(self):
        return self.fft_interval

    def set_fft_interval(self, fft_interval):
        self.fft_interval = fft_interval

    def get_decimation(self):
        return self.decimation

    def set_decimation(self, decimation):
        self.decimation = decimation
        self.qtgui_sink_x_0.set_frequency_range(0, self.hardware_rate/self.decimation)

    def get_channelizer_map(self):
        return self.channelizer_map

    def set_channelizer_map(self, channelizer_map):
        self.channelizer_map = channelizer_map
        self.pfb_channelizer_ccf_0.set_channel_map((self.channelizer_map))

    def get_channel_names(self):
        return self.channel_names

    def set_channel_names(self, channel_names):
        self.channel_names = channel_names

    def get_chan_num(self):
        return self.chan_num

    def set_chan_num(self, chan_num):
        self.chan_num = chan_num

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    if gr.enable_realtime_scheduling() != gr.RT_OK:
        print "Error: failed to enable realtime scheduling."
    if(StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0")):
        Qt.QApplication.setGraphicsSystem(gr.prefs().get_string('qtgui','style','raster'))
    qapp = Qt.QApplication(sys.argv)
    tb = amplitude_loss_test()
    tb.start(512)
    tb.show()
    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()
    tb = None #to clean up Qt widgets
