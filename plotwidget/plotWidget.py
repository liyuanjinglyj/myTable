# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plotWidget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import matplotlib
from PyQt5 import QtCore, QtWidgets
matplotlib.use("qt5agg")  # 声明使用QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.colors as col
import matplotlib.cm as cm
import pandas  as pd
from plotwidget.plotThread import plotThread


class Figure_Canvas(
    FigureCanvas):  # 通过继承FigureCanvas类，使得该类既是一个PyQt5的Qwidget，又是一个matplotlib的FigureCanvas，这是连接pyqt5与matplot                                          lib的关键

    def __init__(self, parent=None, width=11, height=5, dpi=100):
        self.fig = Figure(figsize=(width, height),
                          dpi=100)  # 创建一个Figure，注意：该Figure为matplotlib下的figure，不是matplotlib.pyplot下面的figure
        FigureCanvas.__init__(self, self.fig)  # 初始化父类
        self.setParent(parent)
        self.axes = self.fig.add_subplot(111)
        FigureCanvas.updateGeometry(self)
        matplotlib.rcParams['font.sans-serif'] = ['SimHei']
        matplotlib.rcParams['font.family'] = 'sans-serif'
        matplotlib.rcParams['axes.unicode_minus'] = False

    def test(self, x, y, title=U'每月发帖量走势图', xlabel=u'年份日期（年，月）', ylabel=u'数据量（个）', type=1):
        self.axes.clear()
        self.fig.canvas.draw_idle()
        if type == 1:
            self.axes.plot(x, y, 'r', linestyle='--', marker='o')
            for i, j in zip(x, y):
                self.axes.annotate('%s' % (j), xy=(i, j), xytext=(0, 15), textcoords='offset points', ha='center')
            self.axes.grid()
            self.axes.set_title(title, fontsize='large', fontweight='bold')
            self.axes.set_xlabel(xlabel)
            self.axes.set_ylabel(ylabel)
            self.axes.tick_params(axis='x', labelsize=7, rotation=45, colors='red')
        else:
            patterns = {'-', '+', 'x', '\\', '*', 'o', '0', '.', 'v', '^', '1', '2', '3', '4', '8', 's', 'p', 'h'}
            camp1 = cm.ScalarMappable(col.Normalize(min(y), max(y) + 20), cm.hot)
            bars = self.axes.bar(x, y, alpha=0.5, color=camp1.to_rgba(y), edgecolor='red', label=u'柱形图')
            for bar, pattern in zip(bars, patterns):
                bar.set_hatch(pattern)
            for i, j in zip(x, y):
                self.axes.annotate('%s' % (j), xy=(i, j), xytext=(0, 25), textcoords='offset points', ha='center',
                                   arrowprops=dict(facecolor='black', shrink=0.15), fontsize=7)
            self.axes.grid()
            self.axes.set_title(title, fontsize='large', fontweight='bold')
            self.axes.set_xlabel(xlabel, fontsize=15)
            self.axes.set_ylabel(ylabel, fontsize=15)
            self.axes.legend(loc='upper left')
            self.axes.tick_params(axis='x', labelsize=7, rotation=45, colors='red')


class Ui_Form(QtWidgets.QWidget):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1200, 700)
        self.graphicsView = QtWidgets.QGraphicsView(Form)
        self.graphicsView.setGeometry(QtCore.QRect(30, 140, 1120, 550))
        self.graphicsView.setObjectName("graphicsView")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 30, 61, 16))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(110, 30, 291, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 54, 16))
        self.label_2.setObjectName("label_2")
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(110, 80, 291, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        # self.df = pd.read_excel(r'E:\Projects\PyCharmProjects\myTable\shuju.xlsx')
        self.name_id = '云月静'
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "图表走势图"))
        self.label.setText(_translate("Form", "用户昵称："))
        self.comboBox.setItemText(0, _translate("Form", "云月静"))
        self.comboBox.setItemText(1, _translate("Form", "欢乐的小机友"))
        self.comboBox.setItemText(2, _translate("Form", "鹏飞小哥"))
        self.comboBox.setItemText(3, _translate("Form", "云谷择城"))
        self.comboBox.setItemText(4, _translate("Form", "择城终老"))
        self.comboBox.setItemText(5, _translate("Form", "彧幃"))
        self.comboBox.setItemText(6, _translate("Form", "小三爷说数码"))
        self.label_2.setText(_translate("Form", "图标详情："))
        self.comboBox_2.setItemText(0, _translate("Form", "每月发帖量走势图"))
        self.comboBox_2.setItemText(1, _translate("Form", "每月总浏览量走势图"))
        self.comboBox_2.setItemText(2, _translate("Form", "每月总评论量走势图"))
        self.comboBox_2.setItemText(3, _translate("Form", "每月单帖最高浏览量柱形图"))
        self.comboBox_2.setItemText(4, _translate("Form", "每月单帖最高评论量柱形图"))
        self.comboBox.currentIndexChanged.connect(self.comboBox_clicked)
        self.comboBox_2.activated.connect(self.comboBox_2_clicked)
        self.getDataFrame()

    #获取云端数据库信息
    def getDataFrame(self):
        self.thread = plotThread()
        self.thread._signal.connect(self.plotThread_callbacklog)
        self.thread.start()

    #槽函数接受返回云端数据信息
    def plotThread_callbacklog(self, dataFrame):
        self.df = dataFrame
        self.init_view()

    # 初始化界面
    def init_view(self):
        dr = Figure_Canvas()
        x = []
        y = []
        df = self.df.copy()
        df['s_date'] = pd.to_datetime(df['s_date'])
        df = df.set_index('s_date')
        data = df[df['s_nameId'] == self.name_id].resample('M').count().reset_index(drop=False)
        for index, row in data.iterrows():
            y.append(row['s_url'])
            x.append(str(row['s_date'].year)[-2:] + str(row['s_date'].month))
        dr.test(x, y, title=U'每月发帖量走势图')
        graphicscene = QtWidgets.QGraphicsScene()
        graphicscene.addWidget(dr)
        self.graphicsView.setScene(graphicscene)
        self.graphicsView.show()

    def comboBox_clicked(self, index):
        if index == 0:
            self.name_id = '云月静'
        elif index == 1:
            self.name_id = '欢乐的小机友'
        elif index == 2:
            self.name_id = '鹏飞小哥'
        elif index == 3:
            self.name_id = '云谷择城'
        elif index == 4:
            self.name_id = '择城终老'
        elif index == 5:
            self.name_id = '彧幃'
        elif index == 6:
            self.name_id = '小三爷说数码'
        else:
            return

    def comboBox_2_clicked(self, index):
        dr = Figure_Canvas()
        self.comboBox_2_activated(dr, index)
        graphicscene = QtWidgets.QGraphicsScene()
        graphicscene.addWidget(dr)
        self.graphicsView.setScene(graphicscene)  # 第五步，把QGraphicsScene放入QGraphicsView
        self.graphicsView.show()  # 最后，调用show方法呈现图形！Voila!!

    def comboBox_2_activated(self, dr, index):
        x = []
        y = []
        df = self.df.copy()
        df['s_date'] = pd.to_datetime(df['s_date'])
        df = df.set_index('s_date')
        if index == 0:
            data = df[df['s_nameId'] == self.name_id].resample('M').count().reset_index(drop=False)
            for index, row in data.iterrows():
                y.append(row['s_url'])
                x.append(str(row['s_date'].year)[-2:] + str(row['s_date'].month))
            dr.test(x, y, title=U'每月发帖量走势图')
        elif index == 1:
            data = df[df['s_nameId'] == self.name_id].resample('M').sum().reset_index(drop=False)
            for index, row in data.iterrows():
                y.append(row['s_count'])
                x.append(str(row['s_date'].year)[-2:] + str(row['s_date'].month))
            dr.test(x, y, title=U'每月总浏览量走势图')
        elif index == 2:
            data = df[df['s_nameId'] == self.name_id].resample('M').sum().reset_index(drop=False)
            for index, row in data.iterrows():
                y.append(row['s_comment'])
                x.append(str(row['s_date'].year)[-2:] + str(row['s_date'].month))
            dr.test(x, y, title=U'每月总评论量走势图')
        elif index == 3:
            data = df[df['s_nameId'] == self.name_id].resample('M')['s_count'].max().reset_index(drop=False)
            for index, row in data.iterrows():
                if pd.isnull(row['s_count']):
                    y.append(0)
                else:
                    y.append(row['s_count'])
                x.append(str(row['s_date'].year)[-2:] + str(row['s_date'].month))
            dr.test(x, y, title=U'每月单帖最高浏览量柱形图', type=2)
        elif index == 4:
            data = df[df['s_nameId'] == self.name_id].resample('M')['s_comment'].max().reset_index(drop=False)
            for index, row in data.iterrows():
                if pd.isnull(row['s_comment']):
                    y.append(0)
                else:
                    y.append(row['s_comment'])
                x.append(str(row['s_date'].year)[-2:] + str(row['s_date'].month))
            dr.test(x, y, title=U'每月单帖最高评论量柱形图', type=2)
        else:
            return


'''
    # 每月发帖量走势图
    def totalnumber_volume(self, dr):
        x = []
        y = []
        df = self.df.copy()
        df['日期'] = pd.to_datetime(df['日期'])
        df = df.set_index('日期')
        data = df[df['昵称'] == self.name_id].resample('M').count().reset_index(drop=False)
        for index, row in data.iterrows():
            y.append(row['链接'])
            x.append(str(row['日期'].year)[-2:] + str(row['日期'].month))
        dr.test(x, y, title=U'每月发帖量走势图')

    # 评论量走势图
    def comments_volume(self, dr):
        x = []
        y = []
        df = self.df.copy()
        df['日期'] = pd.to_datetime(df['日期'])
        df = df.set_index('日期')
        data = df[df['昵称'] == self.name_id].resample('M').sum().reset_index(drop=False)
        data['日期'] = pd.to_datetime(data['日期'])
        for index, row in data.iterrows():
            y.append(row['评论量'])
            x.append(str(row['日期'].year)[-2:] + str(row['日期'].month))
        dr.test(x, y, title=U'每月总评论量走势图')

    # 浏览量走势图
    def pageview_volume(self, dr):
        x = []
        y = []
        df = self.df.copy()
        df['日期'] = pd.to_datetime(df['日期'])
        df = df.set_index('日期')
        data = df[df['昵称'] == self.name_id].resample('M').sum().reset_index(drop=False)
        data['日期'] = pd.to_datetime(data['日期'])
        for index, row in data.iterrows():
            y.append(row['浏览量'])
            x.append(str(row['日期'].year)[-2:] + str(row['日期'].month))
        dr.test(x, y, title=U'每月总浏览量走势图')

    # 浏览量最大柱形图
    def pageview_max_volume(self, dr):
        x = []
        y = []
        df = self.df.copy()
        df['日期'] = pd.to_datetime(df['日期'])
        df = df.set_index('日期')
        data = df[df['昵称'] == self.name_id].resample('M')['浏览量'].max().reset_index(drop=False)
        data['日期'] = pd.to_datetime(data['日期'])
        for index, row in data.iterrows():
            if pd.isnull(row['浏览量']):
                y.append(0)
            else:
                y.append(row['浏览量'])
            x.append(str(row['日期'].year)[-2:] + str(row['日期'].month))
        dr.test(x, y, title=U'每月单帖最高浏览量柱形图', type=2)
'''
