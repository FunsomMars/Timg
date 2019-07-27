#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 
# @Time : 2019-07-23 22:47 
# @Author : Simon Meng 
# @Site :  
# @File : mkdir.py 
# @Software: PyCharm

import os


# Make a folder under the current path
def mkdir(path):
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)
