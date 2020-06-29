# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 12:09:44 2020

@author: 王钟毓
"""
import csv


def vainErr(): # 用来清除usr表中的‘’,一般在用户借书和管理员查用户时使用
    with open('usrInfo.csv', 'r') as usrInfo:
        reader = csv.reader(usrInfo)
        allusr = [row for row in reader]
    for i in range(len(allusr)):
        tmp = allusr[i]
        while '' in tmp:  # 直到该行中所有的‘’被清除干净才会退出循环
            tmp.remove('')
        allusr[i] = tmp
    with open('usrInfo.csv', 'w', newline='') as usrinfo:  # 重新写入allusr
        writer = csv.writer(usrinfo)
        for i in allusr:
            writer.writerow(i) 
