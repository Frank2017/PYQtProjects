# coding=UTF-8
import sys
from PyQt5 import QtCore, QtWidgets,QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_MainWindow import Ui_MainWindow
import filemodel as FM
import funclibs
from redefineModel import *

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
        self.DeletePswBtn.clicked.connect(self.DeleteSelectedPassword)

        # # 为menu绑定动作
        self.ImportExcelAction.triggered.connect(self.ImportExcelMenuFunc)

        # # 为PswBooksList添加单击，双击事件
        self.PswBooksList.clicked.connect(self.PswBooksListClick)
        self.PswBooksList.doubleClicked.connect(self.PswBooksListDouClick)
        # # 为PswBooksList右键菜单绑定动作
        self.PswBooksList.customContextMenuRequested[QtCore.QPoint].connect(self.PswBooksListContext)
        # # 为PswList添加单机双击事件
        self.PswList.clicked.connect(self.PswListClick)
        self.PswList.doubleClicked.connect(self.PswListDouClick)
        # # 为PswList添加右键菜单
        self.PswList.customContextMenuRequested[QtCore.QPoint].connect(self.PswListContext)

        # 初始化filemodel进行存储
        self.filemodel = FM.FileModel()
        if self.filemodel.initModel() == 0:
            QtWidgets.QMessageBox.information(u'错误', u'初始化失败')
            sys.exit(0)
        self.PswBooksManageVer = self.filemodel.getPswBooksManage()
        self.PasswordDictVer = {}
        self.CurOpenPswBookName = ''
        self.CurOpenPswBookNameMD5 = ''

        # 初始化将一些按钮点击功能禁止
        if self.CurOpenPswBookName == '':
            # self.PswSelectAllBtn.setEnabled(False)
            # self.PswClearAllBtn.setEnabled(False)
            self.PswBooksCloseBtn.setEnabled(False)
            self.AddPswBtn.setEnabled(False)
            # self.DeletePswBtn.setEnabled(False)
        # if len(self.PswBooksManageVer) == 0:
        #     self.DeletePswBooksBtn.setEnabled(False)
        #     self.ExportExcelBtn.setEnabled(False)
        #     self.PswBooksSelectAllBtn.setEnabled(False)
        #     self.PswBooksClearBtn.setEnabled(False)


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
        dialog = AddBookDialog('添加密码本',self.PswBooksManageVer)
        # 如果是正常结束，ok返回1，cancel返回o,关闭返回0
        # print dialog.exec_()
        if dialog.exec_():
            temp = dialog.getData()
            # 密码本管理文件的存储格式为dict， 密码本名：[MD5（password）, MD5(密码本名，用于在PswBooksDb
            # 中命名密码本存储名)]
            # print temp
            self.PswBooksManageVer[temp[0]] = [funclibs.getMD5(temp[1]), funclibs.getMD5(temp[0])]
            # 建立对应的PswFile
            self.filemodel.setPswBooks({}, funclibs.getMD5(temp[0]))
            # 说明文件没有创建成功
            if self.filemodel.getPswBook(funclibs.getMD5(temp[0])) is None:
                QtWidgets.QMessageBox.information(self, u'错误', u'添加密码本错误')
                # 从Manage 管理变量中讲新添加的删除
                self.PswBooksManageVer.pop(temp[0])
            else:
                QtWidgets.QMessageBox.information(self, u'提示', u'添加密码本成功')
            # 将内容存入文件
            self.filemodel.setPswBooksManage(self.PswBooksManageVer)
            # 设置PswBooksList
            self.func.setPswBooksList()
            # 获取最新的PswBooksManageVer
            self.PswBooksManageVer = self.filemodel.getPswBooksManage()
        pass
        dialog.destroy()

    def DeletePasswordBooks(self):
        delList = self.func.getCheckedItems(self.PswBooksList)
        # 记录待删除的文件个数
        delLen = len(delList)
        # 记录PswBooksManage的备份
        manageTemp = self.PswBooksManageVer.copy()
        # 标记位 ，flag=0表示删除成功，flag=1表示删除失败
        flag = 0
        # backupList 从dict中删除成功但是，删除文件时出错
        backupList = []
        for dit in delList:
            # 若有的单词本没有被删除，修改标记为1,不存在dict未删除且文件未删除的情况
            if self.PswBooksManageVer.pop(dit) is None:
                flag = 1
                backupList.append(dit)
            else:
                # 删除文件出错
                state = self.filemodel.removePswFile(funclibs.getMD5(dit))
                if state == 0:
                    flag = 1
                    backupList.append(dit)
        # 记录未删除的文件个数
        backupLen = len(backupList)
        # 说明有的单词本未被删除，需要回滚
        if flag == 1 and backupLen != 0:
            for bk in backupList:
                val = manageTemp[bk]
                self.PswBooksManageVer[bk] = val
        # 将当前的PSWBOOKSMANAGE状态进行写入文件
        self.filemodel.setPswBooksManage(self.PswBooksManageVer)
        self.func.setPswBooksList()
        self.PswBooksManageVer = self.filemodel.getPswBooksManage()
        QtWidgets.QMessageBox.information(self, u'提示',u'批量删除'+str(delLen - backupLen)+u'个密码本成功')
        pass

    def SelectAllPasswordBooks(self):
        if self.PswBooksList.count() > 0:
            self.func.setSelectAllOrUnselectAll(self.PswBooksList,1)
        pass

    def ClearAllSelectedPasswordBooks(self):
        if self.PswBooksList.count() > 0:
            self.func.setSelectAllOrUnselectAll(self.PswBooksList, 0)
        pass

    def ExportExcel(self):
        pass

    # 为搜索定义Button函数
    def SearchPsw(self):
        searchKey = self.SearchInput.text()
        if self.PswBooksList.count() > 0:
            booksLen = self.PswBooksList.count()
            for i in range(booksLen):
                item = self.PswBooksList.item(i)
                booksName = item.text()
                if booksName.find(searchKey):
                    item.setSelected(True)
        if self.CurOpenPswBookName != '' and self.PswList.count() > 0:
            pswLen = self.PswList.count()
            for i in range(pswLen):
                item = self.PswList.item(i)
                pswName = item.text()
                # print pswName
                if pswName.find(searchKey):
                    item.setSelected(True)
        pass

    def SearchInputClear(self):
        self.SearchInput.setText('')
        if self.PswBooksList.count() > 0:
            booksLen = self.PswBooksList.count()
            for i in range(booksLen):
                item = self.PswBooksList.item(i)
                if item.isSelected():
                    item.setSelected(False)
        if self.CurOpenPswBookName != '' and self.PswList.count() > 0:
            pswLen = self.PswList.count()
            for i in range(pswLen):
                item = self.PswList.item(i)
                if item.isSelected():
                    item.setSelected(False)
        pass


    # 为password定义函数
    def SelectAllPassword(self):
        if self.PswList.count() > 0:
            self.func.setSelectAllOrUnselectAll(self.PswList, 1)
        pass

    def ClearAllSelectedPassword(self):
        if self.PswList.count() > 0:
            self.func.setSelectAllOrUnselectAll(self.PswList, 0)
        pass

    def CloseCurPasswordBooks(self):
        # 关闭前将最新数据写入文件
        if self.CurOpenPswBookNameMD5 != '':
            self.filemodel.setPswBooks(self.PasswordDictVer, self.CurOpenPswBookNameMD5)
        self.PasswordDictVer = {}
        self.CurOpenPswBookName = ''
        self.CurOpenPswBookNameMD5 = ''
        self.PswList.clear()
        self.PswBooksCloseBtn.setEnabled(False)
        self.AddPswBtn.setEnabled(False)
        QtWidgets.QMessageBox.information(self,u'提示', u'密码本关闭成功')
        pass

    def AddPassword(self):
        dialog = AddPasswordDialog(u'添加新密码项', self.PasswordDictVer)
        if dialog.exec_():
            addData =  dialog.getData()
            self.PasswordDictVer[(addData[0], addData[1])] = addData[2]
            if self.CurOpenPswBookNameMD5 != '':
                self.filemodel.setPswBooks(self.PasswordDictVer, self.CurOpenPswBookNameMD5)
            self.PasswordDictVer = self.filemodel.getPswBook(self.CurOpenPswBookNameMD5)
            self.func.setPswListByData(self.PasswordDictVer)
            pass
        dialog.destroy()
        pass

    def DeleteSelectedPassword(self):
        selectedList = self.func.getCheckedItems(self.PswList)
        keyList = funclibs.transToDictKey(selectedList)
        self.__deletePassword(keyList)
        pass

    def __deletePassword(self,keyList):
        if keyList is None:
            QtWidgets.QMessageBox.information(self,u'错误',u'没有待删除的密码项')
        else:
            cnt = 0
            for k in keyList:
                if len(k) == 2:
                    if self.PasswordDictVer.has_key((k[0],k[1])):
                        self.PasswordDictVer.pop((k[0],k[1]))
                        cnt += 1
            self.filemodel.setPswBooks(self.PasswordDictVer,self.CurOpenPswBookNameMD5)
            self.PasswordDictVer = self.filemodel.getPswBook(self.CurOpenPswBookNameMD5)
            self.func.setPswListByData(self.PasswordDictVer)
            QtWidgets.QMessageBox.information(self,u'提示',u'成功删除' + str(cnt) + u'个密码项')
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
            editNameAction = QtWidgets.QAction(u'修改名称', self.PswBooksList)
            editNameAction.triggered.connect(self.EditPswBooksListItemName)
            listItemMenu.addAction(editNameAction)
            editPswAction = QtWidgets.QAction(u'修改密码', self.PswBooksList)
            editPswAction.triggered.connect(self.EditPswBooksListItemPsw)
            listItemMenu.addAction(editPswAction)
            deleteAction = QtWidgets.QAction(u'删除', self.PswBooksList)
            deleteAction.triggered.connect(self.DeletePswBooksListItem)
            listItemMenu.addAction(deleteAction)
        listItemMenu.exec_(QtGui.QCursor.pos())
        pass

    def OpenPswBooksListItem(self):
        item = self.PswBooksList.currentItem()
        pswBooksName = item.text()
        if self.filemodel.pswFileExist(funclibs.getMD5(pswBooksName)):
            dialog = QtWidgets.QInputDialog()
            text, ok = dialog.getText(self, u'输入密码', u'请输入(' + pswBooksName + u')的开启密码', QtWidgets.QLineEdit.Password)
            if ok:
                if funclibs.getMD5(text) != self.PswBooksManageVer[pswBooksName][0]:
                    QtWidgets.QMessageBox.information(self, u'错误', u'输入(' + pswBooksName + u')的密码错误')
                else:
                    pswData = self.filemodel.getPswBook(funclibs.getMD5(pswBooksName))
                    if pswData is not None:
                        # QtWidgets.QMessageBox.information(self, u'正确', u'输入(' + pswBooksName + u')的密码正确')
                        self.PasswordDictVer = self.filemodel.getPswBook(funclibs.getMD5(pswBooksName))
                        self.CurOpenPswBookName = pswBooksName
                        self.CurOpenPswBookNameMD5 = funclibs.getMD5(pswBooksName)
                        if self.PasswordDictVer is not None:
                            self.PswBooksCloseBtn.setEnabled(True)
                            self.AddPswBtn.setEnabled(True)
                            self.func.setPswListByData(self.PasswordDictVer)
                            # QtWidgets.QMessageBox.information(self, u'打开', u'打开密码本(' + pswBooksName + u')成功')
                        else:
                            self.PasswordDictVer = {}
                            QtWidgets.QMessageBox.information(self, u'错误', u'打开密码本(' + pswBooksName + u')错误')
                    else:
                        QtWidgets.QMessageBox.information(self, u'错误', u'密码本(' + pswBooksName + u')的密码文件不存在')
        else:
            QtWidgets.QMessageBox.information(self, u'错误', u'密码本(' + pswBooksName + u')的密码文件不存在')
        pass

    def EditPswBooksListItemName(self):
        item = self.PswBooksList.currentItem()
        dialog = QtWidgets.QInputDialog()
        pswBooksNameOld = item.text()
        pswBooksNameNew, ok = dialog.getText(self, u'修改密码本名称', u'请输入密码本（' + pswBooksNameOld + u'）的新名称')
        if ok:
            if self.PswBooksManageVer.has_key(pswBooksNameNew):
                QtWidgets.QMessageBox.information(self, u'错误', u'该密码本('+pswBooksNameNew+u')已存在，请重新命名')
            else:
                pswBooksNameOldMD5 = funclibs.getMD5(pswBooksNameOld)
                pswBooksNameNewMD5 = funclibs.getMD5(pswBooksNameNew)
                state = self.filemodel.renamePswFile(pswBooksNameOldMD5,pswBooksNameNewMD5)
                manageTemp = self.PswBooksManageVer.copy()
                if state == -2:
                    QtWidgets.QMessageBox.information(self, u'错误',u'该密码本('+pswBooksNameNew+u')已存在，请重新命名')
                elif state == -1:
                    QtWidgets.QMessageBox.information(self, u'错误', u'原始密码本(' + pswBooksNameOld + u')文件不存在。\n请删除后重新添加该密码本！')
                elif state == 0:
                    QtWidgets.QMessageBox.information(self, u'错误', u'重命名密码本失败')
                elif state == 1:
                    # 获取原来的名字对应值
                    newVal = self.PswBooksManageVer[pswBooksNameOld]
                    # 将新的密码本名的MD5值进行更改
                    newVal[1] = pswBooksNameNewMD5
                    # 将新修改的值加入manage中
                    self.PswBooksManageVer[pswBooksNameNew] =newVal
                    # 删除掉原来的名字对应的信息
                    self.PswBooksManageVer.pop(pswBooksNameOld)

                    self.filemodel.setPswBooksManage(self.PswBooksManageVer)
                    self.func.setPswBooksList()
                    self.PswBooksManageVer = self.filemodel.getPswBooksManage()
                    QtWidgets.QMessageBox.information(self, u'提示', u'密码本重命名成功')
        pass

    def EditPswBooksListItemPsw(self):
        item = self.PswBooksList.currentItem()
        bkName = item.text()
        dialog = EditBookPswDialog(u'修改开启密码',self.PswBooksManageVer, bkName)
        if dialog.exec_():
            pswNew = dialog.getData()
            self.PswBooksManageVer[bkName][0] = funclibs.getMD5(pswNew)
            self.filemodel.setPswBooksManage(self.PswBooksManageVer)
            self.PswBooksManageVer = self.filemodel.getPswBooksManage()
            self.func.setPswBooksList()
            QtWidgets.QMessageBox.information(self, u'提示',u'修改(' + bkName + u')的开启密码成功')
        dialog.destroy()
        pass

    def DeletePswBooksListItem(self):
        item = self.PswBooksList.currentItem()
        booksName = item.text()
        bookmanageTemp = self.PswBooksManageVer.copy()
        state = self.filemodel.removePswFile(funclibs.getMD5(booksName))
        if self.PswBooksManageVer.pop(booksName) is not None and state != 0:
            QtWidgets.QMessageBox.information(self, u'提示', booksName + u' 删除成功')
            self.filemodel.setPswBooksManage(self.PswBooksManageVer)
            self.func.setPswBooksList()
            self.PswBooksManageVer = self.filemodel.getPswBooksManage()
        else:
            QtWidgets.QMessageBox.information(self, u'提示', booksName + u' 删除失败')
            self.filemodel.setPswBooksManage(bookmanageTemp)
            self.func.setPswBooksList()
            self.PswBooksManageVer = bookmanageTemp.copy()
        pass
    # # 为PswList添加单击双击事件
    def PswListClick(self):
        item = self.PswList.currentItem()
        if item is not None:
            item.setCheckState(QtCore.Qt.Checked if item.checkState() == QtCore.Qt.Unchecked else QtCore.Qt.Unchecked)
        pass

    def PswListDouClick(self):
        item = self.PswList.currentItem()
        # 防止双击更改item的状态
        if item is not None:
            state = item.checkState()
            item.setCheckState(QtCore.Qt.Unchecked if state == QtCore.Qt.Checked else QtCore.Qt.Checked)
            self.OpenPswListItem()
        pass
    # # 为PswList添加右键菜单
    def PswListContext(self,point):
        listItemMenu = QtWidgets.QMenu()
        if QtWidgets.QListWidget.itemAt(self.PswList, point) != None:
            openAction = QtWidgets.QAction(u'打开', self.PswList)
            openAction.triggered.connect(self.OpenPswListItem)
            listItemMenu.addAction(openAction)
            editAction = QtWidgets.QAction(u'修改', self.PswList)
            editAction.triggered.connect(self.EditPswListItem)
            listItemMenu.addAction(editAction)
            deleteAction = QtWidgets.QAction(u'删除', self.PswList)
            deleteAction.triggered.connect(self.DeletePswListItem)
            listItemMenu.addAction(deleteAction)
        listItemMenu.exec_(QtGui.QCursor.pos())
        pass

    def OpenPswListItem(self):
        item = self.PswList.currentItem()
        key = funclibs.transStrToDictKey(item.text())
        if key is not None:
            initdata = key
            if self.PasswordDictVer.has_key((key[0], key[1])):
                initdata.append(self.PasswordDictVer[(key[0], key[1])])
                print initdata
                dialog = OpenPasswordDialog(u'打开密码项', initdata)
                if dialog.exec_():
                    pass
                dialog.destroy()
            else:
                QtWidgets.QMessageBox.information(self, u'错误', '(' + key[0] + ',' + key[1] + ')' + u'该密码项不存在')
        else:
            QtWidgets.QMessageBox.information(self, u'错误', u'键值转码失败')
        pass

    def EditPswListItem(self):
        item = self.PswList.currentItem()
        key = funclibs.transStrToDictKey(item.text())
        if key is not None:
            initdata = key
            if self.PasswordDictVer.has_key((key[0], key[1])):
                initdata.append(self.PasswordDictVer[(key[0],key[1])])
                # print initdata
                dialog = EditPasswordDialog(u'修改密码项',self.PasswordDictVer, initdata)
                if dialog.exec_():
                    editData = dialog.getData()
                    # 修改原则：既然点击了修改，原来的数据都要删除，然后插入新的数据
                    self.PasswordDictVer.pop((key[0], key[1]))
                    self.PasswordDictVer[(editData[0], editData[1])] = editData[2]
                    if self.CurOpenPswBookNameMD5 != '':
                        self.filemodel.setPswBooks(self.PasswordDictVer, self.CurOpenPswBookNameMD5)
                    self.PasswordDictVer = self.filemodel.getPswBook(self.CurOpenPswBookNameMD5)
                    self.func.setPswListByData(self.PasswordDictVer)
                    pass
                dialog.destroy()
            else:
                QtWidgets.QMessageBox.information(self, u'错误', '('+ key[0] + ',' + key[1] +')'+u'该密码项不存在')
        else:
            QtWidgets.QMessageBox.information(self, u'错误', u'键值转码失败')
        pass

    def DeletePswListItem(self):
        item = self.PswList.currentItem()
        itemName = item.text()
        key = funclibs.transToDictKey(itemName)
        self.__deletePassword(key)
        pass