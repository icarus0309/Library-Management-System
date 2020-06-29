# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 13:28:32 2020

@author: 王钟毓
"""

def modUsrBook(allusr,allbook,usrname):
    allbookname = [row[0] for row in allbook]
    allbooknum = [row[2] for row in allbook]
    allusrname = [row[0] for row in allusr]
    idx = allusrname.index(usrname)
    flag = input('是否修改该用户的某一本书的借阅数量？按y确认，其余任意键跳过')
    if flag=='y':
        modbook = input('该书籍为：')
        tmp = allusr[idx]       #代指这个用户的信息条
        if modbook in tmp:
            if modbook in allbookname:
                idxbook = allbookname.index(modbook)    #这里要是能报错说明管理员太能作妖
                idx_in = tmp.index(modbook)
                booknum = int(allbooknum[idxbook])
                usrnum = int(tmp[idx_in+1])
                try:
                    modnum = int(input('修改数量为：'))
                except ValueError as e:
                    print('输入非法')
                    modnum = usrnum
                if 0< modnum <= booknum + usrnum:
                    allusr[idx][idx_in] = modnum
                    allbook[idxbook][2] = booknum + usrnum -modnum
                else:
                    print('修改数量不在合理范围内')
            else:
                flag2 = input('本图书馆关于这本书籍的信息已被您删除，\
                              是否清除该用户此条借阅信息？\ny确认/任意键无视')
                if flag2=='y':
                   idx_in = tmp.index(modbook)
                   tmp.pop(idx_in)
                   tmp.pop(idx_in)
                   allusr[idx] = tmp
                   print('-------------清除成功-------------')
        else:
            print('输入非法')
    flag = input('是否删除掉该用户某一本书的借阅信息？按y确认，其余任意键跳过')
    if flag=='y':
        modbook = input('该书籍为：')
        tmp = allusr[idx]       #代指这个用户的信息条
        if modbook in tmp:
            if modbook in allbookname:       #如果某本书已经被删除，但是之前有人借过
                idxbook = allbookname.index(modbook)
                idx_in = tmp.index(modbook)
                booknum = int(allbooknum[idxbook])
                usrnum = int(tmp[idx_in+1])
                tmp.pop(idx_in)
                tmp.pop(idx_in)
                print('-----------删除成功----------')
                newbooknum = booknum+usrnum
                allbook[idxbook][2] = newbooknum
            else:
                flag2 = input('本图书馆关于这本书籍的信息已被您删除，\
                              是否清除该用户此条借阅信息？\ny确认/任意键无视')
                if flag2=='y':
                   idx_in = tmp.index(modbook)
                   tmp.pop(idx_in)
                   tmp.pop(idx_in)
                   print('-----------删除成功----------')
            allusr[idx] = tmp
        else:
            print('输入非法')
    return allusr,allbook