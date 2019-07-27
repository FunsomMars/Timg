#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 
# @Time : 2019-07-23 21:02 
# @Author : Simon Meng 
# @Site :  
# @File : list2int.py 
# @Software: PyCharm


# Convert items to integer
def list2int(lis):
    def fn(li):
        li[0] = int(li[0])
        li[1] = int(li[1])
        return li
    lists = list(map(fn, lis))
    return lists
