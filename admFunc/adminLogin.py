# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 10:28:39 2020

@author: P_Wan
"""
import sys
import getpass          #用来隐藏密码
sys.path.append("..")   #将上一层文件路径导入
import admFunc          #导入上一层路径下的admFunc.py文件


def login():            #管理员登录
    err_count = 0
    while err_count<5:  #五次登录失败退出程序
        print('请输入管理员帐号：',end='')
        username=input()
        password=getpass.getpass('请输入管理员密码：')
        if [username,password] == ['admin','admin']:
            print('成功登入管理员界面,请选择接下来的操作：')
            admFunc.mainFuncAdm() #登录成功即开始调用管理员程序
        else:
            err_count += 1
            print('\n账户名或密码错误,请重新输入：' )
    print('登入5次失败，自动退出程序')
    sys.exit(0)  #也可以改成退回主程序