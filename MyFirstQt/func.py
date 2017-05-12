# coding=UTF-8

import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from first_qt import Ui_MainWindow


class Controller(QMainWindow,Ui_MainWindow):
    def __init__(self):
        # 初始化父类
        super(Controller, self).__init__()
        #初始化UI界面
        self.setupUi(self)
        self.retranslateUi(self)
        # 为UI界面上控件加载slot事件绑定,为防止多次绑定，最好是将绑定操作加在__init__里面
        self.BrowseBtn.clicked.connect(self.BrowseBtn_click)
        self.listWidget.itemClicked.connect(self.ListItemClick)
        # 将slot和signal进行绑定
        QtCore.QMetaObject.connectSlotsByName(self)

    def BrowseBtn_click(self):
        directory = QtCore.QDir.currentPath()
        self.lineEdit.setText(directory)
        if self.listWidget.count() > 0:
            self.listWidget.clear()
        self.ShowDir()
        pass


    def ShowDir(self):
        path = self.lineEdit.text()
        self.currentDir = QtCore.QDir(path)
        files = self.currentDir.entryList(QtCore.QDir.Files | QtCore.QDir.NoSymLinks)
        listfiles = []
        for f in files:
            listfiles.append(QtWidgets.QListWidgetItem(self.tr(f)))
        index = 0
        for lf in listfiles:
            index += 1
            self.listWidget.insertItem(index, lf)
        pass


    def ListItemClick(self, obj):
        QtWidgets.QMessageBox.warning(self.listWidget, "warning", obj.text(), QtWidgets.QMessageBox.Yes)
        pass
