import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog, QLabel, QWidget, QMainWindow
from PyQt5.QtGui import QPalette, QBrush, QPixmap
from UI import Ui_MainWindow as UiM
from FG import FG_MainWindow as FGM
import librosa
import matplotlib.pyplot as plt
import librosa.display
import IPython.display as ipd
import pygame.mixer as sounds


sounds.init()


class Window2(QDialog,FGM):
    def __init__(self):
        super().__init__()
        self.setupFG(self)
        self.is_pause = True

    def START(self,F):
        sounds.music.load(F)
        if self.is_pause:
            self.is_pause = False
            sounds.music.play()
            self.FGPB.setStyleSheet("border-image:url(:/PAUSE.png)")
        else:
            self.is_pause = True
            sounds.music.pause()
            self.FGPB.setStyleSheet("border-image:url(:/STAR.png)")

    def Plot(self,F):
        x, sr = librosa.load(F)
        plt.figure(figsize=(14,5))
        librosa.display.waveplot(x, sr)
        plt.savefig('P:\\Python_examples\\Project\\waveplot.jpg')
        pix = QPixmap('waveplot.jpg')
        self.label.setPixmap(pix)
        self.label.setScaledContents(True)
