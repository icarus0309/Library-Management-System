# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 13:46:13 2020

@author: 王钟毓
"""
import csv

def delUsr(allusr,usrname,idx):
    if usrname=='admin':    #如果管理员想删除管理员（当然这是不可能的）
        print('\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\
              \n熊孩子挺会玩儿哈？？？滚！！！\
              \n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    else:
        with open('bookInfo.csv','r+', newline='') as bookInfo:
            reader = csv.reader(bookInfo)
            allbook = [row for row in reader]
            allbookname = [row[0] for row in allbook]
        tmp = allusr[idx]   #从存储数据中找到要删的人
        tmplen = len(tmp)
        if tmplen>2:        #如果被删除的用户还有书没换，就自动把他的书全还上
            for i in range(2,tmplen,2):#列表从第三项到第tmplen项（步长2）全部为借书的书名
                tmpbookname = tmp[i]   #书名
                tmpbooknum = int(tmp[i+1]) #书数
                tmpidxbook = allbookname.index(tmpbookname) #该书在数据库中的位置
                tmpoldnum = int(allbook[tmpidxbook][2])     #该书的馆余数量
                tmpnewnum = tmpoldnum+tmpbooknum            #更新数据
                allbook[tmpidxbook][2] = tmpnewnum
        allusr.pop(idx)
        print('删除成功！')
    return allusr,allbook