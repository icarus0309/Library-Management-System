# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 11:08:41 2020

@author: 王钟毓
"""
import csv

def findBook(tmp):
    with open('bookInfo.csv','r+', newline='') as bookInfo:
         reader = csv.reader(bookInfo)
         allbook = [row for row in reader]
    allbookname = [row[0] for row in allbook]
    allauthor = [row[1] for row in allbook]
    flag = False
    for k in allbookname:       #k表示每一项书名，如果它包含了tmp自然也可以打印
        if tmp in k and tmp !='':  #''这个东西坏得很，谁都有，一键回车全员打印可还行
            tmpInfo = ['书名：\t','作者：\t','馆余数目:\t']
            idx = allbookname.index(k)
            print('%---------------------------------%')
            for i in range(3):  #tmpInfo有三样信息
                print('\t',tmpInfo[i],allbook[idx][i],\
                      '\t\t\n|---------------------------------|')
            print('\n')
            flag = True
    if tmp in allauthor and tmp != '': #作者这里就省掉了关键字功能了吧，觉得没必要
        print('\n\t书名\t','作者\t','馆余数目\t'\
              '\n|----------------------------------------|')
        while tmp in allauthor:           #作者信息中包含输入关键字
            idx = allauthor.index(tmp)
            for i in range(3):
                print('\t',allbook[idx][i],end='')
            allbook.remove(allbook[idx])
            allauthor.remove(allauthor[idx])
            print('\n')
        flag = True
    if not flag:
         print('\n馆内尚无该书/该作者的书!')