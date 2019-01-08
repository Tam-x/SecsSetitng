#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
Created by Tan.Xing
Created date: 2019/01/03
    edited: 2018/01/04:远程连接/处理界面点击事件
Last edited: 2018/01/04
'''

from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import QTimer, QTime
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
        #设置时间
        # self.timeEditWrok.setTime(QTime(11, 13))

    def init(self):
        self.dtuIp, self.dtuIpArray = self.get_dtu_ip()
        self.deviceAdr  = self.get_device_adr()
        self.dtuCom     = self.get_dtu_com()
        self.mqttServer = self.get_mqtt_server()
        self.mqttPort   = self.get_mqtt_port()
        self.mqttUser   = Config.MQTT_USER
        self.mqttCode   = Config.MQTT_CODE

    def click_event(self):
        self.btnMqttConnect.clicked.connect(self.click_btn_connect)
        self.timer.timeout.connect(self.flush_ui)
        self.btnSetSysStatus.clicked.connect(self.click_btn_sys)
        self.btnSetAlarm.clicked.connect(self.click_btn_alarm)
        self.btnSetTimeTable.clicked.connect(self.click_btn_timetable)
        self.btnSetJudgeTemp.clicked.connect(self.click_btn_judgetemp)
        self.btnSetChangeModle.clicked.connect(self.click_btn_changemodule)
        self.btnSetInterval.clicked.connect(self.click_btn_interval)
        self.btnSetLogicTemp.clicked.connect(self.click_btn_logic)
        self.btnSetWorkTime.clicked.connect(self.click_btn_worktime)
        self.btnSetOtherValue.clicked.connect(self.click_btn_other_deviation)

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
            self.infos.put(' 提示：当前没有MQTT服务器连接！')
            return None
        return True

    def click_btn_sys(self):
        if self.check_mqtt_connected():
            cmd = self.get_setting_sys_cmd()
            if cmd:
                self.infos.put('发送命令'+str(cmd)+'成功')
                self.mqttClient.publish(Config.MQTT_DOWN_TOPIC.format(self.dtuIp), bytes(cmd),0)
            else:
                self.infos.put(' 提示：系统状态栏有错误输入！')

    def click_btn_alarm(self):
        if self.check_mqtt_connected():
            cmd = self.get_setting_alarm_cmd()
            if cmd:
                self.infos.put('发送命令'+str(cmd)+'成功')
                self.mqttClient.publish(Config.MQTT_DOWN_TOPIC.format(self.dtuIp), bytes(cmd),0)

    def click_btn_timetable(self):
        if self.check_mqtt_connected():
            cmd = self.get_setting_timetable_cmd()
            if cmd:
                self.infos.put('发送命令' + str(cmd) + '成功')
                self.mqttClient.publish(Config.MQTT_DOWN_TOPIC.format(self.dtuIp), bytes(cmd), 0)

    def click_btn_judgetemp(self):
        if self.check_mqtt_connected():
            cmd = self.get_setting_judge_cmd()
            if cmd:
                self.infos.put('发送命令' + str(cmd) + '成功')
                self.mqttClient.publish(Config.MQTT_DOWN_TOPIC.format(self.dtuIp), bytes(cmd), 0)

    def click_btn_changemodule(self):
        if self.check_mqtt_connected():
            cmd = self.get_setting_changemodule_cmd()
            if cmd:
                self.infos.put('发送命令' + str(cmd) + '成功')
                self.mqttClient.publish(Config.MQTT_DOWN_TOPIC.format(self.dtuIp), bytes(cmd), 0)
            else:
                self.infos.put(' 提示：变形模组输入有误！')

    def click_btn_interval(self):
        if self.check_mqtt_connected():
            cmd = self.get_setting_interval_cmd()
            if cmd:
                self.infos.put('发送命令' + str(cmd) + '成功')
                self.mqttClient.publish(Config.MQTT_DOWN_TOPIC.format(self.dtuIp), bytes(cmd), 0)
            else:
                self.infos.put(' 提示：阀门调节时间输入有误！')

    def click_btn_logic(self):
        if self.check_mqtt_connected():
            cmd = self.get_setting_logic_cmd()
            if cmd:
                self.infos.put('发送命令' + str(cmd) + '成功')
                self.mqttClient.publish(Config.MQTT_DOWN_TOPIC.format(self.dtuIp), bytes(cmd), 0)
            else:
                self.infos.put(' 提示：阀门逻辑设定温度输入有误！')

    def click_btn_worktime(self):
        if self.check_mqtt_connected():
            cmd = self.get_setting_worktime_cmd()
            if cmd:
                self.infos.put('发送命令' + str(cmd) + '成功')
                self.mqttClient.publish(Config.MQTT_DOWN_TOPIC.format(self.dtuIp), bytes(cmd), 0)

    def click_btn_other_deviation(self):
        if self.check_mqtt_connected():
            cmd = self.get_setting_other_deviation_cmd()
            if cmd:
                self.infos.put('发送命令' + str(cmd) + '成功')
                self.mqttClient.publish(Config.MQTT_DOWN_TOPIC.format(self.dtuIp), bytes(cmd), 0)
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
        ips = []
        if ip1 and ip2 and ip3 and ip4:
            ips.append(int(ip1))
            ips.append(int(ip2))
            ips.append(int(ip3))
            ips.append(int(ip4))
            return ip1+'.'+ip2+'.' + ip3+'.' + ip4, ips
        return None, None

    def get_device_adr(self):
        adr = self.editDeviceAdr.text().strip()
        if adr:
            return int(adr)
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
                return Frame.create_frame(self.dtuIpArray, 0xA1, Utility.create_timestamp(), body)
        return None

    #0xA2:获取设置报警值阙值数据
    def get_setting_alarm_cmd(self):
        tempAlarm = self.edtAlarmTemp.text().strip()
        inPressAlarm = self.edtAlarmPressIn.text().strip()
        outPressAlarm = self.edtAlarmPressOut.text().strip()
        inFlowAlarm = self.edtAlarmFlowIn.text().strip()
        outFlowAlarm = self.edtAlarmFlowOut.text().strip()
        if not tempAlarm:
            self.infos.put(' 提示：进水管温度报警值填写不正确！')
            return False
        if not inPressAlarm:
            self.infos.put(' 提示：进水管压力报警值填写不正确！')
            return False
        if not outPressAlarm:
            self.infos.put(' 提示：出水管压力报警值填写不正确！')
            return False
        if not inFlowAlarm:
            self.infos.put(' 提示：进水管流量报警值填写不正确！')
            return False
        if not outFlowAlarm:
            self.infos.put(' 提示：出水管流量报警值填写不正确！')
            return False
        body = [self.dtuCom, self.deviceAdr]
        body.extend(Utility.int2bytes(int(tempAlarm)))
        body.extend(Utility.int2bytes(int(inPressAlarm)))
        body.extend(Utility.int2bytes(int(outPressAlarm)))
        body.extend(Utility.int2bytes(int(inFlowAlarm)))
        body.extend(Utility.int2bytes(int(outFlowAlarm)))
        return Frame.create_frame(self.dtuIpArray,0xA2, Utility.create_timestamp(), body)

    # 0xA3:获取时段相关设置值数据
    def get_setting_timetable_cmd(self):
        num = self.comTimeTableNum.currentIndex()+1
        ttable1 = self.edtTimeTable1.text().strip()
        ttable1_1 = self.edtTimeTable1_2.text().strip()
        ttable2 = self.edtTimeTable2.text().strip()
        ttable2_1 = self.edtTimeTable2_1.text().strip()
        ttable3 = self.edtTimeTable3.text().strip()
        ttable3_1 = self.edtTimeTable3_1.text().strip()
        ttable4 = self.edtTimeTable4.text().strip()
        ttable4_1 = self.edtTimeTable4_1.text().strip()
        ttable5 = self.edtTimeTable5.text().strip()
        ttable5_1 = self.edtTimeTable5_1.text().strip()
        ttable6 = self.edtTimeTable6.text().strip()
        ttable6_1 = self.edtTimeTable6_1.text().strip()
        ttable7 = self.edtTimeTable7.text().strip()
        ttable7_1 = self.edtTimeTable7_1.text().strip()
        ttable8 = self.edtTimeTable8.text().strip()
        ttable8_1 = self.edtTimeTable8_1.text().strip()
        ttable9 = self.edtTimeTable9.text().strip()
        ttable9_1 = self.edtTimeTable9_1.text().strip()
        ttable10 = self.edtTimeTable10.text().strip()
        ttable10_1 = self.edtTimeTable10_1.text().strip()
        if not ttable1 or not ttable1_1:
            self.infos.put(' 提示：时段表一值填写不正确！')
            return False
        if not ttable2 or not ttable2_1:
            self.infos.put(' 提示：时段表二值填写不正确！')
            return False
        if not ttable3 or not ttable3_1:
            self.infos.put(' 提示：时段表三值填写不正确！')
            return False
        if not ttable4 or not ttable4_1:
            self.infos.put(' 提示：时段表四值填写不正确！')
            return False
        if not ttable5 or not ttable5_1:
            self.infos.put(' 提示：时段表五值填写不正确！')
            return False
        if not ttable6 or not ttable6_1:
            self.infos.put(' 提示：时段表六值填写不正确！')
            return False
        if not ttable7 or not ttable7_1:
            self.infos.put(' 提示：时段表七值填写不正确！')
            return False
        if not ttable8 or not ttable8_1:
            self.infos.put(' 提示：时段表八值填写不正确！')
            return False
        if not ttable9 or not ttable9_1:
            self.infos.put(' 提示：时段表九值填写不正确！')
            return False
        if not ttable10 or not ttable10_1:
            self.infos.put(' 提示：时段表十值填写不正确！')
            return False
        body = [self.dtuCom, self.deviceAdr, num]
        body.extend([int(ttable1),int(ttable1_1)])
        body.extend(Utility.int2bytes(self.comTimeTable1.currentIndex()))
        body.extend([int(ttable2), int(ttable2_1)])
        body.extend(Utility.int2bytes(self.comTimeTable2.currentIndex()))
        body.extend([int(ttable3),int(ttable3_1)])
        body.extend(Utility.int2bytes(self.comTimeTable3.currentIndex()))
        body.extend([int(ttable4), int(ttable4_1)])
        body.extend(Utility.int2bytes(self.comTimeTable4.currentIndex()))
        body.extend([int(ttable5),int(ttable5_1)])
        body.extend(Utility.int2bytes(self.comTimeTable5.currentIndex()))
        body.extend([int(ttable6), int(ttable6_1)])
        body.extend(Utility.int2bytes(self.comTimeTable6.currentIndex()))
        body.extend([int(ttable7),int(ttable7_1)])
        body.extend(Utility.int2bytes(self.comTimeTable7.currentIndex()))
        body.extend([int(ttable8), int(ttable8_1)])
        body.extend(Utility.int2bytes(self.comTimeTable8.currentIndex()))
        body.extend([int(ttable9),int(ttable9_1)])
        body.extend(Utility.int2bytes(self.comTimeTable9.currentIndex()))
        body.extend([int(ttable10), int(ttable10_1)])
        body.extend(Utility.int2bytes(self.comTimeTable10.currentIndex()))
        return Frame.create_frame(self.dtuIpArray,0xA3, Utility.create_timestamp(), body)

    # 0xA4:获取逻辑控制用设定温度值数据
    def get_setting_judge_cmd(self):
        solartemp1 = self.edtSolarTemp1.text().strip()
        solartemp2 = self.edtSolarTemp2.text().strip()
        solartemp3 = self.edtSolarTemp3.text().strip()
        solartemp4 = self.edtSolarTemp4.text().strip()
        tail1 = self.edtJudgeTemp1.text().strip()
        tail2 = self.edtJudgeTemp2.text().strip()
        tail3 = self.edtJudgeTemp3.text().strip()
        if not solartemp1:
            self.infos.put(' 提示：太阳能出水设定温度值1填写不正确！')
            return False
        if not solartemp2:
            self.infos.put(' 提示：太阳能出水设定温度值2填写不正确！')
            return False
        if not solartemp3:
            self.infos.put(' 提示：太阳能出水设定温度值3填写不正确！')
            return False
        if not solartemp4:
            self.infos.put(' 提示：太阳能出水设定温度值4填写不正确！')
            return False
        if not tail1:
            self.infos.put(' 提示：末端回水低温判断值1填写不正确！')
            return False
        if not tail2:
            self.infos.put(' 提示：末端回水低温判断值2填写不正确！')
            return False
        if not tail3:
            self.infos.put(' 提示：末端回水低温判断值3填写不正确！')
            return False
        body = [self.dtuCom, self.deviceAdr]
        body.extend(Utility.int2bytes(int(solartemp1)))
        body.extend(Utility.int2bytes(int(solartemp2)))
        body.extend(Utility.int2bytes(int(solartemp3)))
        body.extend(Utility.int2bytes(int(solartemp4)))
        body.extend(Utility.int2bytes(int(tail1)))
        body.extend(Utility.int2bytes(int(tail2)))
        body.extend(Utility.int2bytes(int(tail3)))
        return Frame.create_frame(self.dtuIpArray,0xA4, Utility.create_timestamp(), body)

    #0xA5:获取设置相变模组偏移值
    def get_setting_changemodule_cmd(self):
        num = self.edtChangeModleNum.text().strip()
        deviation   = self.edtChangeModleValue.text().strip()
        if num and deviation:
            deviation = int(float(deviation) * 10)
            body = [self.dtuCom, self.deviceAdr, int(num), deviation]
            return Frame.create_frame(self.dtuIpArray, 0xA5, Utility.create_timestamp(), body)
        return None

    #0xA6:获取阀门调节间隔数据
    def get_setting_interval_cmd(self):
        p = self.edtPinterval.text().strip()
        f = self.edtFinterval.text().strip()
        if p and f:
            body = [self.dtuCom, self.deviceAdr]
            body.extend(Utility.int2bytes(int(p)))
            body.extend(Utility.int2bytes(int(f)))
            return Frame.create_frame(self.dtuIpArray, 0xA6, Utility.create_timestamp(), body)
        return False

    #0xA7:获取阀门调节间隔数据
    def get_setting_logic_cmd(self):
        temp = self.edtLogicTemp.text().strip()
        temp1 = self.edtLogicTemp1.text().strip()
        temp2 = self.edtLogicTemp2.text().strip()
        if temp and temp1 and temp2:
            body = [self.dtuCom, self.deviceAdr, int(temp), int(temp1), int(temp2)]
            return Frame.create_frame(self.dtuIpArray, 0xA7, Utility.create_timestamp(), body)
        return False

    #0xA8:获取工作时间设定数据
    def get_setting_worktime_cmd(self):
        status = self.get_work_status()
        work = self.timeEditWrok.text().split(':')
        workHour = int(work[0])
        workMinite = int(work[1])
        day = self.timeEditOffWork.text()
        offWorkHour = int(day[0])
        offWorkMinite = int(day[1])
        body = [self.dtuCom, self.deviceAdr, status, workHour, workMinite, offWorkHour, offWorkMinite]
        return Frame.create_frame(self.dtuIpArray, 0xA8, Utility.create_timestamp(), body)

    def get_work_status(self):
        if self.rdoWorkday.isChecked():
            return 0
        return 1

    #0xA9:获取其他偏移值数据
    def get_setting_other_deviation_cmd(self):
        sun = self.edtOtherSolar.text().strip()
        outdoor = self.edtOtherTemp.text().strip()
        waterIn = self.edtOtherWaterIn.text().strip()
        waterOut = self.edtOtherWaterOut.text().strip()
        if not sun or float(sun) > 25.5:
            self.infos.put(' 提示：太阳能温度偏差填写不正确！')
            return False
        if not waterOut or float(waterOut) > 25.5:
            self.infos.put(' 提示：末端回水偏移填写不正确！')
            return False
        if not outdoor or float(outdoor) > 25.5:
            self.infos.put(' 提示：室外温度偏移填写不正确！')
            return False
        if not waterIn or float(waterIn) > 25.5:
            self.infos.put(' 提示：末端进水偏移填写不正确！')
            return False
        body = [self.dtuCom, self.deviceAdr, int(float(sun)*10), int(float(waterOut)*10), int(float(outdoor)*10), int(float(waterIn)*10)]
        return Frame.create_frame(self.dtuIpArray, 0xA9, Utility.create_timestamp(), body)
