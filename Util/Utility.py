#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
Created by Tan.Xing
Created date: 2019/01/03
Last edited: 2018/01/03
'''
from Config import Config

def show_log(info):
    if Config.SHOW_LOG:
        print(info)

def create_timestamp():
    import datetime
    i = datetime.datetime.now()
    now = []
    now.append(i.year-2000)
    now.append(i.month)
    now.append(i.day)
    now.append(i.hour)
    now.append(i.minute)
    now.append(i.second)
    return now

def int_to_2bytes(num):
    return (num >> 8) & 0xFF, num & 0xFF

def int2bytes(num):
    data = []
    data.append((num >> 8) & 0xFF)
    data.append(num & 0xFF)
    return data

def int4bytes(num):
    data = []
    data.append((num >> 24) & 0xFF)
    data.append((num >> 16) & 0xFF)
    data.append((num >> 8) & 0xFF)
    data.append(num & 0xFF)
    return data

def byte2_to_int(h, l):
    return (h &0xFF)<< 8 | (l&0xFF)

def byte4_to_int(b1, b2, b3, b4):
    return (b1 &0xFF)<< 24 |(b2 &0xFF)<< 16 |(b3 &0xFF)<< 8 | (b4&0xFF)

def negative_1byte(num):
    return int(hex(num & 0xFF), 16)

def negative_2byte(num):
    return int(hex(num & 0xFFFF), 16)

def negative_4byte(num):
    return int(hex(num & 0xFFFFFF), 16)