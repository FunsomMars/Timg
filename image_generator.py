#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2019-07-23 21:40
# @Author : Simon Meng
# @Site :
# @File : image_generator.py
# @Software: PyCharm

import timg.img_gen as tm
import argparse

parser = argparse.ArgumentParser(description='A python program for generating various images')
parser.add_argument('height', type=int, help='The height of your image')
parser.add_argument('width', type=int, help='The width of your image')
parser.add_argument('folder', type=str, help='The folder name for storing your image')
type_list = ['align', 'purity', 'crosstalk', 'responsetime', 'checkerboard', 'flicker', 'grayscale', 'funny']
parser.add_argument('type', type=str, choices=type_list, help='The type of your image to generate')
parser.add_argument('-ppi', default=401, type=int,
                    help='The ppi of your image, the default value is 401,'
                         ' it should be provided when generating crosstalk image')
parser.add_argument('-gl', default=[0, 128, 255], type=list,
                    help='The gray scale list for generating images, the default value is [0, 128, 255]')
args = parser.parse_args()
gen = tm.Timg(args.height, args.width, args.ppi, args.gl, args.folder)
function_list = [gen.align, gen.purity, gen.crosstalk, gen.responsetime, gen.checkerboard, gen.flicker, gen.grayscale,
                 gen.funny]
function_map = dict(zip(type_list, function_list))
if args.type:
    func = function_map[args.type]
    func()
