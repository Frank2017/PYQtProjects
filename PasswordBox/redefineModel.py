# coding=UTF-8
from PyQt5 import QtGui, QtCore, QtWidgets
import funclibs

class AddBookDialog(QtWidgets.QDialog):
    def __init__(self, title, data, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setWindowTitle(title)
        self.setFixedSize(350, 200)
        self.pswBookdata = data
        # 表格布局，用来布局QLabel和QLineEdit及QSpinBox
        grid = QtWidgets.QGridLayout()
        # 后面四个数的意义（行，列，行跨度，列跨度）
        grid.addWidget(QtWidgets.QLabel(u'密码本名：', parent=self), 0, 0, 1, 1)
        self.lePswName = QtWidgets.QLineEdit(parent=self)
        grid.addWidget(self.lePswName, 0, 1, 1, 2)
        grid.addWidget(QtWidgets.QLabel(u'开启密码：', parent=self), 1, 0, 1, 1)
        self.lePsw = QtWidgets.QLineEdit(self)
        self.lePsw.setEchoMode(QtWidgets.QLineEdit.Password)
        grid.addWidget(self.lePsw, 1, 1, 1, 2)
        grid.addWidget(QtWidgets.QLabel(u'再次输入密码：', parent=self), 2, 0, 1, 1)
        self.leRePsw = QtWidgets.QLineEdit(self)
        self.leRePsw.setEchoMode(QtWidgets.QLineEdit.Password)
        grid.addWidget(self.leRePsw, 2, 1, 1, 2)
        # 创建ButtonBox，用户确定和取消
        buttonBox = QtWidgets.QDialogButtonBox(parent=self)
        buttonBox.setOrientation(QtCore.Qt.Horizontal)  # 设置为水平方向
        buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)  # 确定和取消两个按钮
        # 连接信号和槽
        buttonBox.accepted.connect(self.accept)  # 确定
        buttonBox.rejected.connect(self.reject)  # 取消
        # 垂直布局，布局表格及按钮
        layout = QtWidgets.QVBoxLayout()
        # 加入前面创建的表格布局
        layout.addLayout(grid)
        # 放一个间隔对象美化布局
        spacerItem = QtWidgets.QSpacerItem(20, 48, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        layout.addItem(spacerItem)
        # ButtonBox
        layout.addWidget(buttonBox)
        self.setLayout(layout)
        pass

    def accept(self):
        pswbname = self.lePswName.text()
        pswVal = self.lePsw.text()
        rePswVal = self.leRePsw.text()
        if pswbname == '':
            QtWidgets.QMessageBox.information(self, '错误！', u'请输入密码本名称')
            self.lePswName.setFocus()
        elif self.pswBookdata.has_key(pswbname) and pswbname != '':
            QtWidgets.QMessageBox.information(self, '错误！', u'该密码本已存在')
            self.lePswName.setFocus()
            self.lePswName.setText('')
        elif pswVal == '' or rePswVal == '':
            QtWidgets.QMessageBox.information(self, '错误！', u'请输入密码')
            self.lePsw.setFocus()
            self.lePsw.setText('')
            self.leRePsw.setText('')
        elif rePswVal != pswVal:
            QtWidgets.QMessageBox.information(self, '错误！', u'两次输入密码不一致')
            self.lePsw.setFocus()
            self.lePsw.setText('')
            self.leRePsw.setText('')
        else:
            super(AddBookDialog, self).accept()
        pass

    def reject(self):
        super(AddBookDialog, self).reject()
        pass

    def getData(self):
        return [self.lePswName.text(), self.lePsw.text()]
        pass


class EditBookPswDialog(QtWidgets.QDialog):
    def __init__(self, title, data, bkname, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setWindowTitle(title + '(' + bkname + ')')
        self.setFixedSize(350, 200)
        self.pswBookdata = data
        self.bookName = bkname
        # 表格布局，用来布局QLabel和QLineEdit及QSpinBox
        grid = QtWidgets.QGridLayout()
        # 后面四个数的意义（行，列，行跨度，列跨度）
        grid.addWidget(QtWidgets.QLabel(u'输入原始密码：', parent=self), 0, 0, 1, 1)
        self.lePswOld = QtWidgets.QLineEdit(parent=self)
        self.lePswOld.setEchoMode(QtWidgets.QLineEdit.Password)
        grid.addWidget(self.lePswOld, 0, 1, 1, 2)
        grid.addWidget(QtWidgets.QLabel(u'输入新密码：', parent=self), 1, 0, 1, 1)
        self.lePswNew = QtWidgets.QLineEdit(self)
        self.lePswNew.setEchoMode(QtWidgets.QLineEdit.Password)
        grid.addWidget(self.lePswNew, 1, 1, 1, 2)
        grid.addWidget(QtWidgets.QLabel(u'再次输入新密码：', parent=self), 2, 0, 1, 1)
        self.leRePswNew = QtWidgets.QLineEdit(self)
        self.leRePswNew.setEchoMode(QtWidgets.QLineEdit.Password)
        grid.addWidget(self.leRePswNew, 2, 1, 1, 2)
        # 创建ButtonBox，用户确定和取消
        buttonBox = QtWidgets.QDialogButtonBox(parent=self)
        buttonBox.setOrientation(QtCore.Qt.Horizontal)  # 设置为水平方向
        buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)  # 确定和取消两个按钮
        # 连接信号和槽
        buttonBox.accepted.connect(self.accept)  # 确定
        buttonBox.rejected.connect(self.reject)  # 取消
        # 垂直布局，布局表格及按钮
        layout = QtWidgets.QVBoxLayout()
        # 加入前面创建的表格布局
        layout.addLayout(grid)
        # 放一个间隔对象美化布局
        spacerItem = QtWidgets.QSpacerItem(20, 48, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        layout.addItem(spacerItem)
        # ButtonBox
        layout.addWidget(buttonBox)
        self.setLayout(layout)
        pass

    def accept(self):
        pswOldVal = self.lePswOld.text()
        pswNewVal = self.lePswNew.text()
        rePswNewVal = self.leRePswNew.text()
        if self.pswBookdata.has_key(self.bookName):
            # 获得原始密码校验值
            checkPsw = self.pswBookdata[self.bookName][0]
        else:
            checkPsw = ''
        # 获得输入原始密码的校验值
        pswOldValMd5 = funclibs.getMD5(pswOldVal)
        if pswOldVal == '':
            QtWidgets.QMessageBox.information(self, u'错误', u'请输入原始密码')
            self.lePswOld.setText('')
            self.lePswOld.setFocus()
        elif pswNewVal == '':
            QtWidgets.QMessageBox.information(self, u'错误', u'请输入新密码')
            self.lePswNew.setText('')
            self.leRePswNew.setText('')
            self.lePswNew.setFocus()
        elif checkPsw != pswOldValMd5:
            QtWidgets.QMessageBox.information(self, u'错误', u'请输入正确的原始密码')
            self.lePswOld.setText('')
            self.lePswOld.setFocus()
        elif pswNewVal != rePswNewVal:
            QtWidgets.QMessageBox.information(self, u'错误', u'输入两次新密码不一致')
            self.lePswNew.setText('')
            self.leRePswNew.setText('')
            self.lePswNew.setFocus()
        else:
            super(EditBookPswDialog, self).accept()
        pass

    def reject(self):
        super(EditBookPswDialog, self).reject()
        pass

    def getData(self):
        return self.lePswNew.text()
        pass


class AddPasswordDialog(QtWidgets.QDialog):
    def __init__(self, title, data, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setWindowTitle(title)
        self.setFixedSize(350, 200)
        self.passwordDict = data
        # 表格布局，用来布局QLabel和QLineEdit及QSpinBox
        grid = QtWidgets.QGridLayout()
        # 后面四个数的意义（行，列，行跨度，列跨度）
        grid.addWidget(QtWidgets.QLabel(u'应用名称：', parent=self), 0, 0, 1, 1)
        self.leAppName = QtWidgets.QLineEdit(parent=self)
        grid.addWidget(self.leAppName, 0, 1, 1, 2)
        grid.addWidget(QtWidgets.QLabel(u'用户名：', parent=self), 1, 0, 1, 1)
        self.leUserName = QtWidgets.QLineEdit(self)
        grid.addWidget(self.leUserName, 1, 1, 1, 2)
        grid.addWidget(QtWidgets.QLabel(u'登录密码：', parent=self), 2, 0, 1, 1)
        self.lePassword = QtWidgets.QLineEdit(self)
        self.lePassword.setEchoMode(QtWidgets.QLineEdit.Password)
        grid.addWidget(self.lePassword, 2, 1, 1, 2)
        # 创建ButtonBox，用户确定和取消
        buttonBox = QtWidgets.QDialogButtonBox(parent=self)
        buttonBox.setOrientation(QtCore.Qt.Horizontal)  # 设置为水平方向
        buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)  # 确定和取消两个按钮
        # 连接信号和槽
        buttonBox.accepted.connect(self.accept)  # 确定
        buttonBox.rejected.connect(self.reject)  # 取消
        # 垂直布局，布局表格及按钮
        layout = QtWidgets.QVBoxLayout()
        # 加入前面创建的表格布局
        layout.addLayout(grid)
        # 放一个间隔对象美化布局
        spacerItem = QtWidgets.QSpacerItem(20, 48, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        layout.addItem(spacerItem)
        # ButtonBox
        layout.addWidget(buttonBox)
        self.setLayout(layout)
        pass

    def accept(self):
        appName = self.leAppName.text()
        userName = self.leUserName.text()
        userPswd = self.lePassword.text()
        if appName == '':
            QtWidgets.QMessageBox.information(self, '错误！', u'请输入应用名称')
            self.leAppName.setFocus()
        elif userName == '':
            QtWidgets.QMessageBox.information(self, '错误！', u'请输入用户名')
            self.leUserName.setFocus()
        elif userPswd == '':
            QtWidgets.QMessageBox.information(self, '错误！', u'请输入密码')
            self.lePassword.setFocus()
        elif self.passwordDict.has_key((appName, userName)):
            QtWidgets.QMessageBox.information(self, '错误！', u'('+ appName + u',' + userName +u')对应的密码项已存在')
        else:
            super(AddPasswordDialog, self).accept()
        pass

    def reject(self):
        super(AddPasswordDialog, self).reject()
        pass

    def getData(self):
        return [self.leAppName.text(), self.leUserName.text(), self.lePassword.text()]
        pass

class OpenPasswordDialog(AddPasswordDialog):
    def __init__(self, title, initData):
        super(OpenPasswordDialog, self).__init__(title,None)
        self.leAppName.setText(initData[0])
        self.leUserName.setText(initData[1])
        self.lePassword.setText(initData[2])
        self.leAppName.setEnabled(False)
        self.leUserName.setEnabled(False)
        self.lePassword.setEnabled(False)
        self.lePassword.setEchoMode(QtWidgets.QLineEdit.Normal)
        pass
    def accept(self):
        QtWidgets.QDialog.accept(self)
        pass

    def reject(self):
        QtWidgets.QDialog.reject(self)
        pass


class EditPasswordDialog(AddPasswordDialog):
    def __init__(self, title, data, initData):
        super(EditPasswordDialog, self).__init__(title,data)
        self.leAppName.setText(initData[0])
        self.leUserName.setText(initData[1])
        self.lePassword.setText(initData[2])
        self.lePassword.setEchoMode(QtWidgets.QLineEdit.Normal)
        pass
    def accept(self):
        appName = self.leAppName.text()
        userName = self.leUserName.text()
        userPswd = self.lePassword.text()
        if appName == '':
            QtWidgets.QMessageBox.information(self, '错误！', u'请输入应用名称')
            self.leAppName.setFocus()
        elif userName == '':
            QtWidgets.QMessageBox.information(self, '错误！', u'请输入用户名')
            self.leUserName.setFocus()
        elif userPswd == '':
            QtWidgets.QMessageBox.information(self, '错误！', u'请输入密码')
            self.lePassword.setFocus()
        else:
            QtWidgets.QDialog.accept(self)
        pass

    def reject(self):
        super(EditPasswordDialog, self).reject()
        pass

    def getData(self):
        return super(EditPasswordDialog, self).getData()
        pass
