# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 23:56:14 2020

@author: 王钟毓
"""
import sys
import main

sys.path.append(r'.\usrFunc')  # 导入路径1
import broBook  # 导入路径1下需要用到的py文件
import modPwd
import returnBook
import showAcc

sys.path.append(r'.\admFunc')  # 导入路径2
import showBook  # 导入路径2下需要用到的py文件
import findBook


# 需要导入文件名称

def mainFuncUsr(username):
    while True:
        print('\n***************************************')
        print('********  借阅书籍--------1  **********')
        print('********  归还书籍--------2  **********')
        print('********  查找书籍--------3  **********')
        print('********  查看账户信息----4  **********')
        print('********  查看所有书籍----5  **********')
        print('********  修改密码--------6  **********')
        print('********  返回主界面------7  **********')
        print('********  退出--------任意键  **********')
        print('***************************************\n')
        v = input('请输入对应的数字：\n')
        if v == '1':
            broBook.broBook(username)
            input('任意键继续')
        elif v == '2':
            returnBook.returnBook(username)
            input('任意键继续')
        elif v == '3':
            tmp = input('请输入要查找的书籍名或作家名：')
            findBook.findBook(tmp)
            input('任意键继续')
        elif v == '4':
            showAcc.showAcc(username)
            input('任意键继续')
        elif v == '5':
            showBook.showBook()
            input('任意键继续')
        elif v == '6':
            modPwd.modPwd(username)
            input('任意键继续')
        elif v == '7':
            main.main()
        else:
            sys.exit(0)





















