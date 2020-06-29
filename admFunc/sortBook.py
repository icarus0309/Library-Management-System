# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 11:12:30 2020

@author: 王钟毓
"""
import csv
import showBook
import SortFunc   #sort函数有5个，一起写在了SortFunc.py里

def sortBook():
    with open('bookInfo.csv','r+', newline='') as bookInfo:
         reader = csv.reader(bookInfo)
         allbook = [row for row in reader]
    print('当前顺序排列情况如下：')
    showBook.showBook()     #先展示一下当前排序
    tmp = input('请输入需要进行的排序类型：\n1.同作者就近重排\n2.调换两书籍位置\
          \n3.倒序重排\n4.随机重排\n5.短长名重排\n\n:')
    if tmp in ['1','2','3','4','5']:#分别按照对应的要求进行排序
        if tmp == '1':
            allbook_upd = SortFunc.sameAutSort(allbook)
        elif tmp == '2':
            allbook_upd = SortFunc.twoSort(allbook)
        elif tmp == '3':
            allbook_upd = SortFunc.resrSort(allbook)
        elif tmp == '4':
            allbook_upd = SortFunc.randSort(allbook)
        else:
            allbook_upd = SortFunc.lenSort(allbook)
        with open('bookInfo.csv','w', newline='') as bookInfo:
            #我之前在这里犯了个错误：还没排序完成就录入，自然会把之前的信息都丢掉
            writer = csv.writer(bookInfo)
            for i in allbook_upd:
                writer.writerow(i) 
        count = 1
        print('更新排序后的书籍信息为：')
        for i in allbook_upd:   #显示排序完成后的书籍信息表（大图书馆肯定不能这么干）
            print(count,i)
            count += 1
    else:
        print('输入非法，已退出排序操作')
        
        
        
        
        
        