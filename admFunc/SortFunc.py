# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 11:43:36 2020

@author: 王钟毓
"""
import random

#同作者就近重排
def sameAutSort(allbook): #以后尝试用哈希表改进这里
    allauthor = [row[1] for row in allbook] #数据表的第二列存储作者信息
    newallbook = [] #newallbook是用来存储排序完毕的书籍信息表
    tmp = allbook.copy() #深拷贝（我闲的）
    for i in allauthor:
        idx = [] #用来存储相同作者书籍的下标
        for j in range(len(tmp)): #遍历表中所有的作者
            if tmp[j][1]==i:
                idx.append(j) #作者相同，idx存储+1
        for j in range(len(idx)):
            newallbook.append(tmp[idx[j]]) #将当前作者的全部书籍写入newallbook
        #接下来，从tmp里清除掉已经录入newallbook的作者
        delcount = 0 #每删除一次，元素下标就要往前缩进一位，因此用delcount表缩进次数
        for j in idx:
            if tmp[j-delcount][1] == i: #当前位置上的作者是否等于要找的作者
                tmp.remove(tmp[j-delcount]) #清除操作
                delcount += 1
    return newallbook

#调换两书籍位置    
def twoSort(allbook): 
    allbookname  = [row[0] for row in allbook]
    str1 = input('请输入需要交换的书籍名称\n第一本：')
    str2 = input('第二本：')
    if str1 in allbookname and str2 in allbookname:
        idx1 = allbookname.index(str1) #根据两个位置下标交换书籍位置
        idx2 = allbookname.index(str2)
        tmp = allbook[idx1]
        allbook[idx1] = allbook[idx2]
        allbook[idx2] = tmp
        return allbook
    else:
        print('您可能输入了本馆不存在的书籍，您可以尝试查询本馆所有书籍信息')
        return allbook

#倒序重排          
def resrSort(allbook):
    label = [i for i in range(len(allbook))] #label即0,1,2,...直到allbook的长度
    zipbook = [(x,y) for x,y in zip(label,allbook)] #用zip将allbook和label绑定
    sortedbook = [y for _,y in zipbook[::-1]] #将zipbook根据label倒序重排
    return sortedbook #allbook也随之重排，上一行中的y即指代allbook
 
#随机重排
def randSort(allbook):        
    label = [i for i in range(len(allbook))]
    random.shuffle(label) #将0到长度的数字打乱顺序
    zipbook = [(x,y) for x,y in zip(label,allbook)] #其余同上
    sorted_zip = sorted(zipbook)
    sortedbook = [y for _,y in sorted_zip]
    return sortedbook
 
#短长名重排
def lenSort(allbook):
    allbookname  = [row[0] for row in allbook]
    length = [len(i) for i in allbookname] #和倒序重排相同，将label换成length即可
    zipbook = [(x,y) for x,y in zip(length,allbook)]
    sorted_zip = sorted(zipbook)
    sortedbook = [y for _, y in sorted_zip]
    return sortedbook   