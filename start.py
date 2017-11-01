#!/usr/bin/env python
# -*- coding: utf-8 -*-

import StartUI
from PySide.QtGui import *
from PySide.QtCore import *
from khoi_va_diem import KhoiDiem
import sys
import os
import json


class Start(QMainWindow, StartUI.Ui_MainWindow):
    def __init__(self, stu_input_p):
        super(Start, self).__init__()
        self.setupUi(self)
        self.setGeometry(300, 100, 900, 550)

        self.student_p = stu_input_p
        self.next_window = KhoiDiem(self)
        self.btn_start.clicked.connect(self.next_step)

    def next_step(self):
        if len(self.le_name.text().strip()) == 0:
            QMessageBox.warning(self, u'Thông Báo!', u'Bạn chưa nhập tên!',
                                         QMessageBox.Ok)
        else:
            student = {'name': self.le_name.text()}
            with open(self.student_p, 'w') as stu_f:
                json.dump(student, stu_f)
            self.hide()
            self.next_window.show()


if __name__ == '__main__':
    stu_input_p = os.path.join(os.getcwd(), 'student_input')
    app = QApplication(sys.argv)
    window = Start(stu_input_p)
    window.show()
    sys.exit(app.exec_())
