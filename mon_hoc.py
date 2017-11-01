#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide.QtCore import *
from PySide.QtGui import *
from YeuThichUI import *
from linh_vuc import NhomLV
import json


class NhomMH(QMainWindow, Ui_YeuThichMW):
    def __init__(self, pre_window):
        super(NhomMH, self).__init__()
        self.setupUi(self)
        self.setGeometry(300, 100, 900, 550)
        self.student_p = pre_window.student_p

        self.lb_step.setText(QApplication.translate("YeuThichMW", "Bước 2 of 8", None, QApplication.UnicodeUTF8))
        self.lb_typeFavor.setText(QApplication.translate("YeuThichMW", "Mức độ yêu thích trên từng nhóm môn học của bạn:", None, QApplication.UnicodeUTF8))

        self.__nhomMH = ['Nhóm Tự Nhiên','Nhóm Xã Hội', 'Nhóm Ngoại Ngữ', 'Nhóm Thể Dục', 'Nhóm Công Nghệ', 'Nhóm Nghệ Thuật']
        self.__hs_nhomMH = []
        # Them slider cac nhom mon hoc
        for i in range(len(self.__nhomMH)):
            lb_nhomMH = QtGui.QLabel(self.gridLayoutWidget)
            lb_nhomMH.setText(QApplication.translate("YeuThichMW", self.__nhomMH[i] + ": ", None, QApplication.UnicodeUTF8))
            self.gridLayout.addWidget(lb_nhomMH, i, 0, 1, 1)
            lb_min = QtGui.QLabel(self.gridLayoutWidget)
            lb_min.setText('0')
            self.gridLayout.addWidget(lb_min, i, 1, 1, 1)
            hs_nhomMH = QtGui.QSlider(self.gridLayoutWidget)
            hs_nhomMH.setMaximum(10)
            hs_nhomMH.setOrientation(QtCore.Qt.Horizontal)
            self.__hs_nhomMH.append(hs_nhomMH)
            self.gridLayout.addWidget(hs_nhomMH, i, 2, 1, 1)
            lb_max = QtGui.QLabel(self.gridLayoutWidget)
            lb_max.setText('10')
            self.gridLayout.addWidget(lb_max, i, 3, 1, 1)

        # setup cac btn dieu huong
        self.pre_window = pre_window
        self.btn_back.clicked.connect(self.pre_step)

        self.next_window = NhomLV(self)
        self.btn_save_continue.clicked.connect(self.save_next_step)

        self.btn_skip.clicked.connect(self.save_next_step)

    def pre_step(self):
        self.hide()
        self.pre_window.show()

    def save_next_step(self):
        nhom_mon_hoc = []
        for row in range(6):
            nhom_mon_hoc.append(self.gridLayout.itemAt(4*row + 2).widget().value())

        with open(self.student_p, 'r') as stu_f:
            student = json.load(stu_f)
        student['nhom_mon_hoc'] = nhom_mon_hoc

        with open(self.student_p, 'w') as stu_f:
            json.dump(student, stu_f)

        self.hide()
        self.next_window.show()

    # def skip_step(self):
    #     self.hide()
    #     self.next_window.show()
