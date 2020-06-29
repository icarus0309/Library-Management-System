# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 11:28:26 2020

@author: 王钟毓
"""
import csv

def showBook(): #展示所有书籍
    with open('bookInfo.csv','r+', newline='') as bookInfo:
         reader = csv.reader(bookInfo)
         allbook = [row for row in reader]
    print('***************************\n序号\t书名\t作者\t馆存数量')
    count = 1
    for i in allbook: #按行展示，count用来表示序号
        print(count,i)
        count += 1