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
