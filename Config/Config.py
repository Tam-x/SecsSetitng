#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
Created by Tan.Xing
Created date: 2019/01/03
Last edited: 2018/01/03
'''
VERSION = '1.0.3'

MQTT_BROKER = None
MQTT_PORT = None
MQTT_USER = 'wmstest'
MQTT_CODE = 'wmstest1234'

MQTT_DOWN_TOPIC = 'dtu/down/secs/yarlung/{}'
MQTT_UP_TOPIC = 'dtu/up/secs/{}/remote'

MQTT_CLIENT = 'secs-desktoptool-'
SHOW_LOG = True

BTN_CLICK_INTERVAL = 1000
PWD_INPUT_INTERVAL = 15 * 60