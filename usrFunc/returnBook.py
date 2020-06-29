# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 01:52:09 2020

@author: 王钟毓
"""
import csv

def returnBook(username):
    #还书操作需要对两张表都进行修改
    with open('bookInfo.csv','r') as bookInfo:
        reader = csv.reader(bookInfo)
        allbook = [row for row in reader]
    allbookname = [row[0] for row in allbook]
    allnum = [row[2] for row in allbook] #存储数量
    allnum =[int(i) for i in allnum]     #将字符转化为字符串
    with open('usrInfo.csv','r') as usrInfo:
        reader = csv.reader(usrInfo)
        allusr = [row for row in reader]
    allusrname = [row[0] for row in allusr]
    rtbook = input('请输入您想要归还的书籍名称：')
    idx1 = allusrname.index(username)     #idx1表示用户在用户表的位置
    tmp1 = allusr[idx1]                   #tmp1表示当前用户信息条
    if rtbook in allbookname:             #如果该书确实在馆存内
        idx2 = allbookname.index(rtbook)  #idx2表示要换的书在书籍表的位置
        tmp2 = int(allbook[idx2][2])      #tmp2表示该书的馆余数量
        if rtbook in tmp1:                #如果用户确实有借过该书
            tmp1_1 = tmp1.index(rtbook)+1 #'借阅数量'的位置='书籍名称'位置+1
            ownnum = int(tmp1[tmp1_1])    #将借阅数量转化为整形
            try:
                rtnum = int(input('请输入您想要归还的本数：'))
            except ValueError as e:
                print('请输入正整数！')
                rtnum = 0               #归还数目不为整形时按0处理
            if 0 < rtnum <= ownnum:     #如果输入的数值合法
                ownnum -= rtnum         #用户拥有数目减去归还数目
                tmp2 += rtnum           #馆余数目加上归还数目
                print('**********归还成功+_+!************')
                if ownnum == 0:   #如果用户拥有数目为0，删除该书借阅信息                    
                    tmp1.pop(tmp1_1-1)  #删除书籍名称
                    tmp1.pop(tmp1_1-1)  #删除借阅数量
                    allusr[idx1] = tmp1 #更新用户信息            
                    allbook[idx2][2] = tmp2 #更新书籍数目信息
                else:             #如果用户拥有数目不为0，直接录入
                    allbook[idx2][2] = tmp2 #依旧要更新书籍数目信息
                    allusr[idx1][tmp1_1] = ownnum 
                with open('bookInfo.csv','w',newline='') as bookinfo:
                    writer = csv.writer(bookinfo)
                    for i in allbook:
                        writer.writerow(i)
                with open('usrInfo.csv','w',newline='') as usrinfo:
                    writer = csv.writer(usrinfo)
                    for i in allusr:
                        writer.writerow(i)
            else:
                print('您的输入在您实际借阅的数目范围之外！')
        else:
            print('您尚未借阅该书，无需归还')                    
    else:
        print('该书籍不存在或已被管理员清除！将自动为您清除此条借阅信息')
        if rtbook in tmp1:
            #要考虑到一种特殊情况：用户借了某书后管理员却将该书在图书馆的信息删除了，
            #那么用户在归还这本书的时候将会自动清除掉这本书的借阅信息
            tmp1_1 = tmp1.index(rtbook)
            tmp1.pop(tmp1_1)
            tmp1.pop(tmp1_1)