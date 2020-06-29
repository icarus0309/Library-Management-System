# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 12:06:55 2020

@author: 王钟毓
"""
#首先导入必要的文件，因为都在同一文件夹下，所以不需要扩增路径
import csv
import modUsrBook
import delUsr
import vainErr

def modUsr():
    vainErr.vainErr() #如main中所提到的，用来清除用户信息表中可能存在的‘’
    #由于修改用户信息可能造成书籍流通变动，所以需要同时导入两个数据文件
    with open('usrInfo.csv','r') as usrInfo:
        reader = csv.reader(usrInfo)
        allusr = [row for row in reader]
    with open('bookInfo.csv','r+', newline='') as bookInfo:
        reader = csv.reader(bookInfo)
        allbook = [row for row in reader]
    allusrname = [row[0] for row in allusr]
    usrname = input('请输入需要修改信息的用户名：')
    if usrname in allusrname:
        idx = allusrname.index(usrname) #找到该用户在用户信息表中的位置
        print('该用户所有信息为：',allusr[idx]) #展示该用户的信息条
        tmp = input('1.修改该用户的用户名\n2.修改该用户的密码\
                     \n3.修改该用户的借书信息\n4.删除该用户（该用户所借书籍自动归档）')
        if tmp in ['1','2','3','4']:
            if tmp =='1':
                new_name=input('该用户名修改为：')
                if new_name in allusrname:    #如果新名字已经存在，则跳过
                    print('新用户名已被注册！此次修改失败')
                else:
                    allusr[idx][0] = new_name #新名字按下标写入
            elif tmp =='2':
                new_pwd =input('该用户密码修改为：')
                allusr[idx][1] = new_pwd   #新密码按下标写入，但密码重复没关系
            elif tmp=='3':      #修改用户的借书信息代码量庞大，故另起一个函数写之
                allusr,allbook = modUsrBook.modUsrBook(allusr,allbook,usrname)
            else:               #删除用户的代码量也挺大的，因为用户借过的书也得自动归还
                allusr,allbook = delUsr.delUsr(allusr,usrname,idx)
            #将改好的两表分别重新录入
            with open('usrInfo.csv','w', newline='') as usrInfo:
                writer = csv.writer(usrInfo)
                for i in allusr:
                    writer.writerow(i)
            with open('bookInfo.csv','w', newline='') as bookInfo:
                writer = csv.writer(bookInfo)
                for i in allbook:
                    writer.writerow(i)
        else:
            print('未检测到合法输入，已自动退出')
    else:
        print('查无此人')