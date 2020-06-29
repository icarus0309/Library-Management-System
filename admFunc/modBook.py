# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 11:10:24 2020

@author: P_Wan
"""
import csv

def modBook():
    with open('bookInfo.csv','r+', newline='') as bookInfo:
         reader = csv.reader(bookInfo)
         allbook = [row for row in reader]
    allbookname = [row[0] for row in allbook]
    allauthor = [row[1] for row in allbook]
    #前面和之前一样，用while true意图在于能够持续进行修改，退出则可以break
    while True:
        tmp = input('需要修改的书籍名称为？\n')
        if tmp in allbookname:  #判断输入书名是否存在
            idx = allbookname.index(tmp)
            print('\n该书当前信息为：\n********************\
                  \n书名:',allbookname[idx],\
                  '\n作者：',allauthor[idx],\
                  '\n馆余数目：',allbook[idx][2],\
                  '\n********************\
                  \n\n请输入对应序号进行书籍属性修改：\
                  \n1.书名\n2.作者\n3.馆余数目\n4.退出此次修改')
            tmp=input()
            if tmp in ['1','2','3','4']:
                if tmp == '1': #改书名
                    new_name = input('请输入新书名：')
                    allbook[idx][0],allbookname[idx] = new_name,new_name
                elif tmp == '2': #改作者
                    new_aut = input('请输入新作者：')
                    allbook[idx][1],allauthor[idx] = new_aut,new_aut
                elif tmp == '3': #改馆存数量
                    try:         #处理异常
                        tmp_booknum = int(input('更新馆存数量为：'))
                    except ValueError as e:
                        print('请输入正整数！')
                        tmp_booknum = allbook[idx][2]  #如果异常，按原数目输入
                    allbook[idx][2] = tmp_booknum      #写入修改后的书籍数目
                else:
                    continue    #不做任何修改直接进行下一轮循环
            else:
                print('输入字符无效，修改失败')
            print('修改后为：\t',allbook[idx])
            with open('bookInfo.csv','w', newline='') as bookInfo:
                writer = csv.writer(bookInfo)
                for i in allbook:
                    writer.writerow(i)
        else:       #如果输入书名不存在
            print('\n*********************\n\t查无此书!')
        flag = input('是否继续修改？y继续/任意其他键退出')
        if flag != 'y': #用以退出循环
            break