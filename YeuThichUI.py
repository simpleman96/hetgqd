# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui_files/nhomMH.ui'
#
# Created: Sun Oct 29 23:42:34 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_YeuThichMW(object):
    def setupUi(self, YeuThichMW):
        YeuThichMW.setObjectName("YeuThichMW")
        YeuThichMW.resize(873, 525)
        YeuThichMW.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtGui.QWidget(YeuThichMW)
        self.centralwidget.setObjectName("centralwidget")
        self.lb_step = QtGui.QLabel(self.centralwidget)
        self.lb_step.setGeometry(QtCore.QRect(60, 30, 200, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lb_step.setFont(font)
        self.lb_step.setObjectName("lb_step")
        self.btn_back = QtGui.QPushButton(self.centralwidget)
        self.btn_back.setGeometry(QtCore.QRect(20, 450, 91, 27))
        self.btn_back.setObjectName("btn_back")
        self.btn_save_continue = QtGui.QPushButton(self.centralwidget)
        self.btn_save_continue.setGeometry(QtCore.QRect(110, 450, 121, 27))
        self.btn_save_continue.setObjectName("btn_save_continue")
        self.btn_skip = QtGui.QPushButton(self.centralwidget)
        self.btn_skip.setGeometry(QtCore.QRect(230, 450, 121, 27))
        self.btn_skip.setObjectName("btn_skip")
        self.lb_typeFavor = QtGui.QLabel(self.centralwidget)
        self.lb_typeFavor.setGeometry(QtCore.QRect(60, 80, 451, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.lb_typeFavor.setFont(font)
        self.lb_typeFavor.setObjectName("lb_typeFavor")
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(60, 120, 541, 291))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        YeuThichMW.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(YeuThichMW)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 873, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        YeuThichMW.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(YeuThichMW)
        self.statusbar.setObjectName("statusbar")
        YeuThichMW.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(YeuThichMW)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(YeuThichMW)
        QtCore.QMetaObject.connectSlotsByName(YeuThichMW)

    def retranslateUi(self, YeuThichMW):
        YeuThichMW.setWindowTitle(QtGui.QApplication.translate("YeuThichMW", "Hệ thống trợ giúp chọn ngành 2018", None, QtGui.QApplication.UnicodeUTF8))
        # self.lb_step.setText(QtGui.QApplication.translate("YeuThichMW", "Bước 2 of 9", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_back.setText(QtGui.QApplication.translate("YeuThichMW", "Quay lại", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_save_continue.setText(QtGui.QApplication.translate("YeuThichMW", "Lưu và tiếp tục", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_skip.setText(QtGui.QApplication.translate("YeuThichMW", "Bỏ qua bước này", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_typeFavor.setText(QtGui.QApplication.translate("YeuThichMW", "Mức độ yêu thích trên từng nhóm môn học của bạn:", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("YeuThichMW", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("YeuThichMW", "Exit", None, QtGui.QApplication.UnicodeUTF8))

