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

#小时输入框
class HourEdit(QLineEdit):
    def __init__(self, parent):
        super(HourEdit, self).__init__()
        self.setAlignment(Qt.AlignCenter)
        validator = QRegExpValidator(QRegExp("[0-9]|[1][0-9]|[2][0-3]"))
        self.setValidator(validator)

#分钟输入框
class MiniteEdit(QLineEdit):
    def __init__(self, parent):
        super(MiniteEdit, self).__init__()
        self.setAlignment(Qt.AlignCenter)
        validator = QRegExpValidator(QRegExp("[0-9]|[1-5][0-9]"))
        self.setValidator(validator)

#模组编号输入框
class ModuleEdit(QLineEdit):
    def __init__(self, parent):
        super(ModuleEdit, self).__init__()
        self.setAlignment(Qt.AlignVCenter)
        validator = QRegExpValidator(QRegExp("[1-9]|[1-7][0-9]|[8][0]"))
        self.setValidator(validator)

#偏移值
class DeviationEdit(QLineEdit):
    def __init__(self, parent):
        super(DeviationEdit, self).__init__()
        self.setAlignment(Qt.AlignVCenter)
        validator = QRegExpValidator(QRegExp('^-?[0-9]([.]{1}[0-9]{1})?$|^-12.8$|1[0-2]([.]{1}[0-7]{1})?$'))
        self.setValidator(validator)

#32-bit singed integer
class SingedInteger(QLineEdit):
    def __init__(self, parent):
        super(SingedInteger, self).__init__()
        validator = QRegExpValidator(QRegExp('^-?(\d{1,9}|1\d{9}|2(0\d{8}|1([0-3]\d{7}|4([0-6]\d{6}|7([0-3]\d{5}|4([0-7]\d{4}|8([0-2]\d{3}|3([0-5]\d{2}|6([0-3]\d|4[0-7])))))))))$|^-2147483648$'))
        self.setValidator(validator)

# 16-bit singed short 32767
class SingedShort(QLineEdit):
    def __init__(self, parent):
        super(SingedShort, self).__init__()
        validator = QRegExpValidator(QRegExp('^-?(\d{1,4}|[1-2]\d{4}|3([0-1]{3}|2([0-6]\d{2}|7([0-5]\d{1}|6([0-7])))))$|^-32768$'))
        self.setValidator(validator)

# 16-bit singed short 65535
class UnSingedShort(QLineEdit):
    def __init__(self, parent):
        super(UnSingedShort, self).__init__()
        validator = QRegExpValidator(QRegExp('[1-9]\d{1,3}|[1-5]\d{4}|6([1-4]\d{3}|5([0-4]{2}|5([0-2]\d{1}|3([0-5]))))$|^0'))
        self.setValidator(validator)


# 8-bit singed byte 127
class SingedByte(QLineEdit):
    def __init__(self, parent):
        super(SingedByte, self).__init__()
        validator = QRegExpValidator(QRegExp('^-?([1-9][0-9]|1([0-1]\d|2[0-7]))$|^-128$|0'))
        self.setValidator(validator)

#整数
class Number(QLineEdit):
    def __init__(self, parent):
        super(Number, self).__init__()
        self.setAlignment(Qt.AlignVCenter)
        validator = QRegExpValidator(QRegExp("^(0|-?[1-9][0-9]*)$"))
        self.setValidator(validator)