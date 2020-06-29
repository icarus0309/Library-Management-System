# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 09:20:20 2020

@author: 王钟毓
"""
import csv

def showAcc(username):    
    with open('usrInfo.csv','r+', newline='') as usrInfo:
         reader = csv.reader(usrInfo)
         allusr = [row for row in reader]
    allusrname = [row[0] for row in allusr]
    if username in allusrname:
        idx = allusrname.index(username)
        tmp = allusr[idx]
        print('用户名\t :  ',tmp[0])
        tmp.pop(0)     #删除用户名   
        tmp.pop(0)     #删除用户密码
        for i in range(len(tmp)):
            if i%2==0:  #i为偶数，则打印名称
                print('----------------------------------\
                      \n借书信息',int(i/2+1),'为：',tmp[i],end='\t')
            else:       #i为奇数，则打印数目
                print(tmp[i],'本')
    else:
        print('当前用户不存在')
