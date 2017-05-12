# coding=UTF-8

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from func import Controller


def main():
    app = QtWidgets.QApplication(sys.argv)
    # 主函数直接生成控制器类，调用show方法
    mainWindow = Controller()
    # ui = Ui_MainWindow()
    # ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
    pass


if __name__ == "__main__":
    main()
    pass