# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 09:21:59 2020

@author: 王钟毓
"""
import csv

def modPwd(username):    
    with open('usrInfo.csv','r') as usrInfo:
        reader = csv.reader(usrInfo)
        allusr = [row for row in reader]
    allusrname = [row[0] for row in allusr]
    allpwd = [row[1] for row in allusr]
    if username not in allusrname:
        #一般这情况不会出现，除非在登入的同时管理员也登入了并修改了用户信息表
        print('可能是由于管理员的骚操作导致系统崩溃了，您暂时无法正常运行程序')
    else:
        idx = allusrname.index(username)
        err = 0
        safe = input('请输入原密码：') #这里就不隐身了吧
        
        while err<5:
            if safe == allpwd[idx]:
                newpwd = input('请输入新密码：')
                allusr[idx][1] = newpwd #在对应位置修改密码
                with open('usrInfo.csv','w',newline='') as usrinfo:
                    writer = csv.writer(usrinfo) #写入新密码
                    for i in allusr:
                        writer.writerow(i)
                break
            else:
                err += 1 #表示错输入次数，并用来提醒剩余次数
                if err<5:
                    print('原密码输入错误，您还有',5-err,'次机会重新输入：')
                    safe = input()
                else:
                    print('5次输入均错误，修改密码失败')
                    break
