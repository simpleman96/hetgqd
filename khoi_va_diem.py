#!/usr/bin/env python
# -*- coding: utf-8 -*-

import KhoiVaDiemUI
from PySide.QtGui import *
from PySide.QtCore import *
from mon_hoc import NhomMH
import pymysql
import json


class KhoiDiem(QMainWindow, KhoiVaDiemUI.Ui_KhoiDiemMW):
    def __init__(self, pre_window):
        super(KhoiDiem, self).__init__()
        self.setupUi(self)
        self.setGeometry(300, 100, 900, 550)

        self.student_p = pre_window.student_p

        # Cac loai khoi thi
        self.__khoi_thi = self.get_khoi_thi()
        for key in range(len(self.__khoi_thi)):
            self.cb_khoi.addItem(self.__khoi_thi[key]['ten_khoi'], key)

        # Cac Mon se thi
        self.__mon_thi = []
        self.__khoi_da_chon = []

        self.model_khoi = QStandardItemModel(self.lv_khoi)
        self.lv_khoi.setModel(self.model_khoi)

        # Setup btn_themKhoi, btn_xoaKhoi
        self.btn_themKhoi.clicked.connect(self.them_khoi)
        self.btn_xoaKhoi.clicked.connect(self.xoa_khoi)

        # Setup cac btn dieu huong
        self.pre_window = pre_window
        self.btn_back.clicked.connect(self.pre_step)

        self.next_window = NhomMH(self)
        self.btn_save_continue.clicked.connect(self.save_next_step)

    def them_khoi(self):
        cur_khoi = self.cb_khoi.currentText()
        cur_khoiID = self.cb_khoi.currentIndex()

        if cur_khoi not in self.__khoi_da_chon:
            self.__khoi_da_chon.append(cur_khoi)
        # items = self.model_khoi.findItems(cur_khoi)
        # if len(items) == 0:
            self.model_khoi.appendRow(QStandardItem(cur_khoi))

        before_size = len(self.__mon_thi)
        for i in range(1, 4):
            try:
                self.__mon_thi.index(self.__khoi_thi[cur_khoiID]['mon_' + str(i)])
            except ValueError:
                self.__mon_thi.append(self.__khoi_thi[cur_khoiID]['mon_' + str(i)])

        for row in range(before_size, len(self.__mon_thi)):
            lb_mon = QLabel(self.gridLayoutWidget)
            lb_mon.setAlignment(Qt.AlignCenter)
            lb_mon.setWordWrap(True)
            lb_mon.setText(self.__mon_thi[row])
            self.gl_nhapDiem.addWidget(lb_mon, row + 1, 0, 1, 1)

            for col in range(1, 8):
                cb_diem = QComboBox(self.gridLayoutWidget)
                for key in range(100):
                    cb_diem.addItem(str(key * 0.1), key * 0.1)
                self.gl_nhapDiem.addWidget(cb_diem, row + 1, col, 1, 1)
            cb_cap_thi = QComboBox(self.gridLayoutWidget)
            cb_cap_thi.addItem(u'Cấp Quận', 1)
            cb_cap_thi.addItem(u'Cấp Tỉnh', 2)
            cb_cap_thi.addItem(u'Cấp Quốc Gia', 3)
            cb_cap_thi.addItem(u'Cấp Quốc Tế', 4)
            self.gl_nhapDiem.addWidget(cb_cap_thi, row + 1, 8, 1, 1)

    def xoa_khoi(self):
        # clear model cho list view khoi
        self.model_khoi.clear()
        # clear list mon thi
        self.__mon_thi = []

        for i in reversed(range(8, self.gl_nhapDiem.count())):
            temp = self.gl_nhapDiem.itemAt(i)
            temp.widget().deleteLater()
            self.gl_nhapDiem.removeItem(temp)

    def pre_step(self):
        self.hide()
        self.pre_window.show()

    def save_next_step(self):
        diem_mon = {}
        if self.gl_nhapDiem.rowCount() > 1:
            for row in range(1, self.gl_nhapDiem.rowCount()):
                # mon = self.gl_nhapDiem.itemAt(9 * row).widget().text()
                diem = []
                for col in range(9 * row + 1, 9 * (row + 1)):
                    t_index = self.gl_nhapDiem.itemAt(col).widget().currentIndex()
                    diem.append(self.gl_nhapDiem.itemAt(col).widget().itemData(t_index))
                diem_mon[unicode(self.__mon_thi[row - 1])] = diem

            with open(self.student_p, 'r') as stu_f:
                student = json.load(stu_f)
            student['khoi_diem'] = {'khoi': self.__khoi_da_chon, 'diem': diem_mon}

            with open(self.student_p, 'w') as stu_f:
                json.dump(student, stu_f)

            self.hide()
            self.next_window.show()
        else:
            QMessageBox.warning(self, u'Thông Báo!', u'Bạn phải thi ít nhât 1 khối!',
                                QMessageBox.Ok)

    # def skip_step(self):
    #     self.hide()
    #     self.next_window.show()

    def get_khoi_thi(self):
        # Connect to the database
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='helloworld',
                                     db='enrollment_database',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        result = []
        try:
            with connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT `*` FROM `khoi_thi`"
                cursor.execute(sql)
                result = cursor.fetchall()
        finally:
            connection.close()
            return result
