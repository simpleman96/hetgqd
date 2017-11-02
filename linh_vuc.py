#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide.QtCore import *
from PySide.QtGui import *
from YeuThichUI import *
from tinh_cach import NhomTC
import json


class NhomLV(QMainWindow, Ui_YeuThichMW):
    def __init__(self, pre_window):
        super(NhomLV, self).__init__()
        self.setupUi(self)
        self.setGeometry(300, 100, 900, 550)
        self.student_p = pre_window.student_p

        self.lb_step.setText(QApplication.translate("YeuThichMW", "Bước 3 của 8", None, QApplication.UnicodeUTF8))
        self.lb_typeFavor.setText(
            QApplication.translate("YeuThichMW", "Mức độ yêu thích trên từng nhóm lĩnh vực của bạn:", None,
                                   QApplication.UnicodeUTF8))

        self.__nhomLV = ['Khoa Học Xã Hội Nhân Văn', 'Khoa Học Tự Nhiên', 'Khoa Học Kỹ Thuật Công Nghệ', 'Kinh Tế', 'Y Dược',
                         'An Ninh Quốc Phòng', 'Văn Hóa - Thể Thao - Năng Khiếu']
        self.__hs_nhomLV = []
        # Them slider cac nhom linh vuc
        for i in range(len(self.__nhomLV)):
            lb_nhomLV = QtGui.QLabel(self.gridLayoutWidget)
            lb_nhomLV.setWordWrap(True)
            lb_nhomLV.setText(
                QApplication.translate("YeuThichMW", self.__nhomLV[i] + ": ", None, QApplication.UnicodeUTF8))
            self.gridLayout.addWidget(lb_nhomLV, i, 0, 1, 1)
            lb_min = QtGui.QLabel(self.gridLayoutWidget)
            lb_min.setText('0')
            self.gridLayout.addWidget(lb_min, i, 1, 1, 1)
            hs_nhomLV = QtGui.QSlider(self.gridLayoutWidget)
            hs_nhomLV.setMaximum(10)
            hs_nhomLV.setOrientation(QtCore.Qt.Horizontal)
            self.__hs_nhomLV.append(hs_nhomLV)
            self.gridLayout.addWidget(hs_nhomLV, i, 2, 1, 1)
            lb_max = QtGui.QLabel(self.gridLayoutWidget)
            lb_max.setText('10')
            self.gridLayout.addWidget(lb_max, i, 3, 1, 1)

        # setup cac btn dieu huong
        self.pre_window = pre_window
        self.btn_back.clicked.connect(self.pre_step)

        self.next_window = NhomTC(self)
        self.btn_save_continue.clicked.connect(self.save_next_step)

        self.btn_skip.clicked.connect(self.save_next_step)


    def pre_step(self):
        self.hide()
        self.pre_window.show()

    def save_next_step(self):
        nhom_linh_vuc = []
        for row in range(7):
            nhom_linh_vuc.append(self.gridLayout.itemAt(4 * row + 2).widget().value())

        with open(self.student_p, 'r') as stu_f:
            student = json.load(stu_f)
        student['nhom_linh_vuc'] = nhom_linh_vuc

        with open(self.student_p, 'w') as stu_f:
            json.dump(student, stu_f)

        self.hide()
        self.next_window.show()

    # def skip_step(self):
    #     self.hide()
    #     self.next_window.show()
