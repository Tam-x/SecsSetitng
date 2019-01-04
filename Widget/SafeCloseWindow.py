#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
网络非法断开后关闭连接

Created by Tan.Xing
Created date: 2019/01/03
Last edited: 2019/01/03
'''

from PyQt5.QtWidgets import QMainWindow

class SafeCloseMainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

    def set_close(self, close):
        self.close = close

    def closeEvent(self, event):
        try:
            self.close()
        except:
            pass
        super(SafeCloseMainWindow, self).closeEvent(event)