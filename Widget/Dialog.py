#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
Created by Tan.Xing
Created date: 2018/01/09
    2019/01/11edited: 密码输入弹框
Last edited: 2019/01/11
'''

from PyQt5 import QtGui
from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QDialogButtonBox, QHBoxLayout,QVBoxLayout
from Config import Config
import time

class AboutDialog(QDialog):
    def __init__(self, parent=None):
        super(AboutDialog, self).__init__(parent)
        self.resize(360, 190)
        self.setFixedSize(360, 190)
        self.setWindowTitle('关于')
        self.setWindowIcon((QtGui.QIcon(':about.ico')))
        label=QLabel('名称：SECS远程桌面工具', self)
        label.move(25, 30)
        label=QLabel('版本：'+ Config.VERSION, self)
        label.move(25, 60)
        label.setWordWrap(True)
        label=QLabel('免责声明：本软件涉及工业设备远程运维功能，需要专业人\n\n员在特定场景下指导使用。运维过程'
                     '与结果仅为参考，软件\n\n提供方不对任何潜在后果负责，请使用方作为参考工具使用。', self)
        label.move(25, 90)
        # label=QLabel('开发：成都雅鲁科技(2019)', self)
        # label.move(25, 120)

SUPER_PASSWORD = 'yarlung666'#type1
BASE_PASSWORD = '%ssecs%s'#type2

class PasswordDialog(QDialog):
    def __init__(self, parent=None):
        super(PasswordDialog, self).__init__(parent)
        lable = QLabel('输入密码')
        self.hint_lable = QLabel()
        self.password = QLineEdit()
        self.usertype = 0
        self.password.setEchoMode(QLineEdit.Password)
        okBtn = QDialogButtonBox(QDialogButtonBox.Ok)
        okBtn.accepted.connect(self.clickOk)
        okBtn.setCenterButtons(True)
        cancelBtn = QDialogButtonBox(QDialogButtonBox.Cancel)
        cancelBtn.rejected.connect(self.clickCancel)
        cancelBtn.setCenterButtons(True)
        hbox = QHBoxLayout()
        hbox.addWidget(okBtn)
        hbox.addWidget(cancelBtn)
        vbox = QVBoxLayout()
        vbox.addWidget(lable)
        vbox.addWidget(self.password)
        vbox.addWidget(self.hint_lable)
        vbox.addLayout(hbox)
        self.setLayout(vbox)
        self.setWindowTitle('密码弹窗')

    def clickOk(self):
        password = str(self.password.text()).strip()
        if password is None or not password:
            self.hint_lable.setText('密码为空')
        elif (self.checkPassword(password)):
            self.accept()
        else:
            self.hint_lable.setText('您输入的密码不正确！')

    def clickCancel(self):
        self.reject()

    def getTimeLabel(self):
        ##remove float##
        localTime = time.localtime(time.time())
        if localTime.tm_isdst and time.daylight:
            timezone = -time.altzone
        else:
            timezone = -time.timezone
        timeSec = time.time() + timezone
        timeStr = time.strftime("%H:%M", time.gmtime(timeSec))
        return timeStr.split(":")

    def checkPassword(self, password):
        time = self.getTimeLabel()
        hour = int(time[0])
        minute = int(time[1])
        '''
        dynamic password is the difference between current hour and minute
        + base password + the sum of current hour and minute
        '''
        dynamic_pwd = BASE_PASSWORD % (abs(hour - minute), (hour + minute))
        if password == SUPER_PASSWORD:
            self.usertype = 1
            return True
        elif password == dynamic_pwd:
            self.usertype = 2
            return True
        return False