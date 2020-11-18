#-*-coding:utf-8-*-
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import numpy as np
from testplot2pyqt5 import Ui_Dialog
import matplotlib
matplotlib.use("Qt5Agg")  # 宣告使用QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
#建立一個matplotlib圖形繪製類
class MyFigure(FigureCanvas):
    def __init__(self,width=5, height=4, dpi=100):
        #第一步：建立一個建立Figure
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        #第二步：在父類中啟用Figure視窗
        super(MyFigure,self).__init__(self.fig) #此句必不可少，否則不能顯示圖形
        #第三步：建立一個子圖，用於繪製圖形用，111表示子圖編號，如matlab的subplot(1,1,1)
        self.axes = self.fig.add_subplot(111)
        #第四步：就是畫圖，【可以在此類中畫，也可以在其它類中畫】
    def plotsin(self):
        self.axes0 = self.fig.add_subplot(111)
        t = np.arange(0.0, 3.0, 0.01)
        s = np.sin(2 * np.pi * t)
        self.axes0.plot(t, s)
    def plotcos(self):
        t = np.arange(0.0, 3.0, 0.01)
        s = np.sin(2 * np.pi * t)
        self.axes.plot(t, s)
class MainDialogImgBW(QDialog,Ui_Dialog):
    def __init__(self):
        super(MainDialogImgBW,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("顯示matplotlib繪製圖形")
        self.setMinimumSize(0,0)
        #第五步：定義MyFigure類的一個例項
        self.F = MyFigure(width=3, height=2, dpi=100)
        #self.F.plotsin()
        self.plotcos()
        #第六步：在GUI的groupBox中建立一個佈局，用於新增MyFigure類的例項（即圖形）後其他部件。
        self.gridlayout = QGridLayout(self.groupBox)  # 繼承容器groupBox
        self.gridlayout.addWidget(self.F,0,1)
        #補充：另建立一個例項繪圖並顯示
        self.plotother()
    def plotcos(self):
        t = np.arange(0.0, 5.0, 0.01)
        s = np.cos(2 * np.pi * t)
        self.F.axes.plot(t, s)
        self.F.fig.suptitle("cos")
    def plotother(self):
        F1 = MyFigure(width=5, height=4, dpi=100)
        F1.fig.suptitle("Figuer_4")
        F1.axes1 = F1.fig.add_subplot(221)
        x = np.arange(0, 50)
        y = np.random.rand(50)
        F1.axes1.hist(y, bins=50)
        F1.axes1.plot(x, y)
        F1.axes1.bar(x, y)
        F1.axes1.set_title("hist")
        F1.axes2 = F1.fig.add_subplot(222)
        ## 呼叫figure下面的add_subplot方法，類似於matplotlib.pyplot下面的subplot方法
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        y = [23, 21, 32, 13, 3, 132, 13, 3, 1]
        F1.axes2.plot(x, y)
        F1.axes2.set_title("line")
        # 散點圖
        F1.axes3 = F1.fig.add_subplot(223)
        F1.axes3.scatter(np.random.rand(20), np.random.rand(20))
        F1.axes3.set_title("scatter")
        # 折線圖
        F1.axes4 = F1.fig.add_subplot(224)
        x = np.arange(0, 5, 0.1)
        F1.axes4.plot(x, np.sin(x), x, np.cos(x))
        F1.axes4.set_title("sincos")
        self.gridlayout.addWidget(F1, 0, 2)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainDialogImgBW()
    main.show()
    #app.installEventFilter(main)
    sys.exit(app.exec_())