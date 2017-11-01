#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide.QtCore import *
from PySide.QtGui import *
from YeuThichUI import *
from tieu_chi import TieuChi
import json


class HoanCanh(QMainWindow, Ui_YeuThichMW):
    def __init__(self, pre_window):
        super(HoanCanh, self).__init__()
        self.setupUi(self)
        self.setGeometry(300, 100, 900, 550)
        self.student_p = pre_window.student_p

        self.lb_step.setText(QApplication.translate("YeuThichMW", "Bước 7 of 8", None, QApplication.UnicodeUTF8))
        self.lb_typeFavor.setText(
            QApplication.translate("YeuThichMW", "Chọn điều kiện tài chính của gia đình bạn:", None,
                                   QApplication.UnicodeUTF8))

        # Them slider dktc
        lb_min = QtGui.QLabel(self.gridLayoutWidget)
        lb_min.setText('0')
        self.gridLayout.addWidget(lb_min, 0, 0, 1, 1)
        self.hs_dieuKien = QtGui.QSlider(self.gridLayoutWidget)
        self.hs_dieuKien.setMaximum(5)
        self.hs_dieuKien.setOrientation(QtCore.Qt.Horizontal)
        self.gridLayout.addWidget(self.hs_dieuKien, 0, 1, 1, 1)
        lb_max = QtGui.QLabel(self.gridLayoutWidget)
        lb_max.setText('5')
        self.gridLayout.addWidget(lb_max, 0, 2, 1, 1)

        # setup cac btn dieu huong
        self.pre_window = pre_window
        self.btn_back.clicked.connect(self.pre_step)

        self.next_window = TieuChi(self)
        self.btn_save_continue.clicked.connect(self.save_next_step)
        self.btn_skip.clicked.connect(self.save_next_step)


    def pre_step(self):
        self.hide()
        self.pre_window.show()

    def save_next_step(self):
        hoan_canh = self.gridLayout.itemAt(1).widget().value()
        with open(self.student_p, 'r') as stu_f:
            student = json.load(stu_f)
        student['hoan_canh'] = hoan_canh

        with open(self.student_p, 'w') as stu_f:
            json.dump(student, stu_f)

        self.hide()
        self.next_window.show()

    # def skip_step(self):
    #     self.hide()
    #     self.next_window.show()
