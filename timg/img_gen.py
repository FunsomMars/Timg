#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 
# @Time : 2019-05-10 14:32 
# @Author : Simon Meng 
# @Site :  
# @File : optical_test.py
# @Software: PyCharm

import math
import numpy as np
import imageio
import matplotlib.pyplot as plt
from mkdir import mkdir
from list2int import list2int


class Timg(object):
    # Property initializing
    def __init__(self, image_h, image_v, filename, ppi=401, gl=(0, 128, 255)):
        self.image_h = image_h
        self.image_v = image_v
        self.ppi = ppi
        self.gl = gl
        self.filename = filename
        mkdir(filename)

    # A cross in center, for alignment
    def align(self):
        image_h = self.image_h
        image_v = self.image_v
        filename = self.filename
        image = np.zeros((image_h, image_v, 3), dtype='uint8')
        image[:, math.ceil(image_v / 2), 2] = 255
        image[math.ceil(image_h / 2), :, 2] = 255
        plt.imsave(filename + '/image_align.png', image)

    # White, red, green and blue, with 255 gray scale
    def purity(self):
        image_h = self.image_h
        image_v = self.image_v
        filename = self.filename
        for i in range(5):
            image = np.zeros((image_h, image_v, 3), dtype='uint8')
            color_dict = {0: '_red', 1: '_green', 2: '_blue', 3: '_black', 4: '_white'}
            if i <= 2:
                image[:, :, i] = 255
            elif i == 3:
                image[:, :, :] = 0
            else:
                image[:, :, :] = 255
            plt.imsave(filename + '/image%s.png' % color_dict[i], image)

    # Crosstalk
    def crosstalk(self):
        image_h = self.image_h
        image_v = self.image_v
        ppi = self.ppi
        filename = self.filename
        inch = 25.4  # 1inch equals to 25.4mm
        edge = math.ceil(ppi / inch)  # pixels per mm
        bias = edge * 9  # The moving rectangle moves 9mm per step

        def image_hori(colum_min, colum_max, gray, height, width):
            image = np.zeros((height, width, 3), dtype='uint8') + 128
            for i in range(height):
                for j in range(width):
                    if i < math.ceil(height / 3) or i > math.ceil(height * 2 / 3):
                        if colum_min <= j < colum_max:
                            image[i, j] = gray
                    else:
                        break
            return image

        def image_vert(row_min, row_max, gray, height, width):
            image = np.zeros((height, width, 3), dtype='uint8') + 128
            for i in range(height):
                for j in range(width):
                    if row_min <= i < row_max:
                        if j < math.ceil(width / 3) or j > math.ceil(width * 2 / 3):
                            image[i, j, :] = gray
                    else:
                        break
            return image

        l_bias = [[image_v / 2 - bias, image_v * 5 / 6 - bias], [image_v / 2 + bias, image_v * 5 / 6 + bias],
                  [image_v / 6 + bias, image_v / 2 + bias], [image_v / 6 - bias, image_v / 2 - bias]]
        v_bias = [[image_h / 2 - bias, image_h * 5 / 6 - bias], [image_h / 2 + bias, image_h * 5 / 6 + bias],
                  [image_h / 6 + bias, image_h / 2 + bias], [image_h / 6 - bias, image_h / 2 - bias]]
        l_bias = list2int(l_bias)
        v_bias = list2int(v_bias)

        k = 0
        for l, m in l_bias:
            sq_black = image_hori(l, m, 0, image_h, image_v)
            sq_white = image_hori(l, m, 255, image_h, image_v)
            plt.imsave(filename + '/crosstalk_black_%s.png' % k, sq_black)
            plt.imsave(filename + '/crosstalk_white_%s.png' % k, sq_white)
            k += 1
        for l, m in v_bias:
            sq_black = image_vert(l, m, 0, image_h, image_v)
            sq_white = image_vert(l, m, 255, image_h, image_v)
            plt.imsave(filename + '/crosstalk_black_%s.png' % k, sq_black)
            plt.imsave(filename + '/crosstalk_white_%s.png' % k, sq_white)
            k += 1

    # Gray response time
    def responsetime(self):
        image_h = self.image_h
        image_v = self.image_v
        filename = self.filename
        gray = [0, 36, 63, 127, 255]
        image_1 = np.zeros((image_h, image_v, 3), dtype='uint8')
        image_2 = np.zeros((image_h, image_v, 3), dtype='uint8')
        for i in gray:
            for j in gray:
                images = []
                if i < j:
                    image_1[:, :, :] = i
                    image_2[:, :, :] = j
                    images.append(image_1)
                    images.append(image_2)
                    imageio.mimsave(filename + '/gray_responsetime%s_%s.gif' % (i, j), images, duration=0.1)

    # Checkerboard and GL128
    def checkerboard(self):
        image_h = self.image_h
        image_v = self.image_v
        filename = self.filename
        h_pixel = image_h / 16
        l_pixel = image_v / 9
        image = np.zeros((image_h, image_v, 3), dtype='uint8')
        for i in range(1, image_h + 1, 1):
            for j in range(1, image_v + 1, 1):
                if math.ceil(i / h_pixel) % 2 == 0:
                    if math.ceil(j / l_pixel) % 2 == 1:
                        image[i - 1, j - 1, :] = 255
                if math.ceil(i / h_pixel) % 2 == 1:
                    if math.ceil(j / l_pixel) % 2 == 0:
                        image[i - 1, j - 1, :] = 255
        plt.imsave(filename + '/image_checkerboard.png', image)

    # Flicker image
    def flicker(self):
        image_h = self.image_h
        image_v = self.image_v
        filename = self.filename
        image = np.zeros((image_h, image_v, 3), dtype='uint8')
        for i in range(image_h):
            for j in range(image_v):
                if i % 2 == 0:
                    if j % 2 == 1:
                        image[i, j, :] = 128
                if i % 2 == 1:
                    if j % 2 == 0:
                        image[i, j, :] = 128
        plt.imsave(filename + '/flicker1%s.png' % '_dot', image)

        for i in range(1, image_h):
            if i % 4 == 1:
                image[i, :, :] = image[0, :, :]
            if i % 4 == 2:
                image[i, :, :] = image[3, :, :]
        plt.imsave(filename + '/flicker2%s.png' % '_2h1v', image)

        image = np.zeros((image_h, image_v, 3), dtype='uint8')
        for i in range(image_v):
            if i % 6 == 0:
                image[:, i, 0] = 255
            if i % 6 == 2:
                image[:, i, 1] = 255
            if i % 6 == 4:
                image[:, i, 2] = 255
        plt.imsave(filename + '/flicker3%s.png' % '_column', image)

        image = np.zeros((image_h, image_v, 3), dtype='uint8')
        for i in range(image_h):
            if i % 2 == 1:
                image[i, :, :] = 186
        plt.imsave(filename + '/flicker4%s.png' % '_gl186', image)

        image = np.zeros((image_h, image_v, 3), dtype='uint8')
        for i in range(image_v):
            if i % 2 == 1:
                image[:, i, 2] = 255
            if i % 2 == 0:
                image[:, i, 0] = 255
                image[:, i, 1] = 255
        plt.imsave(filename + '/flicker5%s.png' % '_column_by', image)

    # White, red, green, blue image with different gray scales
    def grayscale(self):
        image_h = self.image_h
        image_v = self.image_v
        gls = self.gl
        filename = self.filename
        for gl in gls:
            image_w = np.zeros((image_h, image_v, 3), dtype='uint8') + int(gl)
            image_r = np.zeros((image_h, image_v, 3), dtype='uint8')
            image_r[:, :, 0] = int(gl)
            image_g = np.zeros((image_h, image_v, 3), dtype='uint8')
            image_g[:, :, 1] = int(gl)
            image_b = np.zeros((image_h, image_v, 3), dtype='uint8')
            image_b[:, :, 2] = int(gl)
            plt.imsave(filename + '/white_gl_%s.png' % gl, image_w)
            plt.imsave(filename + '/red_gl_%s.png' % gl, image_r)
            plt.imsave(filename + '/green_gl_%s.png' % gl, image_g)
            plt.imsave(filename + '/blue_gl_%s.png' % gl, image_b)

    # Funny image: Rectangle of different sizes in the middle, with the same aspect ratio
    def funny(self):
        image_h = self.image_h
        image_v = self.image_v
        filename = self.filename
        scaling = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
        image = np.zeros((image_h, image_v, 3), dtype='uint8')
        img = []
        for i in scaling:
            sq_h = math.floor(image_h * math.sqrt(i))
            sq_l = math.floor(image_v * math.sqrt(i))
            padding_h = math.floor((image_h - sq_h) / 2)
            padding_l = math.floor((image_v - sq_l) / 2)
            image[padding_h:padding_h + sq_h, padding_l:padding_l + sq_l, :] = 255
            plt.imsave(filename + '/rect_scaling_%s.png' % i, image)
            tmp_image = image.copy()  # image will cover the front image during each loop
            img.append(tmp_image)
        imageio.mimsave(filename + '/rect_scaling.gif', img, duration=0.1)
