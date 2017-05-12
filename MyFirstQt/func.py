# coding=UTF-8

import sys
from PyQt5 import QtCore, QtWidgets,QtGui
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
        self.BrowseBtn.clicked.connect(self.BrowseBtnClick)
        self.listWidget.itemClicked.connect(self.ListItemClick)
        self.OutBtn.clicked.connect(self.OutBtnClick)
        self.listWidget.customContextMenuRequested[QtCore.QPoint].connect(self.ListWidgetsContext)
        # 将slot和signal进行绑定
        QtCore.QMetaObject.connectSlotsByName(self)

    def BrowseBtnClick(self):
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

    def ListWidgetsContext(self, point):
        listItemMenu = QtWidgets.QMenu()
        if QtWidgets.QListWidget.itemAt(self.listWidget,point) != None:
            editAction = QtWidgets.QAction(u'修改',self.listWidget)
            editAction.triggered.connect(self.EditListItem)
            listItemMenu.addAction(editAction)
        listItemMenu.exec_(QtGui.QCursor.pos())

    def EditListItem(self):
        item = self.listWidget.currentItem()
        item.setText("Modify " + item.text())

    def OutBtnClick(self):
        text,ok = QtWidgets.QInputDialog.getText(self,'Inut Password','Enter Password:')
        if ok:
            itemLen = self.listWidget.count()
            self.listWidget.insertItem(itemLen+1, QtWidgets.QListWidgetItem(self.tr(text)))