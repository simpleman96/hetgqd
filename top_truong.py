#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide.QtCore import *
from PySide.QtGui import *
from YeuThichUI import *
from hoan_canh import HoanCanh
import pymysql
import json
import ControlDatabaseAccess as CD


class TopTruong(QMainWindow, Ui_YeuThichMW):
    def __init__(self, pre_window):
        super(TopTruong, self).__init__()
        self.setupUi(self)
        self.setGeometry(300, 100, 900, 550)
        self.setFixedSize(900, 550)

        self.student_p = pre_window.student_p

        self.lb_step.setText(QApplication.translate("YeuThichMW", "Bước 6 of 8", None, QApplication.UnicodeUTF8))
        self.lb_typeFavor.setText(
            QApplication.translate("YeuThichMW", "Chọn 3 trường bạn yêu thích nhất cùng mức độ thích:", None,
                                   QApplication.UnicodeUTF8))
        self.__truong = CD.get_table('truong')
        self.__hs_topTruong = []
        # Them slider top truong
        for i in range(3):
            cb_truong = QtGui.QComboBox(self.gridLayoutWidget)
            for key in range(len(self.__truong)):
                cb_truong.addItem(self.__truong[key]['ten_truong'][:30], key)
            self.gridLayout.addWidget(cb_truong, i, 0, 1, 1)
            lb_min = QtGui.QLabel(self.gridLayoutWidget)
            lb_min.setText('0')
            self.gridLayout.addWidget(lb_min, i, 1, 1, 1)
            hs_topTruong = QtGui.QSlider(self.gridLayoutWidget)
            hs_topTruong.setMaximum(10)
            hs_topTruong.setOrientation(QtCore.Qt.Horizontal)
            self.__hs_topTruong.append(hs_topTruong)
            self.gridLayout.addWidget(hs_topTruong, i, 2, 1, 1)
            lb_max = QtGui.QLabel(self.gridLayoutWidget)
            lb_max.setText('10')
            self.gridLayout.addWidget(lb_max, i, 3, 1, 1)

        # setup cac btn dieu huong
        self.pre_window = pre_window
        self.btn_back.clicked.connect(self.pre_step)

        self.next_window = HoanCanh(self)
        self.btn_save_continue.clicked.connect(self.save_next_step)

        self.btn_skip.clicked.connect(self.save_next_step)

    def pre_step(self):
        self.hide()
        self.pre_window.show()

    def save_next_step(self):
        top_truong = {}
        flat = 0
        for row in range(3):
            truong = self.gridLayout.itemAt(4 * row).widget().currentText()
            if truong in top_truong.keys():
                flat = 1
                break
            else:
                top_truong[truong] = self.gridLayout.itemAt(4 * row + 2).widget().value()

        if flat == 0:
            with open(self.student_p, 'r') as stu_f:
                student = json.load(stu_f)
            student['top_truong'] = top_truong

            with open(self.student_p, 'w') as stu_f:
                json.dump(student, stu_f)

            self.hide()
            self.next_window.show()
        else:
            QMessageBox.warning(self, u'Thông Báo!', u'Bạn phải chọn 3 trường khác nhau!',
                                QMessageBox.Ok)

    # def skip_step(self):
    #     self.hide()
    #     self.next_window.show()
