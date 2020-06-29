# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 10:30:18 2020

@author: 王钟毓
"""
import csv
def addBook():
    #为了避免文件不存在，抢先定义好再说（with open参数为'a'可以定义不存在的文件）
    with open('bookInfo.csv', 'a', newline='') as bookInfo:
        pass
    #flag = True             #标志用以判断是否为空文件
    with open('bookInfo.csv','r+', newline='') as bookInfo:
        reader = csv.reader(bookInfo)
        allbook = [row for row in reader]
    if allbook != [[]]:
        #判断文件是否为空，一来空文件写入更方便，二来为了避免allbookname命名报错
        #flag = False
        allbookname = [row[0] for row in allbook]
        bookname = input('请输入书名：')
        try:            #防止输入不为正整数
            booknum = int(input('请输入要增/减的数量：'))
        except ValueError as e:
            print('请输入正整数！')
            booknum = 0     #如果输入不为整数，则按照0本添加
        writer = csv.writer(bookInfo)
        if bookname not in allbookname:  #如果图书馆尚无该书籍，则添加一本新书
            bookaut = input('请输入作者：')
            with open('bookInfo.csv','a', newline='') as bookInfo:
                #将新书的三项信息写入csv文件---1.书名，2.作者，3.数量
                writer = csv.writer(bookInfo)
                writer.writerow( [bookname,bookaut,booknum] )
            print('----------添加书籍成功！---------'\
                  '\n当前该书籍的 名称 作者 馆存数量 为：',[bookname,bookaut,booknum])
        else:
            #如果图书馆中已经有了该书，那么只能添加数量了
            #这个数字可以为负值，相当于变相地删除书籍，只要别使馆余为负就好
            idx = allbookname.index(bookname)
            tmp = int(allbook[idx][2])  #tmp表示这本书当前图书馆里已经有的数量
            print('当前该书籍数量为：', tmp, end=' ')
            tmp += booknum              #更新图书馆已有数量
            print('添加后的数量为：', tmp)
            if tmp < 0:                   #不能使馆余数量为负数
                print('错误操作！此次添加无效！')
            else:
                allbook[idx][2] = tmp   #其实不管是int还是str类型，录入后都是str
                with open('bookInfo.csv', 'w', newline='') as bookInfo:
                    writer = csv.writer(bookInfo)
                    for i in allbook:
                        writer.writerow(i)
                print('----------同名书籍添加/移除成功！--------')
    else:
        #如果文件为空，则执行这个模块,因为空文件下
        #allbookname = [row[0] for row in allbook]这行代码无法运行
        bookname = input('请输入书名：')
        booknum = int(input('已有该书，请输入要增/减的数量：'))
        bookaut = input('请输入作者：')
        with open('bookInfo.csv','w', newline='') as bookInfo:
            writer = csv.writer(bookInfo)
            writer.writerow( [bookname,bookaut,booknum] )
            print('----------添加书籍成功！---------')