# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi

import matplotlib as mpl
import numpy as np

mpl.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib import style
# from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar
from matplotlib.dates import date2num, MinuteLocator, SecondLocator, DateFormatter

from PyQt5 import QtWidgets

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 汉化
mpl.rcParams['axes.unicode_minus'] = False  # 防止负号乱码
style.use('bmh')


# class CustomToolbar(NavigationToolbar):
#     def __init__(self, canvas_, parent_):
#         self.toolitems = (
#             ('Home', 'Lorem ipsum dolor sit amet', 'home', 'home'),
#             ('Back', 'consectetuer adipiscing elit', 'back', 'back'),
#             ('Forward', 'sed diam nonummy nibh euismod', 'forward', 'forward'),
#             (None, None, None, None),
#             ('Pan', 'tincidunt ut laoreet', 'move', 'pan'),
#             ('Zoom', 'dolore magna aliquam', 'zoom_to_rect', 'zoom'),
#             (None, None, None, None),
#             # ('Subplots', 'putamus parum claram', 'subplots', 'configure_subplots'),
#             ('Save', 'sollemnes in futurum', 'filesave', 'save_figure'),
#         )
#         NavigationToolbar.__init__(self, canvas_, parent_)


class MplCanvas(FigureCanvas):

    def __init__(self):
        self.fig = Figure()

        self.ax = self.fig.add_subplot(111)

        # self.fig.autofmt_xdate(rotation=0, ha='center')  # 自动x轴显示

        # self.fig.tight_layout()

        self.fig.subplots_adjust(left=0.08, bottom=0.1, right=0.95, top=0.95, hspace=0, wspace=0)

        FigureCanvas.__init__(self, self.fig)

        FigureCanvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        FigureCanvas.updateGeometry(self)

        font = {'color': 'darkred',
                'weight': 'normal',
                'size': 9,
                }

        self.ax.set_xlabel(u"时间(s)", fontdict=font, labelpad=0)

        self.ax.set_ylabel(u'电场(kV/m)', fontdict=font, labelpad=0)

        # self.ax.set_title('Dynamic line chart')

        # self.ax.grid()  # 开启网格

        # self.ax.xaxis.set_major_locator(MinuteLocator())  # every minute is a major locator
        #
        # self.ax.xaxis.set_minor_locator(SecondLocator([10, 20, 30, 40, 50]))  # every 10 second is a minor locator
        #
        # self.ax.xaxis.set_major_formatter(DateFormatter('%H:%M:%S'))  # tick label formatter
        #
        # self.ax.xaxis.set_minor_formatter(DateFormatter('%S'))  # tick label formatter

        self.curveObj = None  # draw object
        # self.curveObj2 = None  # draw object

    def plot(self, datax, datay):
        datax = np.array(datax)
        datay = np.array(datay)
        # datay2 = signal.medfilt(datay, 5)  # 中值滤波
        if self.curveObj:
            self.ax.lines.remove(self.curveObj)

        self.curveObj, = self.ax.plot(datax, datay, '.-', linewidth=1)
        self.ax.legend(loc="upper left")
        self.draw()


class MyGraph(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.canvas = MplCanvas()
        self.vbl = QtWidgets.QVBoxLayout()
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)
        self.databuflimit = int(12 * 60 * 85)

    def generateData(self, dataX, dataY):
        self.canvas.plot(dataX, dataY)
