# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dialog_info.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_info(object):
    def setupUi(self, Dialog_info):
        Dialog_info.setObjectName("Dialog_info")
        Dialog_info.resize(262, 241)
        self.label = QtWidgets.QLabel(Dialog_info)
        self.label.setGeometry(QtCore.QRect(30, 40, 72, 15))
        self.label.setObjectName("label")
        self.label_inlines = QtWidgets.QLabel(Dialog_info)
        self.label_inlines.setGeometry(QtCore.QRect(130, 40, 261, 16))
        self.label_inlines.setObjectName("label_inlines")
        self.label_crosslines = QtWidgets.QLabel(Dialog_info)
        self.label_crosslines.setGeometry(QtCore.QRect(130, 70, 261, 16))
        self.label_crosslines.setObjectName("label_crosslines")
        self.label_2 = QtWidgets.QLabel(Dialog_info)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 91, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog_info)
        self.label_3.setGeometry(QtCore.QRect(30, 100, 91, 16))
        self.label_3.setObjectName("label_3")
        self.label_traces = QtWidgets.QLabel(Dialog_info)
        self.label_traces.setGeometry(QtCore.QRect(130, 100, 261, 16))
        self.label_traces.setObjectName("label_traces")
        self.label_4 = QtWidgets.QLabel(Dialog_info)
        self.label_4.setGeometry(QtCore.QRect(30, 130, 91, 16))
        self.label_4.setObjectName("label_4")
        self.label_samples = QtWidgets.QLabel(Dialog_info)
        self.label_samples.setGeometry(QtCore.QRect(130, 130, 261, 16))
        self.label_samples.setObjectName("label_samples")
        self.label_5 = QtWidgets.QLabel(Dialog_info)
        self.label_5.setGeometry(QtCore.QRect(30, 160, 91, 16))
        self.label_5.setObjectName("label_5")
        self.label_interval = QtWidgets.QLabel(Dialog_info)
        self.label_interval.setGeometry(QtCore.QRect(130, 160, 261, 16))
        self.label_interval.setObjectName("label_interval")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_info)
        self.buttonBox.setGeometry(QtCore.QRect(90, 200, 91, 28))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(Dialog_info)
        QtCore.QMetaObject.connectSlotsByName(Dialog_info)

    def retranslateUi(self, Dialog_info):
        _translate = QtCore.QCoreApplication.translate
        Dialog_info.setWindowTitle(_translate("Dialog_info", "FileInfo"))
        self.label.setText(_translate("Dialog_info", "inlines:"))
        self.label_inlines.setText(_translate("Dialog_info", "TextLabel"))
        self.label_crosslines.setText(_translate("Dialog_info", "TextLabel"))
        self.label_2.setText(_translate("Dialog_info", "crosslines:"))
        self.label_3.setText(_translate("Dialog_info", "traces:"))
        self.label_traces.setText(_translate("Dialog_info", "TextLabel"))
        self.label_4.setText(_translate("Dialog_info", "samples:"))
        self.label_samples.setText(_translate("Dialog_info", "TextLabel"))
        self.label_5.setText(_translate("Dialog_info", "interval:"))
        self.label_interval.setText(_translate("Dialog_info", "TextLabel"))

