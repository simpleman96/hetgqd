#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide.QtCore import *
from PySide.QtGui import *
from YeuThichUI import *
from ket_qua import KetQua
import json
import MainClass
import ControlCalculation as CC


class TieuChi(QMainWindow, Ui_YeuThichMW):
    def __init__(self, pre_window):
        super(TieuChi, self).__init__()
        self.setupUi(self)
        self.setGeometry(300, 100, 900, 550)
        self.student_p = pre_window.student_p

        self.lb_step.setText(QApplication.translate("YeuThichMW", "Bước 8 của 8", None, QApplication.UnicodeUTF8))
        self.lb_typeFavor.setText(
            QApplication.translate("YeuThichMW", "Tiêu chí chọn ngành của bạn:", None,
                                   QApplication.UnicodeUTF8))

        self.__tieu_chi = ['Chắc Chắn Đỗ', 'Đúng Sở Thích', 'Đúng Hoàn Cảnh', 'Dễ Có Việc Làm']
        self.__hs_tieu_chi = []
        # Them slider cac nhom tinh cach
        for i in range(len(self.__tieu_chi)):
            lb_nhomTC = QtGui.QLabel(self.gridLayoutWidget)
            lb_nhomTC.setText(
                QApplication.translate("YeuThichMW", self.__tieu_chi[i] + ": ", None, QApplication.UnicodeUTF8))
            self.gridLayout.addWidget(lb_nhomTC, i, 0, 1, 1)
            lb_min = QtGui.QLabel(self.gridLayoutWidget)
            lb_min.setText('0')
            self.gridLayout.addWidget(lb_min, i, 1, 1, 1)
            hs_nhomTC = QtGui.QSlider(self.gridLayoutWidget)
            hs_nhomTC.setMaximum(10)
            hs_nhomTC.setOrientation(QtCore.Qt.Horizontal)
            self.__hs_tieu_chi.append(hs_nhomTC)
            self.gridLayout.addWidget(hs_nhomTC, i, 2, 1, 1)
            lb_max = QtGui.QLabel(self.gridLayoutWidget)
            lb_max.setText('10')
            self.gridLayout.addWidget(lb_max, i, 3, 1, 1)

        # setup cac btn dieu huong
        self.pre_window = pre_window
        self.btn_back.clicked.connect(self.pre_step)

        # self.next_window = KetQua(self)
        self.btn_save_continue.clicked.connect(self.save_next_step)

        self.btn_skip.clicked.connect(self.save_next_step)

    def pre_step(self):
        self.hide()
        self.pre_window.show()

    def save_next_step(self):
        tieu_chi = []
        for row in range(4):
            tieu_chi.append(self.gridLayout.itemAt(4 * row + 2).widget().value())

        with open(self.student_p, 'r') as stu_f:
            student = json.load(stu_f)
        student['tieu_chi'] = tieu_chi

        with open(self.student_p, 'w') as stu_f:
            json.dump(student, stu_f)

        examGroups = student['khoi_diem']['khoi']

        predictSubjects = {}
        for subject in student['khoi_diem']['diem']:
            averageMark = CC.averageMark(student['khoi_diem']['diem'][subject][:5])
            collegeTestMark = student['khoi_diem']['diem'][subject][5]
            bonusForCompetition = CC.bonusForCompetition(student['khoi_diem']['diem'][subject][6],
                                                         student['khoi_diem']['diem'][subject][7])
            predictSubjects.__setitem__(subject,
                                        CC.predictedMark(averageMark, collegeTestMark, bonusForCompetition))

        subjectFavoriteLevel = student['nhom_mon_hoc']
        fieldFavoriteLevel = student['nhom_linh_vuc']
        characterFavoriteLevel = student['nhom_tinh_cach']
        favoriteMajors = student['top_nganh']
        favoriteColleges = student['top_truong']
        studentFee = student['hoan_canh']
        # The set of weights represents the target of student
        userWeights = CC.normalize(student['tieu_chi'])

        student_input = (
            examGroups, predictSubjects, subjectFavoriteLevel, fieldFavoriteLevel, characterFavoriteLevel,
            favoriteMajors,
            favoriteColleges, studentFee, userWeights)

        top_result = MainClass.caculator(student_input)
        for row in top_result:
            print u'{0}'.format(' - '.join(row))

        self.hide()
        self.next_window = KetQua(top_result)
        self.next_window.show()

        # def skip_step(self):
        #     self.hide()
        #     self.next_window.show()
