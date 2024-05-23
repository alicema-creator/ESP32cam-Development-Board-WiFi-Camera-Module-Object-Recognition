# coding:utf-8
# import sys
import cv2
import sys
import os
import random

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import shutil
import time

from PyQt5 import QtCore, QtGui, QtWidgets
class myWin(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(myWin, self).__init__()
        self.setupUi(self)


    def videoRecog2(self):

      
        frame = cv2.cvtColor(im02, cv2.COLOR_BGR2RGB)
        height, width, bytesPerComponent = frame.shape
        bytesPerLine = bytesPerComponent * width

        self.q_image = QtGui.QImage(frame.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888) \
            .scaled(self.label.height() * 0.8, self.label.height() * 0.6)
        self.label.setPixmap(QPixmap.fromImage(self.q_image))
        self.update()


if __name__=="__main__":
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app=QtWidgets.QApplication(sys.argv)
    Widget=myWin()
    Widget.showMaximized();
    Widget.show()
    sys.exit(app.exec_())

