# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WaitingDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_Wating(object):
    def setupUi(self, Dialog_Wating):
        Dialog_Wating.setObjectName("Dialog_Wating")
        Dialog_Wating.resize(355, 96)
        self.gridLayout = QtWidgets.QGridLayout(Dialog_Wating)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Dialog_Wating)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_movie = QtWidgets.QLabel(Dialog_Wating)
        self.label_movie.setText("")
        self.label_movie.setObjectName("label_movie")
        self.gridLayout.addWidget(self.label_movie, 1, 0, 1, 1)

        self.retranslateUi(Dialog_Wating)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Wating)

    def retranslateUi(self, Dialog_Wating):
        _translate = QtCore.QCoreApplication.translate
        Dialog_Wating.setWindowTitle(_translate("Dialog_Wating", "Waiting"))
        self.label.setText(_translate("Dialog_Wating", "Waiting..."))

