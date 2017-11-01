#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide.QtCore import *
from PySide.QtGui import *
from KetQuaUI import *
import json
import pymysql


class KetQua(QMainWindow, Ui_KetQuaMW):
    def __init__(self, top_result):
        super(KetQua, self).__init__()
        self.setupUi(self)
        self.setGeometry(300, 100, 900, 550)

        # self.__ket_qua = []       # Gom ten cac nganh va giai thich tuong ung
        # self.top_result = top_result
        # print self.top_result
        for row in range(len(top_result)):
            lb_nganh = QtGui.QLabel(self.formLayoutWidget)
            lb_nganh.setWordWrap(True)
            lb_nganh.setText(u'{0}'.format(' - '.join(top_result[row])))
                # QApplication.translate("KetQuaMW", u'{0}'.format(' - '.join(top_result[row])), None,
                #                    QApplication.UnicodeUTF8))

            self.formLayout.setWidget(row, QtGui.QFormLayout.LabelRole, lb_nganh)
            lb_giaiThich = QtGui.QLabel(self.formLayoutWidget)
            lb_giaiThich.setWordWrap(True)
            lb_giaiThich.setText(QApplication.translate("KetQuaMW", "Giải thích cho Ngành trường", None,
                                                        QApplication.UnicodeUTF8))
            self.formLayout.setWidget(row, QtGui.QFormLayout.FieldRole, lb_giaiThich)