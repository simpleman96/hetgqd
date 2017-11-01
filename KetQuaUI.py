# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui_files/ketQua.ui'
#
# Created: Mon Oct 30 00:55:25 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_KetQuaMW(object):
    def setupUi(self, KetQuaMW):
        KetQuaMW.setObjectName("KetQuaMW")
        KetQuaMW.resize(873, 525)
        KetQuaMW.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtGui.QWidget(KetQuaMW)
        self.centralwidget.setObjectName("centralwidget")
        self.lb_ketQua = QtGui.QLabel(self.centralwidget)
        self.lb_ketQua.setGeometry(QtCore.QRect(350, 30, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.lb_ketQua.setFont(font)
        self.lb_ketQua.setObjectName("lb_ketQua")
        self.lb_topNganh = QtGui.QLabel(self.centralwidget)
        self.lb_topNganh.setGeometry(QtCore.QRect(80, 110, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.lb_topNganh.setFont(font)
        self.lb_topNganh.setObjectName("lb_topNganh")
        self.formLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(80, 160, 681, 211))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        KetQuaMW.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(KetQuaMW)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 873, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        KetQuaMW.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(KetQuaMW)
        self.statusbar.setObjectName("statusbar")
        KetQuaMW.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(KetQuaMW)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(KetQuaMW)
        QtCore.QMetaObject.connectSlotsByName(KetQuaMW)

    def retranslateUi(self, KetQuaMW):
        KetQuaMW.setWindowTitle(QtGui.QApplication.translate("KetQuaMW", "Hệ thống trợ giúp chọn ngành 2018", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_ketQua.setText(QtGui.QApplication.translate("KetQuaMW", "Kết Quả", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_topNganh.setText(QtGui.QApplication.translate("KetQuaMW", "Bạn nên chọn top 3 ngành học sau:", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("KetQuaMW", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("KetQuaMW", "Exit", None, QtGui.QApplication.UnicodeUTF8))

