# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 01:50:34 2020

@author: 王钟毓
"""

import csv
import sys
import getpass
sys.path.append("..") #因为需要用到usrFunc.py，所以需要导入上一层路径
import usrFunc

def login():
    with open('usrInfo.csv', 'r+', newline='') as usrInfo:#导入用户信息表
        reader = csv.reader(usrInfo)
        allusr = [row for row in reader]
        allusrname = [row[0] for row in allusr]
        allusrPwd = [row[1] for row in allusr]
    err_count = 0
    while err_count<5: #登录5次失败自动退出
        print('请输入用户名：',end='')
        username = input()
        print('请输入用户密码：',end='')
        password=getpass.getpass() #隐藏密码
        if username in allusrname[1:] and password in allusrPwd[1:]:
            print('登录成功！')
            usrFunc.mainFuncUsr(username) #进入用户主函数
        else:
            err_count += 1
            print('\n用户名或密码错误，或登陆帐号为管理员帐号，请重新登陆')
    print('登录5次失败，自动退出程序')