#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
Created by Tan.Xing
Created date: 2019/01/03
Last edited: 2019/01/03
'''

import sys
from PyQt5.QtWidgets import QApplication
from UI.UiController import windowController
from Widget.SafeCloseWindow import SafeCloseMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = SafeCloseMainWindow()
    main = windowController(mainWindow)
    mainWindow.setFixedSize(1036, 660)
    mainWindow.show()
    sys.exit(app.exec_())
    pass