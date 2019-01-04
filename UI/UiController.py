#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
Created by Tan.Xing
Created date: 2019/01/03
    edited: 2018/01/04:远程连接/处理界面点击事件
Last edited: 2018/01/04
'''

from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import QTimer
from UI.UI import Ui_mainWindow
import paho.mqtt.client as mqtt
from Config import Config
from Util import Utility
from Frame import Frame
import re, threading, time, queue

class windowController(Ui_mainWindow, QDialog):
    def __init__(self, widget):
        super(windowController, self).__init__()
        self.setupUi(widget)
        widget.set_close(self.disconnect_remote)
        self.lastConnectTime = 0
        self.isConnected = False
        self.notifyConnectedStatus = False
        self.notifyUnconnectedStatus = False
        self.timer = QTimer()
        self.timer.start(5)
        self.infos  = queue.Queue()
        self.init()
        self.click_event()

    def init(self):
        self.dtuIp      = self.get_dtu_ip()
        self.deviceAdr  = self.get_device_adr()
        self.dtuCom     = self.get_dtu_com()
        self.mqttServer = self.get_mqtt_server()
        self.mqttPort   = self.get_mqtt_port()
        self.mqttUser   = Config.MQTT_USER
        self.mqttCode   = Config.MQTT_CODE

    def click_event(self):
        self.btnMqttConnect.clicked.connect(self.click_btn_connect)
        self.timer.timeout.connect(self.flush_ui)

    def flush_ui(self):
        while self.infos.qsize()>0:
            self.statusbar.showMessage(self.infos.get())

        if self.notifyConnectedStatus:
            self.notifyConnectedStatus = False
            self.mqtt_connected_status()

        if self.notifyUnconnectedStatus:
            self.notifyUnconnectedStatus = False
            self.mqtt_unconnected_status()

# |---------------------------------|#
# |          连接MQTT服务器         |
# | ---------------------------------|#
#
    def check_input_info(self):
        if not self.dtuIp:
            self.statusbar.showMessage('DTU地址填写有误！')
            return None
        if not self.deviceAdr:
            self.statusbar.showMessage('设备地址填写有误！')
            return None
        if not self.mqttServer:
            self.statusbar.showMessage('MQTT服务器填写有误！')
            return None
        if not self.mqttPort:
            self.statusbar.showMessage('MQTT端口号填写有误！')
            return None
        return 'ok'

    def mqtt_connected_status(self):
        self.isConnected = True
        self.btnMqttConnect.setText('断开')

    def mqtt_unconnected_status(self):
        self.isConnected = False
        self.btnMqttConnect.setText('连接')

    def click_btn_connect(self):
        if self.isConnected:
            self.disconnect_remote()
        else:
            self.connect_remote()

    def connect_remote(self):
        self.statusbar.showMessage('开始连接...')
        if self.limit_click_freq():
            self.init()
            if self.check_input_info():
                self.start_mqtt_client()

    def disconnect_remote(self):
        try:
            if self.limit_click_freq():
                self.statusbar.showMessage('与服务器断开连接！')
                self.mqttClient.disconnect()
                self.notifyUnconnectedStatus = True
        except:
            self.notifyUnconnectedStatus = True

    def limit_click_freq(self):
        if int(round(time.time() * 1000)) - self.lastConnectTime < Config.BTN_CLICK_INTERVAL:
            self.statusbar.showMessage('点击太频繁了!')
            return None
        self.lastConnectTime = int(round(time.time() * 1000))
        return 'ok'

    def start_mqtt_client(self):
        thread = threading.Thread(target=self.client_mqtt_loop)
        thread.start()

    def client_mqtt_loop(self):
        client_id = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        self.mqttClient = mqtt.Client(Config.MQTT_CLIENT + client_id)
        self.mqttClient.username_pw_set(self.mqttUser, self.mqttCode)
        self.mqttClient.on_connect = self.on_connect_remote
        self.mqttClient.on_message = self.on_message_remote
        try:
            self.mqttClient.connect(self.mqttServer, self.mqttPort, 10)
            self.mqttClient.loop_forever()
        except Exception as e:
            self.infos.put(str(e.args))
            self.isConnected = False

    def on_connect_remote(self, client, userdata, flags, rc):
        self.infos.put("Connected remote with result code " + str(rc))
        if rc == 0:
            self.isConnected = True
            self.infos.put('连接服务器成功！')
            client.subscribe(Config.MQTT_UP_TOPIC.format(self.dtuIp))
            self.notifyConnectedStatus = True

    def on_message_remote(self, client, userdata, msg):
        Utility.show_log(msg.topic + " " + msg.payload.decode("utf-8"))
        # self.handle_remote_msg(msg.payload.decode("utf-8"))

#|---------------------------------|#
#|          界面点击事件           |
#| ---------------------------------|#
#
    def check_mqtt_connected(self):
        if not self.isConnected:
            self.infos.put('当前没有MQTT服务器连接...')
            return None
        return True

    def click_btn_sys(self):
        if self.check_mqtt_connected():
            self.mqttClient.publish()



#|---------------------------------|#
#|          获取界面信息           |
#| ---------------------------------|#
#
    #首行信息
    def get_dtu_ip(self):
        ip1 = self.editDtuIp_1.text().strip()
        ip2 = self.editDtuIp_2.text().strip()
        ip3 = self.editDtuIp_3.text().strip()
        ip4 = self.editDtuIp_4.text().strip()
        if ip1 and ip2 and ip3 and ip4:
            return ip1+'.'+ip2+'.' + ip3+'.' + ip4
        return None

    def get_device_adr(self):
        adr = self.editDeviceAdr.text().strip()
        if adr:
            return adr
        return None

    def get_dtu_com(self):
        return self.comboBox.currentIndex()+2

    def get_mqtt_server(self):
        ip1 = self.editMqttAdr.text().strip()
        ip2 = self.editMqttAdr_2.text().strip()
        ip3 = self.editMqttAdr_3.text().strip()
        ip4 = self.editMqttAdr_4.text().strip()
        if ip1 and ip2 and ip3 and ip4:
            return ip1+'.'+ip2+'.' + ip3+'.' + ip4
        return None

    def get_mqtt_port(self):
        port = self.editMqttPort.text().strip()
        if port:
            return int(port)
        return None

    #0xA1:获取设置系统状态数据
    def get_setting_sys_cmd(self):
        bootStatus = self.comBootStatus.currentIndex()
        workMode   = self.comWorkMode.currentIndex()
        supplyHeat = self.comSupplyHeat.currentIndex()
        dayMode    = self.comDayMode.currentIndex()
        minReft    = self.edtMinReft.text().strip()
        maxReft    = self.edtMaxRefT.text().strip()
        if minReft and maxReft:
            minReft = int(minReft)
            maxReft = int(maxReft)
            if minReft > 39 and maxReft > 44:
                body = [self.dtuCom, self.deviceAdr, bootStatus, workMode, supplyHeat, dayMode, minReft, maxReft]
                return Frame.create_frame(self.ip, Utility.create_timestamp(), body)
        return None

    #0xA2:获取设置报警值阙值数据
    def get_setting_alarm_cmd(self):
        tempAlarm = self.edi

