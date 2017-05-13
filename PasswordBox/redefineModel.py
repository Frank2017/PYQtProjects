# coding=UTF-8
from PyQt5 import QtGui, QtCore, QtWidgets

class AddDialog(QtWidgets.QDialog):
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
        grid.addWidget(QtWidgets.QLabel(u'', parent=self), 3, 0, 1, 3)
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
            super(AddDialog, self).accept()
        pass

    def reject(self):
        super(AddDialog, self).reject()
        pass

    def getData(self):
        return [self.lePswName.text(), self.lePsw.text()]
        pass