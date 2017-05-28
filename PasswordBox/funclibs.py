# coding=UTF-8
import hashlib
from PyQt5 import QtCore, QtWidgets,QtGui
from Crypto.Cipher import AES
from binascii import b2a_hex,a2b_hex
from PyQt5.QtWidgets import QApplication, QMainWindow


def getMD5(str):
    """
    返回str的MD5加密结果
    :param str: 待加密字符串
    :return: 加密后字符串
    """
    m = hashlib.md5()
    m.update(str.encode("UTF-8"))
    return m.hexdigest()
    pass

def pswCipher(text,key):
    iv = (key.__str__())[0:16]
    text = text.encode("UTF-8")
    paddinglen = 16 - len(text) % 16
    text += '\0' * paddinglen
    cipher = AES.new(key,AES.MODE_CBC,iv)
    msg = b2a_hex(cipher.encrypt(text))
    return msg
    pass

def pswDecipher(ciphertext,key):
    iv = (key.__str__())[0:16]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    msg = cipher.decrypt(a2b_hex(ciphertext))
    msg = msg.replace('\0','')
    return msg
    pass

def pswDictCipher(dict,key):
    if len(dict) > 0:
        for k in dict.keys():
            dict[k] = pswCipher(dict[k], key)
        return dict
    return {}

def transToDictKey(data):
    if isinstance(data, list):
        keyList = []
        for dstr in data:
            result = transStrToDictKey(dstr)
            if result is not None:
                keyList.append(result)
        return keyList
    else:
        return [transStrToDictKey(data)]

    return None
    pass

def transStrToDictKey(str):
    result = str.split('<-*-*-*-*-*-*->')
    # 如果处理的结果不是两个返回None
    if len(result) < 2:
        return None
    return result
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

    def setPswListByData(self, data):
        self.controller.PswList.clear()
        keyList = data.keys()
        index = 0
        for it in keyList:
            textstr = it[0] + '<-*-*-*-*-*-*->' + it[1]
            item = QtWidgets.QListWidgetItem(self.controller.tr(textstr))
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            item.setCheckState(QtCore.Qt.Unchecked)
            self.controller.PswList.insertItem(index, item)
            index += 1
        pass

    def setPswListByFileName(self, fname):
        fnameMD5 = getMD5(fname)
        data = self.controller.filemodel.getPswBook(fnameMD5)
        if data is not None:
            self.setPswListByData(data)
        else:
            QtWidgets.QMessageBox.information(self,u'错误',u'打开密码本（'+fname+u')失败')
        pass
