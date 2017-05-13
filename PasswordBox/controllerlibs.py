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
        # # 为button绑定事件
        self.AddPswBooksBtn.clicked.connect(self.AddPasswordBooks)
        self.DeletePswBooksBtn.clicked.connect(self.DeletePasswordBooks)
        self.PswBooksSelectAllBtn.clicked.connect(self.SelectAllPasswordBooks)
        self.PswClearAllBtn.clicked.connect(self.ClearAllSelectedPasswordBooks)
        self.ExportExcelBtn.clicked.connect(self.ExportExcel)

        self.SearchBtn.clicked.connect(self.SearchPsw)
        self.SearchClearBtn.clicked.connect(self.SearchInputClear)

        self.PswSelectAllBtn.clicked.connect(self.SelectAllPassword)
        self.PswClearAllBtn.clicked.connect(self.ClearAllSelectedPassword)
        self.PswBooksCloseBtn.clicked.connect(self.CloseCurPasswordBooks)
        self.AddPswBtn.clicked.connect(self.AddPassword)
        self.DeletePswBtn.clicked.connect(self.DeletePassword)

        # # 为menu绑定动作
        self.funcMenu.addAction(self.ImportExcelMenu)
        self.menuBar.addAction(self.funcMenu.menuAction())

        # 将slot和signal进行绑定
        QtCore.QMetaObject.connectSlotsByName(self)
        pass

    # 为menu 定义action
    def ImportExcelMenu(self):
        QtWidgets.QMessageBox.warning('waring','Import Excel')
        pass

    # 为PasswordBooks定义Button函数
    def AddPasswordBooks(self):
        pass

    def DeletePasswordBooks(self):
        pass

    def SelectAllPasswordBooks(self):
        pass

    def ClearAllSelectedPasswordBooks(self):
        pass

    def ExportExcel(self):
        pass

    # 为搜索定义Button函数
    def SearchPsw(self):
        pass

    def SearchInputClear(self):
        pass


    # 为password定义函数
    def SelectAllPassword(self):
        pass

    def ClearAllSelectedPassword(self):
        pass

    def CloseCurPasswordBooks(self):
        pass

    def AddPassword(self):
        pass

    def DeletePassword(self):
        pass