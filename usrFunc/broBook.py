# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 01:51:16 2020

@author: 王钟毓
"""
import csv
import sys
sys.path.append("../admFunc")
import vainErr

def broBook(username):
    vainErr.vainErr()         #清除冗余的‘’
    #借书操作需要两张表的信息都录入进来
    with open('bookInfo.csv','r') as bookInfo:
        reader = csv.reader(bookInfo)
        allbook = [row for row in reader]
    allbookname = [row[0] for row in allbook]
    allnum = [row[2] for row in allbook]
    allnum =[int(i) for i in allnum]
    with open('usrInfo.csv','r') as usrInfo:
        reader = csv.reader(usrInfo)
        allusr = [row for row in reader]
        allusrname = [row[0] for row in allusr]
    wanabook = input('请输入您想要借阅的书籍名称：') #用户想要借的书
    if wanabook in allbookname: #如果该书存在
        idx = allbookname.index(wanabook)
        idx2 = allusrname.index(username)
        print('该书当前信息为：\n\n书名:',allbookname[idx],\
              '\n作者：',allbook[idx][1],\
              '\n馆余数目：',allnum[idx],\
              '\n\n')                   #将该书的所有馆存信息展示给该用户
        try:
            wananum = int(input('请输入您想借阅的本数：'))
        except ValueError as e:
            print('请输入正整数！')
            wananum = 0                 #异常则按0处理
        tmp1 = allusr[idx2]
        if 0 < wananum <= int(allbook[idx][2]):
            #上面的int一般是不需要try的，因为在写入参数的时候已经try过了
            #除非人为进入csv表修改该参数为非整形变量
            allnum[idx] -= wananum
            allbook[idx][2] = allnum[idx]
            if wanabook not in tmp1:              #如果用户还没借过这本书
                tmp1.append(wanabook)
                tmp1.append(wananum)
            else:                                 #如果用户已经借过这本书
                tmp1_1 = tmp1.index(wanabook)+1   #书名后面即数量的位置
                tmp1[tmp1_1] = int(tmp1[tmp1_1]) + wananum    #更新该位置的数量                

            allusr[idx2]= tmp1
            print('*************借阅成功！祝您阅读愉快~************')
            with open('bookInfo.csv','a',newline='') as bookinfo:
                writer = csv.writer(bookinfo)
                for i in allbook:
                    writer.writerow(i)
            with open('usrInfo.csv','w',newline='') as usrinfo:
                writer = csv.writer(usrinfo)
                for i in allusr:
                    writer.writerow(i)                     
        else:
            print('您所借书的数目不太合适哦，详细查询一下吧—_—|||')
    else:
        print('很遗憾，馆藏无此书！')