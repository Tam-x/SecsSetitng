#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
Created by Tan.Xing
Created date: 2019/01/03
    edited: 2019/01/04:远程连接/处理界面点击事件
    edited: 2019/01/08:获取界面设置命令及输入限制
    edited: 2019/01/09:功能测试
    edited: 2019/01/10:增加配置导入
Last edited: 2019/01/10
'''

from PyQt5.QtWidgets import QDialog, QFileDialog
from PyQt5.QtCore import QTimer, QTime
from UI.UI import Ui_mainWindow
from Widget.Dialog import AboutDialog
import paho.mqtt.client as mqtt
from Config import Config
from Util import Utility
from Frame import Frame
import ctypes
import threading, time, queue

class windowController(Ui_mainWindow, QDialog):
    def __init__(self, widget):
        super(windowController, self).__init__()
        self.setupUi(widget)
        widget.set_close(self.disconnect_remote)
        self.lastConnectTime = 0
        self.isConnecting = False
        self.isConnected = False
        self.notifyConnectedStatus = False
        self.notifyUnconnectedStatus = False
        self.isSupperPwd = False
        self.isCoustomPwd = False
        self.inputPwdTime = 0
        self.mqttUser   = Config.MQTT_USER
        self.mqttCode   = Config.MQTT_CODE

        self.cmdA1 = False
        self.cmdA2 = False
        self.cmdA3 = False
        self.cmdA4 = False
        self.cmdA5 = False
        self.cmdA6 = False
        self.cmdA7 = False
        self.cmdA8 = False
        self.cmdA9 = False

        self.timer = QTimer()
        self.timer.start(5)
        self.infos  = queue.Queue()
        self.init()
        self.click_event()

    def init(self):
        self.dtuIp, self.dtuIpArray = self.get_dtu_ip()
        self.deviceAdr  = self.get_device_adr()
        self.dtuCom     = self.get_dtu_com()
        self.mqttServer = self.get_mqtt_server()
        self.mqttPort   = self.get_mqtt_port()

    def click_event(self):
        self.btnMqttConnect.clicked.connect(self.click_btn_connect)
        self.timer.timeout.connect(self.flush_ui)
        self.action_DTU.triggered.connect(self.activate_dtu)
        self.action_DTU_2.triggered.connect(self.reactivate_dtu)
        self.action_2.triggered.connect(self.about_dialog)
        self.action.triggered.connect(self.closeEvent)
        self.action_3.triggered.connect(self.open_file)
        #设置
        self.btnSetSysStatus.clicked.connect(self.click_btn_sys)
        self.btnSetAlarm.clicked.connect(self.click_btn_alarm)
        self.btnSetTimeTable.clicked.connect(self.click_btn_timetable)
        self.btnSetJudgeTemp.clicked.connect(self.click_btn_judgetemp)
        self.btnSetChangeModle.clicked.connect(self.click_btn_changemodule)
        self.btnSetInterval.clicked.connect(self.click_btn_interval)
        self.btnSetLogicTemp.clicked.connect(self.click_btn_logic)
        self.btnSetWorkTime.clicked.connect(self.click_btn_worktime)
        self.btnSetOtherValue.clicked.connect(self.click_btn_other_deviation)
        self.btnSetOtherTime.clicked.connect(self.click_btn_setting_time)
        self.btnSetCleanElc.clicked.connect(self.click_btn_other)

        #读取
        self.btnReadSysStatus.clicked.connect(self.click_read_sys)
        self.btnReadAlarm.clicked.connect(self.click_read_alarm)
        self.btnReadTimeTable.clicked.connect(self.click_read_interval)
        self.btnReadJudgeTemp.clicked.connect(self.click_read_judge_temp)
        self.btnReadChangeModle.clicked.connect(self.click_read_module)
        self.btnReadInterval.clicked.connect(self.click_read_valve)
        self.btnReadLogicTemp.clicked.connect(self.click_read_logic)
        self.btnReadWork.clicked.connect(self.click_read_work)
        self.btnReadOtherValue.clicked.connect(self.click_read_other_deviation)

    def activate_dtu(self):
        if self.check_mqtt_connected() and self.limit_click_freq():
            cmd = self.get_reading_cmd(0x901)
            self.infos.put('[系统激活DTU]命令' + str(cmd) + '发送成功。')
            self.mqttClient.publish(Config.MQTT_DOWN_TOPIC.format(self.dtuIp), bytes(cmd), 0)

    def reactivate_dtu(self):
        if self.check_mqtt_connected() and self.limit_click_freq():
            cmd = self.get_reading_cmd(0x900)
            self.infos.put('[系统去活DTU]命令' + str(cmd) + '发送成功。')
            self.mqttClient.publish(Config.MQTT_DOWN_TOPIC.format(self.dtuIp), bytes(cmd), 0)

    def about_dialog(self):
        dialog = AboutDialog()
        dialog.setStyleSheet("QDialog {\n"
        "    background-color: #BBBBBB;\n"
        "    font-family: \"Segoe UI\";\n"
        "}\n")
        result = dialog.exec_()
        if result == QDialog.Accepted:
            return True
        return False

    def open_file(self):
        fileName = QFileDialog.getOpenFileName(caption='选择mqtt配置文件')
        info = '导入配置'
        if fileName:
            try:
                # for line in open(fileName[0]):
                with open(fileName[0]) as f:
                    for line in f.readlines():
                        print(line)
                        if '#' not in line and line.strip():
                            if 'mqtt_broker' in line:
                                server = line.split(':')[1].replace("\n", "").strip()
                                info += ' | 地址: '+server
                                self.editMqttAdr.setText(server)
                            elif 'mqtt_user' in line:
                                self.mqttUser = line.split(':')[1].strip().replace("\n", "")
                                info += ' | 账号: ' + self.mqttUser
                            elif 'mqtt_pwd' in line:
                                self.mqttCode = line.split(':')[1].strip().replace("\n", "")
                                info += ' | 密码: ' + self.mqttCode
                    if '|' in info:
                        self.infos.put(info)
                    else:
                        self.infos.put(info+':none!')
            except:
                pass

    def flush_ui(self):
        while self.infos.qsize()>0:
            self.statusbar.showMessage(self.infos.get())

        if self.notifyConnectedStatus:
            self.notifyConnectedStatus = False
            self.mqtt_connected_status()

        if self.notifyUnconnectedStatus:
            self.notifyUnconnectedStatus = False
            self.mqtt_unconnected_status()

        if self.isCoustomPwd:
            if time.time() - self.inputPwdTime > Config.PWD_INPUT_INTERVAL:
                self.isCoustomPwd = False
                if self.isConnected:
                    try:
                        self.statusbar.showMessage('与服务器断开连接！')
                        self.mqttClient.disconnect()
                        self.notifyUnconnectedStatus = True
                    except:
                        self.notifyUnconnectedStatus = True

        if self.cmdA1:
            self.cmdA1 = False
            self.handle_sys_frame()
        if self.cmdA2:
            self.cmdA2 = False
            self.handle_alarm_frame()
        if self.cmdA3:
            self.cmdA3 = False
            self.handle_timetable_frame()
        if self.cmdA4:
            self.cmdA4 = False
            self.handle_judge_frame()
        if self.cmdA5:
            self.cmdA5 = False
            self.handle_module_frame()
        if self.cmdA6:
            self.cmdA6 = False
            self.handle_valve_interval_frame()
        if self.cmdA7:
            self.cmdA7 = False
            self.handle_valve_logic_frame()
        if self.cmdA8:
            self.cmdA8 = False
            self.handle_worktime_frame()
        if self.cmdA9:
            self.cmdA9 = False
            self.handle_other_deviation_frame()

    # |---------------------------------|#
    # |          连接MQTT服务器         |
    # | ---------------------------------|#
    #
    def check_input_info(self):
        if not self.dtuIp:
            self.statusbar.showMessage('DTU地址填写有误！')
            return None
        if not self.deviceAdr and self.deviceAdr is not 0:
            self.statusbar.showMessage('设备地址填写有误！')
            return None
        if not self.mqttServer:
            self.statusbar.showMessage('MQTT服务器填写有误！')
            return None
        if not self.mqttPort:
            self.statusbar.showMessage('MQTT端口号填写有误！')
            return None
        return True

    def mqtt_connected_status(self):
        self.isConnected = True
        self.btnMqttConnect.setText('断开')

    def mqtt_unconnected_status(self):
        self.isConnected = False
        self.btnMqttConnect.setText('连接')

    def click_btn_connect(self):
        if not self.isCoustomPwd and not self.isSupperPwd:
            res = Utility.check_password()
            if not res:
                return False
            if res == 1:
                self.isSupperPwd = True
                self.infos.put('欢迎无敌超级用户666登陆！')
            else:
                self.inputPwdTime = time.time()
                self.isCoustomPwd = True
                self.infos.put('欢迎用户登陆！')

        if self.isConnecting:
            self.statusbar.showMessage('正在连接远程服务器...')
            return
        if self.isConnected:
            self.disconnect_remote()
        else:
            self.connect_remote()

    def connect_remote(self):
        self.infos.put('开始连接...')
        if self.limit_click_freq():
            self.init()
            if self.check_input_info():
                self.start_mqtt_client()

    def disconnect_remote(self):
        try:
            if self.limit_click_freq():
                self.infos.put('与服务器断开连接！')
                self.mqttClient.disconnect()
                self.notifyUnconnectedStatus = True
        except:
            self.notifyUnconnectedStatus = True

    def limit_click_freq(self):
        if int(round(time.time() * 1000)) - self.lastConnectTime < Config.BTN_CLICK_INTERVAL:
            self.statusbar.showMessage('点击太频繁了!')
            return False
        self.lastConnectTime = int(round(time.time() * 1000))
        return True

    def start_mqtt_client(self):
        self.isConnecting = True
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
            self.infos.put('连接远程服务器'+self.mqttServer+'失败：'+str(e.args))
            self.isConnected = False
            self.isConnecting = False
            self.notifyUnconnectedStatus = True

    def on_connect_remote(self, client, userdata, flags, rc):
        self.infos.put("Connected remote with result code " + str(rc))
        if rc == 0:
            self.isConnected = True
            self.infos.put('连接服务器成功！')
            client.subscribe(Config.MQTT_UP_TOPIC.format(self.dtuIp))
            self.notifyConnectedStatus = True
        self.isConnecting = False

    def on_message_remote(self, client, userdata, msg):
        # self.infos.put('订阅到消息：'+msg.topic + "  " + str(msg.payload))
        self.handle_remote_msg(msg.payload)

#|---------------------------------|#
#|          界面点击事件           |
#| ---------------------------------|#
#
    def check_mqtt_connected(self):
        if not self.isConnected:
            self.infos.put(' 提示：当前没有MQTT服务器连接！')
            return False
        return True

    def click_btn_sys(self):
        if self.check_mqtt_connected() and self.limit_click_freq():
            cmd = self.get_setting_sys_cmd()
            if cmd:
                self.infos.put('设置系统状态命令' + str(cmd) + '发送成功。')
                self.mqttClient.publish(Config.MQTT_DOWN_TOPIC.format(self.dtuIp), bytes(cmd),0)
            else:
                self.infos.put(' 提示：系统状态栏有错误输入！')

    def click_btn_alarm(self):
        if self.check_mqtt_connected() and self.limit_click_freq():
            cmd = self.get_setting_alarm_cmd()
            if cmd:
                self.infos.put('设置报警阙值命令' + str(cmd) + '发送成功。')
                self.mqttClient.publish(Config.MQTT_DOWN_TOPIC.format(self.dtuIp), bytes(cmd),0)

    def click_btn_timetable(self) :
        if self.check_mqtt_connected() and self.limit_click_freq():
            cmd = self.get_setting_timetable_cmd()
            if cmd:
                self.infos.put('设置时段命令' + str(cmd) + '发送成功。')
                self.mqttClient.publish(Config.MQTT_DOWN_TOPIC.format(self.dtuIp), bytes(cmd), 0)

    def click_btn_judgetemp(self):
        if self.check_mqtt_connected() and self.limit_click_freq():
            cmd = self.get_setting_judge_cmd()
            if cmd:
                self.infos.put('设置逻辑控制命令' + str(cmd) + '发送成功。')
                self.mqttClient.publish(Config.MQTT_DOWN_TOPIC.format(self.dtuIp), bytes(cmd), 0)

    def click_btn_changemodule(self) :
        if self.check_mqtt_connected() and self.limit_click_freq():
            cmd = self.get_setting_changemodule_cmd()
            if cmd:
                self.infos.put('设置变形模组命令' + str(cmd) + '发送成功。')
                self.mqttClient.publish(Config.MQTT_DOWN_TOPIC.format(self.dtuIp), bytes(cmd), 0)
            else:
                self.infos.put(' 提示：变形模组输入有误！')

    def click_btn_interval(self):
        if self.check_mqtt_connected() and self.limit_click_freq():
            cmd = self.get_setting_interval_cmd()
            if cmd:
                self.infos.put('设置阀门调节时间命令' + str(cmd) + '发送成功。')
                self.mqttClient.publish(Config.MQTT_DOWN_TOPIC.format(self.dtuIp), bytes(cmd), 0)
            else:
                self.infos.put(' 提示：阀门调节时间输入有误！')

    def click_btn_logic(self):
        if self.check_mqtt_connected() and self.limit_click_freq():
            cmd = self.get_setting_logic_cmd()
            if cmd:
                self.infos.put('设置阀门逻辑设定温度命令' + str(cmd) + '发送成功。')
                self.mqttClient.publish(Config.MQTT_DOWN_TOPIC.format(self.dtuIp), bytes(cmd), 0)
            else:
                self.infos.put(' 提示：阀门逻辑设定温度输入有误！')

    def click_btn_worktime(self):
        if self.check_mqtt_connected() and self.limit_click_freq():
            cmd = self.get_setting_worktime_cmd()
            if cmd:
                self.infos.put('设置工作时间命令' + str(cmd) + '发送成功。')
                self.mqttClient.publish(Config.MQTT_DOWN_TOPIC.format(self.dtuIp), bytes(cmd), 0)

    def click_btn_other_deviation(self):
        if self.check_mqtt_connected() and self.limit_click_freq():
            cmd = self.get_setting_other_deviation_cmd()
            if cmd:
                self.infos.put('设置其他偏移命令' + str(cmd) + '发送成功。')
                self.mqttClient.publish(Config.MQTT_DOWN_TOPIC.format(self.dtuIp), bytes(cmd), 0)

    def click_btn_setting_time(self):
        if self.check_mqtt_connected() and self.limit_click_freq():
            cmd = self.get_setting_date_cmd()
            self.infos.put('设置时间命令' + str(cmd) + '发送成功。')
            self.mqttClient.publish(Config.MQTT_DOWN_TOPIC.format(self.dtuIp), bytes(cmd), 0)

    def click_btn_other(self):
        self.infos.put('你点击了[其他设置]按钮...')
    
    ###############################读取界面###############################

    def click_read_sys(self):
        if self.check_mqtt_connected() and self.limit_click_freq():
            cmd = self.get_reading_cmd(0x91)
            self.infos.put('读取[系统状态]命令' + str(cmd) + '发送成功。')
            self.mqttClient.publish(Config.MQTT_DOWN_TOPIC.format(self.dtuIp), bytes(cmd), 0)

    def click_read_alarm(self):
        if self.check_mqtt_connected() and self.limit_click_freq():
            cmd = self.get_reading_cmd(0x92)
            self.infos.put('读取[报警值阙值]命令' + str(cmd) + '发送成功。')
            self.mqttClient.publish(Config.MQTT_DOWN_TOPIC.format(self.dtuIp), bytes(cmd), 0)

    def click_read_interval(self):
        if self.check_mqtt_connected() and self.limit_click_freq():
            cmd = self.get_reading_cmd(0x93)
            self.infos.put('读取[时段相关设置]命令' + str(cmd) + '发送成功。')
            self.mqttClient.publish(Config.MQTT_DOWN_TOPIC.format(self.dtuIp), bytes(cmd), 0)

    def click_read_judge_temp(self):
        if self.check_mqtt_connected() and self.limit_click_freq():
            cmd = self.get_reading_cmd(0x94)
            self.infos.put('读取[逻辑控制用设定温度]命令' + str(cmd) + '发送成功。')
            self.mqttClient.publish(Config.MQTT_DOWN_TOPIC.format(self.dtuIp), bytes(cmd), 0)

    def click_read_module(self):
        if self.check_mqtt_connected() and self.limit_click_freq():
            cmd = self.get_reading_cmd(0x95)
            if not cmd:
                self.infos.put(' 提示：请输入相变模组编号！')
                return
            self.infos.put('读取[相变模组偏移值]命令' + str(cmd) + '发送成功。')
            self.mqttClient.publish(Config.MQTT_DOWN_TOPIC.format(self.dtuIp), bytes(cmd), 0)

    def click_read_valve(self):
        if self.check_mqtt_connected() and self.limit_click_freq():
            cmd = self.get_reading_cmd(0x96)
            self.infos.put('读取[阀门调节间隔]命令' + str(cmd) + '发送成功。')
            self.mqttClient.publish(Config.MQTT_DOWN_TOPIC.format(self.dtuIp), bytes(cmd), 0)

    def click_read_logic(self):
        if self.check_mqtt_connected() and self.limit_click_freq():
            cmd = self.get_reading_cmd(0x97)
            self.infos.put('读取[阀门逻辑设定温度]命令' + str(cmd) + '发送成功。')
            self.mqttClient.publish(Config.MQTT_DOWN_TOPIC.format(self.dtuIp), bytes(cmd), 0)

    def click_read_work(self):
        if self.check_mqtt_connected() and self.limit_click_freq():
            cmd = self.get_reading_cmd(0x98)
            self.infos.put('读取[工作时间]命令' + str(cmd) + '发送成功。')
            self.mqttClient.publish(Config.MQTT_DOWN_TOPIC.format(self.dtuIp), bytes(cmd), 0)

    def click_read_other_deviation(self):
        if self.check_mqtt_connected() and self.limit_click_freq():
            cmd = self.get_reading_cmd(0x99)
            self.infos.put('读取[其他偏移值]命令' + str(cmd) + '发送成功。')
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
        return self.comboBox.currentIndex()+1

    def get_mqtt_server(self):
        server = self.editMqttAdr.text().strip()
        if server:
            return server
        return None

    def get_mqtt_port(self):
        port = self.editMqttPort.text().strip()
        if port:
            return int(port)
        if self.importPort:
            return self.mqttPort
        return None

#############################################################
#                          设置命令                         #
#############################################################

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
        if not tempAlarm or tempAlarm == '-':
            self.infos.put(' 提示：进水管温度报警值填写不正确！')
            return False
        if not inPressAlarm or inPressAlarm == '-':
            self.infos.put(' 提示：进水管压力报警值填写不正确！')
            return False
        if not outPressAlarm or outPressAlarm == '-':
            self.infos.put(' 提示：出水管压力报警值填写不正确！')
            return False
        if not inFlowAlarm or inFlowAlarm == '-':
            self.infos.put(' 提示：进水管流量报警值填写不正确！')
            return False
        if not outFlowAlarm or outFlowAlarm == '-':
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
        if not solartemp1 or solartemp1 == '-':
            self.infos.put(' 提示：太阳能出水设定温度值1填写不正确！')
            return False
        if not solartemp2 or solartemp2 == '-':
            self.infos.put(' 提示：太阳能出水设定温度值2填写不正确！')
            return False
        if not solartemp3 or solartemp3 == '-':
            self.infos.put(' 提示：太阳能出水设定温度值3填写不正确！')
            return False
        if not solartemp4 or solartemp4 == '-':
            self.infos.put(' 提示：太阳能出水设定温度值4填写不正确！')
            return False
        if not tail1 or tail1 == '-':
            self.infos.put(' 提示：末端回水低温判断值1填写不正确！')
            return False
        if not tail2 or tail2 == '-':
            self.infos.put(' 提示：末端回水低温判断值2填写不正确！')
            return False
        if not tail3 or tail3 == '-':
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
        deviation  = self.edtChangeModleValue.text().strip()
        if num and deviation and deviation is not '-':
            deviation = int(float(deviation) * 10)
            if deviation < 0:
                deviation = Utility.negative_1byte(deviation)
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

    #0xA7:获取阀门逻辑设定温度数据
    def get_setting_logic_cmd(self):
        temp = self.edtLogicTemp.text().strip()
        temp1 = self.edtLogicTemp1.text().strip()
        temp2 = self.edtLogicTemp2.text().strip()
        if temp and temp1 and temp2 and temp is not '-' and temp1 is not '-' and temp2 is not '-':
            if int(temp) < 0:
                temp = Utility.negative_1byte(int(temp))
            if int(temp1) < 0:
                temp1 = Utility.negative_1byte(int(temp1))
            if int(temp2) < 0:
                temp2 = Utility.negative_1byte(int(temp2))
            body = [self.dtuCom, self.deviceAdr, int(temp), int(temp1), int(temp2)]
            return Frame.create_frame(self.dtuIpArray, 0xA7, Utility.create_timestamp(), body)
        return False

    #0xA8:获取工作时间设定数据
    def get_setting_worktime_cmd(self):
        status = self.get_work_status()
        work = self.timeEditWrok.text().split(':')
        workHour = int(work[0])
        workMinite = int(work[1])
        day = self.timeEditOffWork.text().split(':')
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
        if not sun and sun is not '-':
            self.infos.put(' 提示：太阳能温度偏差填写不正确！')
            return False
        if not waterOut and waterOut is not '-':
            self.infos.put(' 提示：末端回水偏移填写不正确！')
            return False
        if not outdoor and outdoor is not '-':
            self.infos.put(' 提示：室外温度偏移填写不正确！')
            return False
        if not waterIn and waterIn is not '-':
            self.infos.put(' 提示：末端进水偏移填写不正确！')
            return False
        sun = int(float(sun)*10)
        waterOut = int(float(waterOut)*10)
        outdoor = int(float(outdoor)*10)
        waterIn = int(float(waterIn)*10)
        if sun < 0:
            sun = Utility.negative_1byte(sun)
        if waterOut < 0:
            waterOut = Utility.negative_1byte(waterOut)
        if outdoor < 0:
            outdoor = Utility.negative_1byte(outdoor)
        if waterIn < 0:
            waterIn = Utility.negative_1byte(waterIn)
        body = [self.dtuCom, self.deviceAdr, sun, waterOut, outdoor, waterIn]
        return Frame.create_frame(self.dtuIpArray, 0xA9, Utility.create_timestamp(), body)

    # 0xAA:时间设置
    def get_setting_date_cmd(self):
        import datetime
        i = datetime.datetime.now()
        body = [self.dtuCom, self.deviceAdr,i.year - 2000, i.month, i.day, i.weekday()+1, i.hour, i.minute, i.second]
        return Frame.create_frame(self.dtuIpArray, 0xAA, Utility.create_timestamp(), body)
    #############################################################
    #                          读取命令                         #
    #############################################################
    def get_reading_cmd_body(self):
        return [self.dtuCom, self.deviceAdr, 0, 0, 0, 0, 0, 0]

    def get_reading_cmd(self, order):
        body = self.get_reading_cmd_body()
        if order == 0x901:
            body[0] = 1
            order = 0x90
        elif order == 0x900:
            body[0] = 0
            order = 0x90
        elif order == 0x95:
            module = self.edtShowChangeModleNum.text()
            if module:
                body[2] = int(module)
            else:
                return False
        return Frame.create_frame(self.dtuIpArray, order, Utility.create_timestamp(), body)

    #############################################################
    #                          订阅消息                        #
    #############################################################
    def handle_remote_msg(self, frame):
        if Frame.check_frame(frame):
            order = frame[11]
            self.temp = frame[18:-3]
            if order == 0xA1:
                self.cmdA1 = True
            elif order == 0xA2:
                self.cmdA2 = True
            elif order == 0xA3:
                self.cmdA3 = True
            elif order == 0xA4:
                self.cmdA4 = True
            elif order == 0xA5:
                self.cmdA5 = True
            elif order == 0xA6:
                self.cmdA6 = True
            elif order == 0xA7:
                self.cmdA7 = True
            elif order == 0xA8:
                self.cmdA8 = True
            elif order == 0xA9:
                self.cmdA9 = True

    def handle_sys_frame(self):
        data = self.temp
        if data:
            self.edtShowBootStatus.setText(self.comBootStatus.itemText(data[2]&0xFF))
            self.edtShowWorkMode.setText(self.comWorkMode.itemText(data[3]&0xFF))
            self.edtShowSupplyHeat.setText(self.comSupplyHeat.itemText(data[4]&0xFF))
            self.edtShowDayMode.setText(self.comDayMode.itemText(data[5]&0xFF))
            self.edtShowMinReft.setText(str(data[6]&0xFF))
            self.edtShowMaxRefT.setText(str(data[7]&0xFF))

    def handle_alarm_frame(self):
        data = self.temp
        if data:
            self.edtShowAlarmTemp.setText(str(ctypes.c_short(Utility.byte2_to_int(data[2], data[3])).value))
            self.edtShowAlarmPressIn.setText(str(ctypes.c_short(Utility.byte2_to_int(data[4], data[5])).value))
            self.edtShowAlarmPressOut.setText(str(ctypes.c_short(Utility.byte2_to_int(data[6], data[7])).value))
            self.edtShowAlarmFlowIn.setText(str(ctypes.c_short(Utility.byte2_to_int(data[8], data[9])).value))
            self.edtShowAlarmFlowOut.setText(str(ctypes.c_short(Utility.byte2_to_int(data[10], data[11])).value))

    def handle_timetable_frame(self):
        data = self.temp
        if data:
            self.edtShowTimeTableNum.setText(str(data[2]&0xFF))
            self.edtReadTimeTable1.setText(str(data[3]&0xFF)+' 时 '+str(data[4]&0xFF)+' 分,模式：'+self.comTimeTable2.itemText(data[6]&0xFF))
            self.edtReadTimeTable1_2.setText(str(data[7]&0xFF)+' 时 '+str(data[8]&0xFF)+' 分,模式：'+self.comTimeTable2.itemText(data[10]&0xFF))
            self.edtReadTimeTable3.setText(str(data[11]&0xFF)+' 时 '+str(data[12]&0xFF)+' 分,模式：'+self.comTimeTable2.itemText(data[14]&0xFF))
            self.edtReadTimeTable4.setText(str(data[15]&0xFF)+' 时 '+str(data[16]&0xFF)+' 分,模式：'+self.comTimeTable2.itemText(data[18]&0xFF))
            self.edtReadTimeTable5.setText(str(data[19]&0xFF)+' 时 '+str(data[20]&0xFF)+' 分,模式：'+self.comTimeTable2.itemText(data[22]&0xFF))
            self.edtReadTimeTable6.setText(str(data[23]&0xFF)+' 时 '+str(data[24]&0xFF)+' 分,模式：'+self.comTimeTable2.itemText(data[26]&0xFF))
            self.edtReadTimeTable7.setText(str(data[27]&0xFF)+' 时 '+str(data[28]&0xFF)+' 分,模式：'+self.comTimeTable2.itemText(data[30]&0xFF))
            self.edtReadTimeTable8.setText(str(data[31]&0xFF)+' 时 '+str(data[32]&0xFF)+' 分,模式：'+self.comTimeTable2.itemText(data[34]&0xFF))
            self.edtReadTimeTable9.setText(str(data[35]&0xFF)+' 时 '+str(data[36]&0xFF)+' 分,模式：'+self.comTimeTable2.itemText(data[38]&0xFF))
            self.edtReadTimeTable10.setText(str(data[39]&0xFF)+' 时 '+str(data[40]&0xFF)+' 分,模式：'+self.comTimeTable2.itemText(data[42]&0xFF))

    def handle_judge_frame(self):
        data = self.temp
        if data:
            self.edtShowSolarTemp1.setText(str(ctypes.c_short(Utility.byte2_to_int(data[2], data[3])).value))
            self.edtShowSolarTemp2.setText(str(ctypes.c_short(Utility.byte2_to_int(data[4], data[5])).value))
            self.edtShowSolarTemp3.setText(str(ctypes.c_short(Utility.byte2_to_int(data[6], data[7])).value))
            self.edtShowSolarTemp4.setText(str(ctypes.c_short(Utility.byte2_to_int(data[8], data[9])).value))
            self.edtShowJudgeTemp1.setText(str(ctypes.c_short(Utility.byte2_to_int(data[10], data[11])).value))
            self.edtShowJudgeTemp2.setText(str(ctypes.c_short(Utility.byte2_to_int(data[12], data[13])).value))
            self.edtShowJudgeTemp3.setText(str(ctypes.c_short(Utility.byte2_to_int(data[14], data[15])).value))

    def handle_module_frame(self):
        data = self.temp
        if data:
            value = ctypes.c_byte(data[3]&0xFF).value
            self.edtShowChangeModleValue.setText(str(value/10))

    def handle_valve_interval_frame(self):
        data = self.temp
        if data:
            self.edtShowPinterval.setText(str(Utility.byte2_to_int(data[2], data[3])))
            self.edtShowFinterval.setText(str(Utility.byte2_to_int(data[4], data[5])))

    def handle_valve_logic_frame(self):
        data = self.temp
        if data:
            self.edtShowLogicTemp.setText(str(ctypes.c_byte(data[2]&0xFF).value))
            self.edtShowLogicTemp1.setText(str(ctypes.c_byte(data[3]&0xFF).value))
            self.edtShowLogicTemp2.setText(str(ctypes.c_byte(data[4]&0xFF).value))

    def handle_worktime_frame(self):
        data = self.temp
        if data:
            if data[2]&0xFF == 0:
                self.radioButton_5.setText('正常上班(√)')
                self.radioButton_2.setText('放假状态')
            else:
                self.radioButton_5.setText('正常上班')
                self.radioButton_2.setText('放假状态(√)')
            workH = data[3]&0xFF
            workM = data[4]&0xFF
            offH = data[5]&0xFF
            offM = data[6]&0xFF
            self.timeEdit.setTime(QTime(workH, workM))
            self.timeEdit_2.setTime(QTime(offH, offM))

    def handle_other_deviation_frame(self):
        data = self.temp
        if data:
            self.edtShowOtherSolar.setText(str(ctypes.c_byte(data[2]&0xFF).value/10))
            self.edtShowOtherWaterOut.setText(str(ctypes.c_byte(data[3]&0xFF).value/10))
            self.edtShowOtherTemp.setText(str(ctypes.c_byte(data[4]&0xFF).value/10))
            self.edtShowOtherWaterIn.setText(str(ctypes.c_byte(data[5]&0xFF).value/10))
