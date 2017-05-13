# coding=UTF-8
import sys
from PyQt5 import QtCore, QtWidgets,QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_MainWindow import Ui_MainWindow
import filemodel
import funclibs
from redefineModel import AddDialog

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
        self.PswBooksClearBtn.clicked.connect(self.ClearAllSelectedPasswordBooks)
        self.ExportExcelBtn.clicked.connect(self.ExportExcel)

        self.SearchBtn.clicked.connect(self.SearchPsw)
        self.SearchClearBtn.clicked.connect(self.SearchInputClear)

        self.PswSelectAllBtn.clicked.connect(self.SelectAllPassword)
        self.PswClearAllBtn.clicked.connect(self.ClearAllSelectedPassword)
        self.PswBooksCloseBtn.clicked.connect(self.CloseCurPasswordBooks)
        self.AddPswBtn.clicked.connect(self.AddPassword)
        self.DeletePswBtn.clicked.connect(self.DeletePassword)

        # # 为menu绑定动作
        self.ImportExcelAction.triggered.connect(self.ImportExcelMenuFunc)

        # # 为PswBooksList添加单击，双击事件
        self.PswBooksList.clicked.connect(self.PswBooksListClick)
        self.PswBooksList.doubleClicked.connect(self.PswBooksListDouClick)
        # # 为PswBooksList右键菜单绑定动作
        self.PswBooksList.customContextMenuRequested[QtCore.QPoint].connect(self.PswBooksListContext)
        # # 为PswList添加单机双击事件

        # # 为PswList添加右键菜单

        # 初始化filemodel进行存储
        self.filemodel = filemodel.FileModel()
        self.PswBooksManageVer = self.filemodel.getPswBooksManage()
        # print self.PswBooksManage
        # 将slot和signal进行绑定
        QtCore.QMetaObject.connectSlotsByName(self)

        # 初始化funclib类
        self.func = funclibs.FuncLibs(self)
        # #初始设置PseBooksList
        self.func.setPswBooksList()
        pass

    # 为menu 定义action
    def ImportExcelMenuFunc(self):
        pass

    # 为PasswordBooks定义Button函数
    def AddPasswordBooks(self):
        dialog = AddDialog('添加密码本',self.PswBooksManageVer)
        # 如果是正常结束，ok返回1，cancel返回o,关闭返回0
        # print dialog.exec_()
        if dialog.exec_():
            temp = dialog.getData()
            # 密码本管理文件的存储格式为dict， 密码本名：[MD5（password）, MD5(密码本名，用于在PswBooksDb
            # 中命名密码本存储名)]
            self.PswBooksManageVer[temp[0]] = [funclibs.getMD5(temp[1]), funclibs.getMD5(temp[0])]
            # 将内容存入文件
            self.filemodel.setPswBooksManage(self.PswBooksManageVer)
            # 设置PswBooksList
            self.func.setPswBooksList()
        pass
        dialog.destroy()

    def DeletePasswordBooks(self):
        delList = self.func.getCheckedItems(self.PswBooksList)
        # 记录PswBooksManage的备份
        manageTemp = self.PswBooksManageVer.copy()
        # 标记位 ，flag=0表示删除成功，flag=1表示删除失败
        flag = 0
        for dit in delList:
            # 若有的单词本没有被删除，修改标记为1
            if self.PswBooksManageVer.pop(dit) is None:
                flag = 1
        # 说明有的单词本未被删除，需要回滚
        if flag == 1:
            self.PswBooksManageVer.clear()
            self.PswBooksManageVer = manageTemp.copy()
            del manageTemp
        else:
            self.filemodel.setPswBooksManage(self.PswBooksManageVer)
            self.func.setPswBooksList()
            self.PswBooksManageVer = self.filemodel.getPswBooksManage()
            QtWidgets.QMessageBox.information(self, u'提示',u'批量删除单词本成功')
        pass

    def SelectAllPasswordBooks(self):
        self.func.setSelectAllOrUnselectAll(self.PswBooksList,1)
        pass

    def ClearAllSelectedPasswordBooks(self):
        self.func.setSelectAllOrUnselectAll(self.PswBooksList, 0)
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

    # # 为PswBooksList添加单击，双击事件
    def PswBooksListClick(self):
        item = self.PswBooksList.currentItem()
        if item is not None:
            item.setCheckState(QtCore.Qt.Checked if item.checkState() == QtCore.Qt.Unchecked else QtCore.Qt.Unchecked)
        pass
    def PswBooksListDouClick(self):
        item = self.PswBooksList.currentItem()
        # 防止双击更改item的状态
        if item is not None:
            state = item.checkState()
            item.setCheckState(QtCore.Qt.Unchecked if state == QtCore.Qt.Checked else QtCore.Qt.Checked)
            self.OpenPswBooksListItem()
        pass
    # # 为PswBooksList右键菜单绑定动作
    def PswBooksListContext(self, point):
        listItemMenu = QtWidgets.QMenu()
        if QtWidgets.QListWidget.itemAt(self.PswBooksList, point) != None:
            openAction = QtWidgets.QAction(u'打开', self.PswBooksList)
            openAction.triggered.connect(self.OpenPswBooksListItem)
            listItemMenu.addAction(openAction)
            editAction = QtWidgets.QAction(u'修改', self.PswBooksList)
            editAction.triggered.connect(self.EditPswBooksListItem)
            listItemMenu.addAction(editAction)
            deleteAction = QtWidgets.QAction(u'删除', self.PswBooksList)
            deleteAction.triggered.connect(self.DeletePswBooksListItem)
            listItemMenu.addAction(deleteAction)
        listItemMenu.exec_(QtGui.QCursor.pos())
        pass

    def OpenPswBooksListItem(self):
        item = self.PswBooksList.currentItem()
        dialog = QtWidgets.QInputDialog()
        pswBooksName = item.text()
        text, ok = dialog.getText(self, u'输入密码', u'请输入' + pswBooksName + u'的密码', QtWidgets.QLineEdit.Password)
        if ok:
            if funclibs.getMD5(text) != self.PswBooksManageVer[pswBooksName][0]:
                QtWidgets.QMessageBox.information(self, u'错误', u'输入' + pswBooksName + u'的密码错误')
            else:
                QtWidgets.QMessageBox.information(self, u'正确', u'输入' + pswBooksName + u'的密码正确')
        pass

    def EditPswBooksListItem(self):
        QtWidgets.QMessageBox.information(self, 'Edit', 'editBooks')
        pass

    def DeletePswBooksListItem(self):
        item = self.PswBooksList.currentItem()
        booksName = item.text()
        if self.PswBooksManageVer.pop(booksName) is not None:
            QtWidgets.QMessageBox.information(self, u'提示', booksName + u' 删除成功')
            self.filemodel.setPswBooksManage(self.PswBooksManageVer)
            self.func.setPswBooksList()
            self.PswBooksManageVer = self.filemodel.getPswBooksManage()
        pass
    # # 为PswList添加单机双击事件

    # # 为PswList添加右键菜单