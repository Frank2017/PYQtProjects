# coding=UTF-8
import sys
from PyQt5 import QtCore, QtWidgets,QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_MainWindow import Ui_MainWindow


class Controller(QMainWindow,Ui_MainWindow):
    def __init__(self):
        # 初始化父类
        super(Controller, self).__init__()
        #初始化UI界面
        self.setupUi(self)
        self.retranslateUi(self)
        # 为UI界面上控件加载slot事件绑定,为防止多次绑定，最好是将绑定操作加在__init__里面

        # 将slot和signal进行绑定
        QtCore.QMetaObject.connectSlotsByName(self)