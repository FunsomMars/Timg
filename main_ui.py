#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 
# @Time : 2019/11/13 5:11 下午 
# @Author : Simon Meng 
# @Site : mspace.tech
# @File : main_ui.py 
# @Software: PyCharm
import sys
from gui.window import Ui_MainWindow
import timg.img_gen as tm
from PyQt5.QtWidgets import QApplication, QMainWindow


class UiGen(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(UiGen, self).__init__(parent)
        self.setupUi(self)
        self.image_h = 1920
        self.image_v = 1080
        self.filename = 'img'
        self.ppi = 401
        self.gl = [0, 128, 255]
        self.type = 'WRGB纯色'
        self.comboBox.setCurrentIndex(0)
        self.spinBox.setRange(0, 10000)
        self.spinBox_2.setRange(0, 10000)
        self.spinBox_3.setRange(0, 10000)
        self.pushButton.setToolTip('点击以生成图片')
        self.pushButton.clicked.connect(self.button_process)

    def button_process(self):
        if self.spinBox_3.value() != 0:
            self.image_h = int(self.spinBox_3.value())
        if self.spinBox_2.value() != 0:
            self.image_v = int(self.spinBox_2.value())
        if self.lineEdit_5.text() != '':
            self.filename = self.lineEdit_5.text()
        if self.spinBox.value() != 0:
            self.ppi = int(self.spinBox.value())
        if self.lineEdit_3.text() != '':
            self.gl = list(map(int, self.gl + self.lineEdit_3.text().split(',')))
            self.gl.sort()
            self.gl = tuple(self.gl)
        if self.comboBox.currentText() != '':
            self.type = self.comboBox.currentText()

        func_class = tm.Timg(self.image_h, self.image_v, self.filename, self.ppi, self.gl)
        type_list = ['十字对齐', 'WRGB纯色', 'Crosstalk', 'Flicker', '响应时间', '棋盘格', '多灰阶图片']
        func_list = [func_class.align, func_class.purity, func_class.crosstalk, func_class.flicker,
                     func_class.responsetime, func_class.checkerboard, func_class.grayscale]
        func_map = dict(zip(type_list, func_list))
        if self.type in type_list:
            func = func_map[self.type]
            func()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = UiGen()
    MainWindow.show()
    sys.exit(app.exec_())
