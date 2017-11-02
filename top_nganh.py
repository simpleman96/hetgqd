#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide.QtCore import *
from PySide.QtGui import *
from YeuThichUI import *
from top_truong import TopTruong
import pymysql
import json
import ControlDatabaseAccess as CD


class TopNganh(QMainWindow, Ui_YeuThichMW):
    def __init__(self, pre_window):
        super(TopNganh, self).__init__()
        self.setupUi(self)
        self.setGeometry(300, 100, 900, 550)
        self.student_p = pre_window.student_p

        self.lb_step.setText(QApplication.translate("YeuThichMW", "Bước 5 of 8", None, QApplication.UnicodeUTF8))
        self.lb_typeFavor.setText(
            QApplication.translate("YeuThichMW", "Chọn 3 ngành bạn yêu thích nhất cùng mức độ thích:", None,
                                   QApplication.UnicodeUTF8))

        # Lay list nganh tu database
        self.__nganh = CD.get_table('nganh')
        self.__hs_topNganh = []
        # Them slider top nganh
        for i in range(3):
            cb_nganh = QtGui.QComboBox(self.gridLayoutWidget)
            for key in range(len(self.__nganh)):
                cb_nganh.addItem(self.__nganh[key]['ten_nganh'][:30], key)
            self.gridLayout.addWidget(cb_nganh, i, 0, 1, 1)
            lb_min = QtGui.QLabel(self.gridLayoutWidget)
            lb_min.setText('0')
            self.gridLayout.addWidget(lb_min, i, 1, 1, 1)
            hs_topNganh = QtGui.QSlider(self.gridLayoutWidget)
            hs_topNganh.setMaximum(10)
            hs_topNganh.setOrientation(QtCore.Qt.Horizontal)
            self.__hs_topNganh.append(hs_topNganh)
            self.gridLayout.addWidget(hs_topNganh, i, 2, 1, 1)
            lb_max = QtGui.QLabel(self.gridLayoutWidget)
            lb_max.setText('10')
            self.gridLayout.addWidget(lb_max, i, 3, 1, 1)

        # setup cac btn dieu huong
        self.pre_window = pre_window
        self.btn_back.clicked.connect(self.pre_step)

        self.next_window = TopTruong(self)
        self.btn_save_continue.clicked.connect(self.save_next_step)

        self.btn_skip.clicked.connect(self.save_next_step)

    def pre_step(self):
        self.hide()
        self.pre_window.show()

    def save_next_step(self):
        top_nganh = {}
        flat = 0
        for row in range(3):
            nganh = self.gridLayout.itemAt(4 * row).widget().currentText()
            if top_nganh.has_key(nganh):
                flat = 1
                break
            else:
                top_nganh[nganh] = self.gridLayout.itemAt(4 * row + 2).widget().value()

        if flat == 0:
            with open(self.student_p, 'r') as stu_f:
                student = json.load(stu_f)
            student['top_nganh'] = top_nganh

            with open(self.student_p, 'w') as stu_f:
                json.dump(student, stu_f)

            self.hide()
            self.next_window.show()
        else:
            QMessageBox.warning(self, u'Thông Báo!', u'Bạn phải chọn 3 ngành khác nhau!',
                                QMessageBox.Ok)

    # def skip_step(self):
    #     self.hide()
    #     self.next_window.show()

