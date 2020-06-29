# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 01:46:55 2020

@author: 王钟毓
"""
import getpass
import csv
import sys
sys.path.append("..") #要用到main.py，所以需要上一层路径也导入
import main

def register():        
    with open('usrInfo.csv','r+', newline='') as usrInfo:
        reader = csv.reader(usrInfo)
        allusr = [row for row in reader]
        allusrname = [row[0] for row in allusr]
        u_name = input('请输入新用户名称：')
        err_count = 0         #注册不合法次数多了之后，用来询问是否退出程序
        exitflag = ''
        while u_name in allusrname or u_name == 'admin' or u_name=='':
            #如果该名称已经被注册，那么需要重新写一个不同的名称
            #不能注册管理员帐号，同时也不能直接回车
            print('该用户名已被注册或不合法！请重新输入用户名称：')
            u_name = input('请输入用户名称:')
            err_count += 1
            if err_count>5:
                exitflag = input('已检测到您输入错误次数过多，是否退出注册？y确认/任意键无视')
                if exitflag=='y': #确认退出循环
                    break
        if exitflag=='y': #确认退回主函数
            main.main() 
        else:  #正常注册
            userpwd = getpass.getpass('请输入密码：')
            while userpwd =='': #不限制次数了吧，反正只要不一直输回车就行了
                userpwd = getpass.getpass('密码不得为空，请重新输入密码：')
            repwd = getpass.getpass('请再确认一遍密码：')
            while userpwd != repwd: #确认密码，不行就不隐身了
                userpwd = input('两次密码输入不符，请重新输入密码：')
                repwd = input('请再确认一遍密码：')
            print('注册成功~')
            with open('usrInfo.csv','a', newline='') as usrInfo:
                writer = csv.writer(usrInfo)      
                writer.writerow( [u_name,userpwd] ) 