#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Parallella Streaming
# GNU Radio version: 3.8.1.0

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import fosphor
from gnuradio.fft import window
from gnuradio import blocks
import pmt
from gnuradio import gr
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import qtgui

class parallella_streaming(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Parallella Streaming")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Parallella Streaming")
        qtgui.util.check_set_qss()
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

        self.settings = Qt.QSettings("GNU Radio", "parallella_streaming")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 2500000

        ##################################################
        # Blocks
        ##################################################
        self.tab_widget_0 = Qt.QTabWidget()
        self.tab_widget_0_widget_0 = Qt.QWidget()
        self.tab_widget_0_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_0_widget_0)
        self.tab_widget_0_grid_layout_0 = Qt.QGridLayout()
        self.tab_widget_0_layout_0.addLayout(self.tab_widget_0_grid_layout_0)
        self.tab_widget_0.addTab(self.tab_widget_0_widget_0, 'Frequency')
        self.tab_widget_0_widget_1 = Qt.QWidget()
        self.tab_widget_0_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_0_widget_1)
        self.tab_widget_0_grid_layout_1 = Qt.QGridLayout()
        self.tab_widget_0_layout_1.addLayout(self.tab_widget_0_grid_layout_1)
        self.tab_widget_0.addTab(self.tab_widget_0_widget_1, 'Time')
        self.top_grid_layout.addWidget(self.tab_widget_0)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
            1024, #size
            samp_rate, #samp_rate
            "", #name
            8 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-10000, 10000)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_NORM, qtgui.TRIG_SLOPE_POS, 0.0, 0, 1, "Ohradnik")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(True)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(True)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)


        labels = ['1I', '1Q', '2I', '2Q', '3I',
            '3Q', '4I', '4Q', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'green', 'green', 'black', 'yellow',
            'dark blue', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(8):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.tab_widget_0_layout_1.addWidget(self._qtgui_time_sink_x_0_win)
        self.fosphor_qt_sink_c_0_0_0_0 = fosphor.qt_sink_c()
        self.fosphor_qt_sink_c_0_0_0_0.set_fft_window(firdes.WIN_BLACKMAN_hARRIS)
        self.fosphor_qt_sink_c_0_0_0_0.set_frequency_range(0, samp_rate)
        self._fosphor_qt_sink_c_0_0_0_0_win = sip.wrapinstance(self.fosphor_qt_sink_c_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.tab_widget_0_grid_layout_0.addWidget(self._fosphor_qt_sink_c_0_0_0_0_win, 1, 1, 1, 1)
        for r in range(1, 2):
            self.tab_widget_0_grid_layout_0.setRowStretch(r, 1)
        for c in range(1, 2):
            self.tab_widget_0_grid_layout_0.setColumnStretch(c, 1)
        self.fosphor_qt_sink_c_0_0_0 = fosphor.qt_sink_c()
        self.fosphor_qt_sink_c_0_0_0.set_fft_window(firdes.WIN_BLACKMAN_hARRIS)
        self.fosphor_qt_sink_c_0_0_0.set_frequency_range(0, samp_rate)
        self._fosphor_qt_sink_c_0_0_0_win = sip.wrapinstance(self.fosphor_qt_sink_c_0_0_0.pyqwidget(), Qt.QWidget)
        self.tab_widget_0_grid_layout_0.addWidget(self._fosphor_qt_sink_c_0_0_0_win, 1, 0, 1, 1)
        for r in range(1, 2):
            self.tab_widget_0_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.tab_widget_0_grid_layout_0.setColumnStretch(c, 1)
        self.fosphor_qt_sink_c_0_0 = fosphor.qt_sink_c()
        self.fosphor_qt_sink_c_0_0.set_fft_window(firdes.WIN_BLACKMAN_hARRIS)
        self.fosphor_qt_sink_c_0_0.set_frequency_range(0, samp_rate)
        self._fosphor_qt_sink_c_0_0_win = sip.wrapinstance(self.fosphor_qt_sink_c_0_0.pyqwidget(), Qt.QWidget)
        self.tab_widget_0_grid_layout_0.addWidget(self._fosphor_qt_sink_c_0_0_win, 0, 1, 1, 1)
        for r in range(0, 1):
            self.tab_widget_0_grid_layout_0.setRowStretch(r, 1)
        for c in range(1, 2):
            self.tab_widget_0_grid_layout_0.setColumnStretch(c, 1)
        self.fosphor_qt_sink_c_0 = fosphor.qt_sink_c()
        self.fosphor_qt_sink_c_0.set_fft_window(firdes.WIN_BLACKMAN_hARRIS)
        self.fosphor_qt_sink_c_0.set_frequency_range(0, samp_rate)
        self._fosphor_qt_sink_c_0_win = sip.wrapinstance(self.fosphor_qt_sink_c_0.pyqwidget(), Qt.QWidget)
        self.tab_widget_0_grid_layout_0.addWidget(self._fosphor_qt_sink_c_0_win, 0, 0, 1, 1)
        for r in range(0, 1):
            self.tab_widget_0_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.tab_widget_0_grid_layout_0.setColumnStretch(c, 1)
        self.blocks_vector_to_streams_0 = blocks.vector_to_streams(gr.sizeof_short*1, 8)
        self.blocks_short_to_float_1_2 = blocks.short_to_float(1, 1)
        self.blocks_short_to_float_1_1 = blocks.short_to_float(1, 1)
        self.blocks_short_to_float_1_0 = blocks.short_to_float(1, 1)
        self.blocks_short_to_float_1 = blocks.short_to_float(1, 1)
        self.blocks_short_to_float_0_2 = blocks.short_to_float(1, 1)
        self.blocks_short_to_float_0_1 = blocks.short_to_float(1, 1)
        self.blocks_short_to_float_0_0 = blocks.short_to_float(1, 1)
        self.blocks_short_to_float_0 = blocks.short_to_float(1, 1)
        self.blocks_float_to_complex_0_2 = blocks.float_to_complex(1)
        self.blocks_float_to_complex_0_1 = blocks.float_to_complex(1)
        self.blocks_float_to_complex_0_0 = blocks.float_to_complex(1)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_short*8, '/dev/stdin', False, 0, 0)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_file_source_0, 0), (self.blocks_vector_to_streams_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.fosphor_qt_sink_c_0, 0))
        self.connect((self.blocks_float_to_complex_0_0, 0), (self.fosphor_qt_sink_c_0_0, 0))
        self.connect((self.blocks_float_to_complex_0_1, 0), (self.fosphor_qt_sink_c_0_0_0, 0))
        self.connect((self.blocks_float_to_complex_0_2, 0), (self.fosphor_qt_sink_c_0_0_0_0, 0))
        self.connect((self.blocks_short_to_float_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.blocks_short_to_float_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_short_to_float_0_0, 0), (self.blocks_float_to_complex_0_0, 0))
        self.connect((self.blocks_short_to_float_0_0, 0), (self.qtgui_time_sink_x_0, 2))
        self.connect((self.blocks_short_to_float_0_1, 0), (self.blocks_float_to_complex_0_1, 0))
        self.connect((self.blocks_short_to_float_0_1, 0), (self.qtgui_time_sink_x_0, 4))
        self.connect((self.blocks_short_to_float_0_2, 0), (self.blocks_float_to_complex_0_2, 0))
        self.connect((self.blocks_short_to_float_0_2, 0), (self.qtgui_time_sink_x_0, 6))
        self.connect((self.blocks_short_to_float_1, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.blocks_short_to_float_1, 0), (self.qtgui_time_sink_x_0, 1))
        self.connect((self.blocks_short_to_float_1_0, 0), (self.blocks_float_to_complex_0_0, 1))
        self.connect((self.blocks_short_to_float_1_0, 0), (self.qtgui_time_sink_x_0, 3))
        self.connect((self.blocks_short_to_float_1_1, 0), (self.blocks_float_to_complex_0_1, 1))
        self.connect((self.blocks_short_to_float_1_1, 0), (self.qtgui_time_sink_x_0, 5))
        self.connect((self.blocks_short_to_float_1_2, 0), (self.blocks_float_to_complex_0_2, 1))
        self.connect((self.blocks_short_to_float_1_2, 0), (self.qtgui_time_sink_x_0, 7))
        self.connect((self.blocks_vector_to_streams_0, 0), (self.blocks_short_to_float_0, 0))
        self.connect((self.blocks_vector_to_streams_0, 2), (self.blocks_short_to_float_0_0, 0))
        self.connect((self.blocks_vector_to_streams_0, 4), (self.blocks_short_to_float_0_1, 0))
        self.connect((self.blocks_vector_to_streams_0, 6), (self.blocks_short_to_float_0_2, 0))
        self.connect((self.blocks_vector_to_streams_0, 1), (self.blocks_short_to_float_1, 0))
        self.connect((self.blocks_vector_to_streams_0, 3), (self.blocks_short_to_float_1_0, 0))
        self.connect((self.blocks_vector_to_streams_0, 5), (self.blocks_short_to_float_1_1, 0))
        self.connect((self.blocks_vector_to_streams_0, 7), (self.blocks_short_to_float_1_2, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "parallella_streaming")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.fosphor_qt_sink_c_0.set_frequency_range(0, self.samp_rate)
        self.fosphor_qt_sink_c_0_0.set_frequency_range(0, self.samp_rate)
        self.fosphor_qt_sink_c_0_0_0.set_frequency_range(0, self.samp_rate)
        self.fosphor_qt_sink_c_0_0_0_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)



def main(top_block_cls=parallella_streaming, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def sig_handler(sig=None, frame=None):
        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
