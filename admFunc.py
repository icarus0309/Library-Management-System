# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 13:44:42 2020

@author: 王钟毓
"""
import sys
import main  # 因为可能需要返回主函数，所以主函数也得导入进来

sys.path.append(r'.\admFunc')  # 导入必要文件的路径
import addBook  # 导入所需要的py文件
import delBook
import findBook
import modBook
import sortBook
import showBook
import viewUsr
import modUsr


def mainFuncAdm():
    while True:
        print('\n***************************************')
        print('********  增加书籍--------1  **********')
        print('********  删除书籍--------2  **********')
        print('********  查找书籍--------3  **********')
        print('********  修改书籍--------4  **********')
        print('********  排列书籍--------5  **********')
        print('********  查看所有书籍----6  **********')
        print('********  查看用户信息----7  **********')
        print('********  修改用户信息----8  **********')
        print('********  返回主界面------9  **********')
        print('********  退出-------任意键  **********')
        print('***************************************\n')
        v = input('请输入对应的数字：\n')
        if v == '1':
            addBook.addBook()  # 调用addBook.py中的addBook()方法
            input('按任意键继续')
        elif v == '2':
            delBook.delBook()
            input('按任意键继续')
        elif v == '3':
            tmp = input('请输入要查找的书籍名或作家名：')
            findBook.findBook(tmp)  # findBook方法需要参数输入
            input('按任意键继续')
        elif v == '4':
            modBook.modBook()
            input('按任意键继续')
        elif v == '5':
            sortBook.sortBook()
            input('按任意键继续')
        elif v == '6':
            showBook.showBook()
            input('按任意键继续')
        elif v == '7':
            viewUsr.viewUsr()
            input('按任意键继续')
        elif v == '8':
            modUsr.modUsr()
            input('按任意键继续')
        elif v == '9':
            main.main()
        else:
            sys.exit(0)

