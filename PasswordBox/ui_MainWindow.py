# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(847, 641)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 226, 581))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.AddPswBooksBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.AddPswBooksBtn.sizePolicy().hasHeightForWidth())
        self.AddPswBooksBtn.setSizePolicy(sizePolicy)
        self.AddPswBooksBtn.setAutoDefault(False)
        self.AddPswBooksBtn.setDefault(False)
        self.AddPswBooksBtn.setFlat(False)
        self.AddPswBooksBtn.setObjectName("AddPswBooksBtn")
        self.horizontalLayout.addWidget(self.AddPswBooksBtn)
        self.DeletePswBooksBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.DeletePswBooksBtn.sizePolicy().hasHeightForWidth())
        self.DeletePswBooksBtn.setSizePolicy(sizePolicy)
        self.DeletePswBooksBtn.setObjectName("DeletePswBooksBtn")
        self.horizontalLayout.addWidget(self.DeletePswBooksBtn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.ExportExcelBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.ExportExcelBtn.sizePolicy().hasHeightForWidth())
        self.ExportExcelBtn.setSizePolicy(sizePolicy)
        self.ExportExcelBtn.setObjectName("ExportExcelBtn")
        self.horizontalLayout_4.addWidget(self.ExportExcelBtn)
        spacerItem = QtWidgets.QSpacerItem(107, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.PswBooksList = QtWidgets.QListWidget(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PswBooksList.sizePolicy().hasHeightForWidth())
        self.PswBooksList.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("思源黑体")
        font.setBold(True)
        font.setWeight(75)
        self.PswBooksList.setFont(font)
        self.PswBooksList.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.PswBooksList.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.PswBooksList.setFrameShadow(QtWidgets.QFrame.Raised)
        self.PswBooksList.setLineWidth(3)
        self.PswBooksList.setMidLineWidth(1)
        self.PswBooksList.setObjectName("PswBooksList")
        self.verticalLayout.addWidget(self.PswBooksList)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.PswBooksSelectAllBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.PswBooksSelectAllBtn.setObjectName("PswBooksSelectAllBtn")
        self.horizontalLayout_5.addWidget(self.PswBooksSelectAllBtn)
        self.PswBooksClearBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.PswBooksClearBtn.setObjectName("PswBooksClearBtn")
        self.horizontalLayout_5.addWidget(self.PswBooksClearBtn)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(240, 10, 591, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.SearchInput = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.SearchInput.setObjectName("SearchInput")
        self.horizontalLayout_2.addWidget(self.SearchInput)
        self.SearchBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.SearchBtn.setStyleSheet("background-color: rgb(238, 238, 238);")
        self.SearchBtn.setObjectName("SearchBtn")
        self.horizontalLayout_2.addWidget(self.SearchBtn)
        self.SearchClearBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.SearchClearBtn.setStyleSheet("background-color: rgb(238, 238, 238);")
        self.SearchClearBtn.setObjectName("SearchClearBtn")
        self.horizontalLayout_2.addWidget(self.SearchClearBtn)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(240, 60, 591, 531))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.PswSelectAllBtn = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(80)
        sizePolicy.setVerticalStretch(25)
        sizePolicy.setHeightForWidth(self.PswSelectAllBtn.sizePolicy().hasHeightForWidth())
        self.PswSelectAllBtn.setSizePolicy(sizePolicy)
        self.PswSelectAllBtn.setObjectName("PswSelectAllBtn")
        self.horizontalLayout_3.addWidget(self.PswSelectAllBtn)
        self.PswClearAllBtn = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.PswClearAllBtn.setObjectName("PswClearAllBtn")
        self.horizontalLayout_3.addWidget(self.PswClearAllBtn)
        spacerItem1 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.PswBooksCloseBtn = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.PswBooksCloseBtn.setObjectName("PswBooksCloseBtn")
        self.horizontalLayout_3.addWidget(self.PswBooksCloseBtn)
        self.AddPswBtn = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.AddPswBtn.setObjectName("AddPswBtn")
        self.horizontalLayout_3.addWidget(self.AddPswBtn)
        self.DeletePswBtn = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.DeletePswBtn.setObjectName("DeletePswBtn")
        self.horizontalLayout_3.addWidget(self.DeletePswBtn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.PswList = QtWidgets.QTableWidget(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PswList.sizePolicy().hasHeightForWidth())
        self.PswList.setSizePolicy(sizePolicy)
        self.PswList.setMinimumSize(QtCore.QSize(100, 0))
        self.PswList.setBaseSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setKerning(True)
        self.PswList.setFont(font)
        self.PswList.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.PswList.setAutoFillBackground(True)
        self.PswList.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.PswList.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.PswList.setLineWidth(3)
        self.PswList.setMidLineWidth(3)
        self.PswList.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.PswList.setShowGrid(False)
        self.PswList.setCornerButtonEnabled(False)
        self.PswList.setObjectName("PswList")
        self.PswList.setColumnCount(3)
        self.PswList.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(79, 229, 224))
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.PswList.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(170, 251, 252))
        self.PswList.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("思源黑体")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(243, 244, 163))
        self.PswList.setHorizontalHeaderItem(2, item)
        self.PswList.horizontalHeader().setCascadingSectionResizes(False)
        self.PswList.horizontalHeader().setDefaultSectionSize(150)
        self.PswList.horizontalHeader().setSortIndicatorShown(False)
        self.PswList.horizontalHeader().setStretchLastSection(True)
        self.PswList.verticalHeader().setVisible(False)
        self.PswList.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_2.addWidget(self.PswList)
        self.verticalLayoutWidget.raise_()
        self.horizontalLayoutWidget_2.raise_()
        self.verticalLayoutWidget_2.raise_()
        self.PswList.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 847, 29))
        self.menuBar.setObjectName("menuBar")
        self.funcMenu = QtWidgets.QMenu(self.menuBar)
        self.funcMenu.setObjectName("funcMenu")
        MainWindow.setMenuBar(self.menuBar)
        self.ImportExcelAction = QtWidgets.QAction(MainWindow)
        self.ImportExcelAction.setObjectName("ImportExcelAction")
        self.funcMenu.addAction(self.ImportExcelAction)
        self.menuBar.addAction(self.funcMenu.menuAction())

        # self.retranslateUi(MainWindow)
        # QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.AddPswBooksBtn.setText(_translate("MainWindow", "添加密码本"))
        self.DeletePswBooksBtn.setText(_translate("MainWindow", "删除密码本"))
        self.ExportExcelBtn.setText(_translate("MainWindow", "导出密码本"))
        self.PswBooksList.setSortingEnabled(True)
        self.PswBooksSelectAllBtn.setText(_translate("MainWindow", "全选"))
        self.PswBooksClearBtn.setText(_translate("MainWindow", "清除"))
        self.SearchInput.setPlaceholderText(_translate("MainWindow", "输入搜索关键字"))
        self.SearchBtn.setText(_translate("MainWindow", "搜索"))
        self.SearchClearBtn.setText(_translate("MainWindow", "清空"))
        self.PswSelectAllBtn.setText(_translate("MainWindow", "全选"))
        self.PswClearAllBtn.setText(_translate("MainWindow", "反选"))
        self.PswBooksCloseBtn.setText(_translate("MainWindow", "关闭密码本"))
        self.AddPswBtn.setText(_translate("MainWindow", "添加密码"))
        self.DeletePswBtn.setText(_translate("MainWindow", "删除密码"))
        self.PswList.setSortingEnabled(True)
        item = self.PswList.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "勾选"))
        item = self.PswList.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "应用名"))
        item = self.PswList.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "用户名"))
        self.funcMenu.setTitle(_translate("MainWindow", "菜单"))
        self.ImportExcelAction.setText(_translate("MainWindow", "导入"))

