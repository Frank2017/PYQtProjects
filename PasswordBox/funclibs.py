# coding=UTF-8
import hashlib
from PyQt5 import QtCore, QtWidgets,QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow


def getMD5(str):
    """
    返回str的MD5加密结果
    :param str: 待加密字符串
    :return: 加密后字符串
    """
    m = hashlib.md5()
    m.update(str)
    return m.hexdigest()
    pass

class FuncLibs:
    def __init__(self, controller):
        self.controller = controller

    def setPswBooksList(self):
        self.controller.PswBooksList.clear()
        dict = self.controller.filemodel.getPswBooksManage()
        pswbooksList = dict.keys()
        index = 0
        for it in pswbooksList:
            item = QtWidgets.QListWidgetItem(self.controller.tr(it))
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            item.setCheckState(QtCore.Qt.Unchecked)
            self.controller.PswBooksList.insertItem(index, item)
            index += 1
        pass

    def setSelectAllOrUnselectAll(self, objList, flag):
        if objList is not None:
            itemLen = objList.count()
            for i in range(itemLen):
                item = objList.item(i)
                if flag == 0:
                    item.setCheckState(QtCore.Qt.Unchecked)
                else:
                    item.setCheckState(QtCore.Qt.Checked)
        pass

    def getCheckedItems(self,objList):
        if objList is not None:
            listLen = objList.count()
            delList = []
            for i in range(listLen):
                item = objList.item(i)
                if item.checkState() == QtCore.Qt.Checked:
                    delList.append(item.text())
            return delList
        pass
