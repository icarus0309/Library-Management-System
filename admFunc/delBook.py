# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 10:38:58 2020

@author: 王钟毓
"""
import csv


def delBook():
    with open('bookInfo.csv', 'r+', newline='') as bookInfo:
        reader = csv.reader(bookInfo)
        allbook = [row for row in reader]
    # 只要reader里的信息提取出来了，allbookname这一行放在with里外都可以
    allbookname = [row[0] for row in allbook]
    while True:
        bookname = input('请输入要删除的书籍名称：')
        if bookname in allbookname:  # 检查需要删除的书是否在库存中
             idx = allbookname.index(bookname)
             remain = [i for i in range(len(allbook))]
             remain.remove(idx)      # remain表示剩余书籍
             with open('bookInfo.csv', 'w', newline='') as bookInfo:
                writer = csv.writer(bookInfo)
                for i in remain:
                    writer.writerow(allbook[i])
             print('----------删除完成！--------')
        else:
             print('----------该书不存在！---------')
        flag = input('是否继续删除？y继续/任意键退出')
        if flag == 'y':               # 是否继续删除，是的话不退出循环
            continue
        else:
            break
