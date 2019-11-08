# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pieWidget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import calendar
import datetime
import matplotlib
import pandas as pd
matplotlib.use("qt5agg")  # 声明使用QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5 import QtCore, QtWidgets
from plotwidget.plotThread import plotThread


class Figure_Canvas(FigureCanvas):
    def __init__(self, parent=None, width=7.8, height=5.5, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=100)
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)
        self.axes = self.fig.add_subplot(111)
        FigureCanvas.updateGeometry(self)
        matplotlib.rcParams['font.sans-serif'] = ['SimHei']
        matplotlib.rcParams['font.family'] = 'sans-serif'
        matplotlib.rcParams['axes.unicode_minus'] = False

    def test(self, x, y, title=U'每月发帖量走势图'):
        self.axes.clear()
        self.fig.canvas.draw_idle()
        for i in range(0,len(x)):
            y[i]+='('+str(x[i])+'篇)'
        self.axes.pie(x, labels=y, autopct='%1.1f%%', textprops={'fontsize': 8, 'color': 'blue'})
        self.axes.legend(loc='best', bbox_to_anchor=(1.1, 1.05), fontsize=8, borderaxespad=0.3)
        self.axes.set_title(title, fontsize=12, color='r')


class pieWidget(QtWidgets.QWidget):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(828, 705)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 40, 161, 16))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(180, 40, 271, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(100, 90, 60, 16))
        self.label_2.setObjectName("label_2")
        self.graphicsView = QtWidgets.QGraphicsView(Form)
        self.graphicsView.setGeometry(QtCore.QRect(20, 120, 799, 571))
        self.graphicsView.setObjectName("graphicsView")
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(180, 90, 271, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comIndex = 0
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "百分比图"))
        self.label.setText(_translate("Form", "选择需要查看的占比图："))
        self.comboBox.setItemText(0, _translate("Form", "用户组输出内容占比图"))
        self.comboBox.setItemText(1, _translate("Form", "各板块内容占比图"))
        self.label_2.setText(_translate("Form", "选择年月："))
        self.comboBox_2.activated.connect(self.comboBox_2_clicked)
        self.comboBox.activated.connect(self.comboBox_clicked)
        self.init_comboBox2()
        self.getDataFrame()

    def comboBox_clicked(self, index):
        if index == 0:
            self.comIndex = 0
        elif index == 1:
            self.comIndex = 1
        else:
            return

    def init_view(self):
        self.draw_pie_invitation(self.comboBox_2.currentText(), 's_nameId', u'当前年月帖子输出占比图')

    def comboBox_2_clicked(self):
        if self.comIndex == 0:
            self.draw_pie_invitation(self.comboBox_2.currentText(), 's_nameId', u'当前年月帖子输出占比图')
        elif self.comIndex == 1:
            self.draw_pie_invitation(self.comboBox_2.currentText(), 's_device', u'当前年月各板块内容占比图')
        else:
            return

    def draw_pie_invitation(self, currentText, groupText, title):
        dr = Figure_Canvas()
        x = []
        y = []
        df = self.df.copy()
        df['s_date'] = pd.to_datetime(df['s_date'])
        df = df.set_index('s_date')
        name_df = df.groupby(groupText, as_index=False)
        for name, group in name_df:
            data = group.resample('M').count().reset_index(drop=False)  # 每个总帖子数
            data2 = data[data['s_date'] == currentText]
            if len(data2.values.tolist()) <= 0 or data2.values.tolist()[0][3] <= 1:
                continue
            else:
                x.append(data2.values.tolist()[0][3])
                y.append(name)
        dr.test(x, y, title)
        graphicscene = QtWidgets.QGraphicsScene()
        graphicscene.addWidget(dr)
        self.graphicsView.setScene(graphicscene)
        self.graphicsView.show()


    def init_comboBox2(self):
        com_list = []
        now = datetime.datetime.now()
        for i in range(2017, now.year + 1):
            if i == now.year:
                for j in range(1, now.month + 1):
                    flaglist = calendar.monthrange(i, j)
                    data = str(i) + '-' + str(j) + '-' + str(flaglist[1])
                    com_list.append(data)
            elif i == 2017:
                for j in range(10, now.month + 1):
                    flaglist = calendar.monthrange(i, j)
                    data = str(i) + '-' + str(j) + '-' + str(flaglist[1])
                    com_list.append(data)
            else:
                for j in range(1, 13):
                    flaglist = calendar.monthrange(i, j)
                    data = str(i) + '-' + str(j) + '-' + str(flaglist[1])
                    com_list.append(data)
        for list in com_list:
            # print(list)
            self.comboBox_2.addItem(list)

        # 获取云端数据库信息

    def getDataFrame(self):
        self.thread = plotThread()
        self.thread._signal.connect(self.plotThread_callbacklog)
        self.thread.start()

    # 槽函数接受返回云端数据信息
    def plotThread_callbacklog(self, dataFrame):
        self.df = dataFrame
        self.init_view()
