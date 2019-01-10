#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
Created by Tan.Xing
Created date: 2018/01/09
Last edited: 2019/01/09
'''

from PyQt5 import QtGui
from PyQt5.QtWidgets import QDialog, QLabel
from Config import Config

class AboutDialog(QDialog):
    def __init__(self, parent=None):
        super(AboutDialog, self).__init__(parent)
        self.resize(350, 180)
        self.setWindowTitle('关于')
        self.setWindowIcon((QtGui.QIcon(':about.ico')))
        label=QLabel('版本：'+ Config.VERSION, self)
        label.move(25, 30)
        label=QLabel('名称：SECS远程桌面工具', self)
        label.move(25, 60)
        label=QLabel('编译环境：win8 64', self)
        label.move(25, 90)
        label=QLabel('开发：成都雅鲁科技(2019)', self)
        label.move(25, 120)