#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide.QtCore import *
from PySide.QtGui import *
from YeuThichUI import *
from top_nganh import TopNganh
import json


class NhomTC(QMainWindow, Ui_YeuThichMW):
    def __init__(self, pre_window):
        super(NhomTC, self).__init__()
        self.setupUi(self)
        self.setGeometry(300, 100, 900, 550)
        self.setFixedSize(900, 550)

        self.student_p = pre_window.student_p

        self.lb_step.setText(QApplication.translate("YeuThichMW", "Bước 4 của 8", None, QApplication.UnicodeUTF8))
        self.lb_typeFavor.setText(
            QApplication.translate("YeuThichMW", "Mức độ phù hợp trên từng nhóm tính cách của bạn:", None,
                                   QApplication.UnicodeUTF8))

        self.__nhomTC = ['Nhóm Thống Trị', 'Nhóm Ảnh Hưởng', 'Nhóm Kiên Định', 'Nhóm Tuân Thủ']
        self.__hs_nhomTC = []
        # Them slider cac nhom tinh cach
        for i in range(len(self.__nhomTC)):
            lb_nhomTC = QtGui.QLabel(self.gridLayoutWidget)
            lb_nhomTC.setText(
                QApplication.translate("YeuThichMW", self.__nhomTC[i] + ": ", None, QApplication.UnicodeUTF8))
            self.gridLayout.addWidget(lb_nhomTC, i, 0, 1, 1)
            lb_min = QtGui.QLabel(self.gridLayoutWidget)
            lb_min.setText('0')
            self.gridLayout.addWidget(lb_min, i, 1, 1, 1)
            hs_nhomTC = QtGui.QSlider(self.gridLayoutWidget)
            hs_nhomTC.setMaximum(10)
            hs_nhomTC.setOrientation(QtCore.Qt.Horizontal)
            self.__hs_nhomTC.append(hs_nhomTC)
            self.gridLayout.addWidget(hs_nhomTC, i, 2, 1, 1)
            lb_max = QtGui.QLabel(self.gridLayoutWidget)
            lb_max.setText('10')
            self.gridLayout.addWidget(lb_max, i, 3, 1, 1)

        # setup cac btn dieu huong
        self.pre_window = pre_window
        self.btn_back.clicked.connect(self.pre_step)

        self.next_window = TopNganh(self)
        self.btn_save_continue.clicked.connect(self.save_next_step)

        self.btn_skip.clicked.connect(self.save_next_step)

    def pre_step(self):
        self.hide()
        self.pre_window.show()

    def save_next_step(self):
        nhom_tinh_cach = []
        for row in range(4):
            nhom_tinh_cach.append(self.gridLayout.itemAt(4 * row + 2).widget().value())

        with open(self.student_p, 'r') as stu_f:
            student = json.load(stu_f)
        student['nhom_tinh_cach'] = nhom_tinh_cach

        with open(self.student_p, 'w') as stu_f:
            json.dump(student, stu_f)

        self.hide()
        self.next_window.show()

    # def skip_step(self):
    #     self.hide()
    #     self.next_window.show()
