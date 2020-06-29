# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 12:05:24 2020

@author: 王钟毓
"""
import csv

def viewUsr():
    with open('usrInfo.csv','r') as usrInfo:
        reader = csv.reader(usrInfo)
        allUsr = [row for row in reader]
    allusrname = [row[0] for row in allUsr]
    tmp = input('1.查看单个用户所有信息\n2.查看所有用户名\
                 \n3.查看书被借出情况\n4.查看全部用户全部信息(默认)')
    if tmp=='1':
        getusr = input('请输入需要查询的用户名')
        if getusr in allusrname:
            idx = allusrname.index(getusr)
            print(allUsr[idx])  #打印输入用户名对应的用户所有信息
        else:
            print('查无此人')
    elif tmp=='2':
        print(allusrname)   #打印所有用户名称
    elif tmp=='3':
        for tmp_i in allUsr[1:]:
            print('*************************\n用户名：',tmp_i[0])
            tmp_i.pop(0)
            tmp_i.pop(0)    #将用户名和密码接连去除
            count= 1        #count表示借的第几种书
            if len(tmp_i)==0:
                print('该用户暂无借书信息')
            else:
                while len(tmp_i)>1:
                    print('——————————————————————————\n借书信息',count,\
                          ':',tmp_i[0],'\t',tmp_i[1],'本')
                    tmp_i.pop(0)
                    tmp_i.pop(0) #接连去除当前书籍的名称和数量
                    count += 1
    else:
         print(allUsr) #打印所有信息