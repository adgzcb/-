import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog
from UI import Ui_MainWindow as UiM
import window2 as w2


class AppWindow(QDialog,UiM):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.UIPB.clicked.connect(lambda: self.load_data(0))
        self.filename = ''

    def load_data(self,i):
        self.i = i
        if self.i == 0:
            self.filename, self.filetype = QFileDialog.getOpenFileName(self,"Open File", "./", "(*.wav)")
            if self.filename != '':
                self.UIlabel.setText(self.filename)
        else:
            return self.filename


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = AppWindow()
    s = w2.Window2()

    def getfilename():
        F = w.load_data(1)
        s.FGPB.clicked.connect(lambda: s.START(F))
        s.FGPB_3.clicked.connect(lambda: s.Plot(F))
    w.UIPB_2.clicked.connect(lambda: [s.show(),getfilename()])
    w.show()
    sys.exit(app.exec_())
