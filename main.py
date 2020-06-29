# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 13:36:14 2020

没什么太大的问题，主要有这么几个小问题：

    1.我不知道修改了某一项之后的用户或书籍信息如何写入源文件，目前似乎没找到好的方法，只好每次
      都在with open中使用‘w’，即全部推翻重写，小文件这样做可以，数据量庞大估计会吃不消
    2.有时候前人借了书，新注册的用户为了强行匹配长度，会出现'',''的情况，目前也没找到原因在哪
      只好特意写了vainErr.py放在admFunc文件夹下

@author: 王钟毓
"""
import sys
sys.path.append(r'.\usrFunc')  # 导入必要文件的路径
sys.path.append(r'.\admFunc')
import login  # 导入所需要的py文件
import register
import adminLogin


def main():  # 主函数开始运行
    while True:
        print('\n\n      **********************')
        print('      *欢迎来到图书管理系统*')
        print('      **********************\n')
        print('**********************************')
        print('******   用户登录------- 1  ******')
        print('******   用户注册------- 2  ******')
        print('******   管理员登录----- 3  ******')
        print('******   退出-------任意键  ******')
        print('**********************************\n')
        i = input('请输入对应的数字：')
        if i == '1':
            login.login()  # 调用login.py中的login()方法
        elif i == '2':
            register.register()  # 同上
        elif i == '3':
            adminLogin.login()  # 同上
        else:
            sys.exit(0)  # 退出程序


if __name__ == '__main__':
    main()


