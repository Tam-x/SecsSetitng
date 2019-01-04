#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
限制用户输入值

Created by Tan.Xing
Created date: 2019/01/03
Last edited: 2019/01/03
'''

from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtCore import Qt, QRegExp
from PyQt5.QtGui import QRegExpValidator

class IPEdit(QLineEdit):
    def __init__(self, parent):
        super(IPEdit, self).__init__()
        self.setAlignment(Qt.AlignCenter)
        validator = QRegExpValidator(QRegExp("[0-9]|[1-9][0-9]|[1][0-9][0-9]|[2][0-4][0-9]|[2][5][0-5]"))
        self.setValidator(validator)

class AddressEdit(QLineEdit):
    def __init__(self, parent):
        super(AddressEdit, self).__init__()
        self.setAlignment(Qt.AlignCenter)
        validator = QRegExpValidator(QRegExp("[0]|[1-9][0-9]|[1][0-9][0-9]|[2][0-4][0-9]|[2][5][0-5]"))
        self.setValidator(validator)

class PortEdit(QLineEdit):
    def __init__(self, parent):
        super(PortEdit, self).__init__()
        self.setAlignment(Qt.AlignCenter)
        validator = QRegExpValidator(QRegExp("[1-9][0-9]|[1-9][0-9][0-9]|[1-9][0-9][0-9][0-9]|[1-9][0-9][0-9][0-9][0-9]"))
        self.setValidator(validator)

#40-80，无小数点输入
class MinReftEdit(QLineEdit):
    def __init__(self, parent):
        super(MinReftEdit, self).__init__()
        self.setAlignment(Qt.AlignVCenter)
        validator = QRegExpValidator(QRegExp("[4-7][0-9]|[8][0]"))
        self.setValidator(validator)

#45-85,无小数点输入
class MaxReftEdit(QLineEdit):
    def __init__(self, parent):
        super(MaxReftEdit, self).__init__()
        self.setAlignment(Qt.AlignVCenter)
        validator = QRegExpValidator(QRegExp("[4][5-9]|[5-7][0-9]|[8][0-5]"))
        self.setValidator(validator)