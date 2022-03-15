# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SingleTraceSettingUi.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SingleTraceSetting(object):
    def setupUi(self, SingleTraceSetting):
        SingleTraceSetting.setObjectName("SingleTraceSetting")
        SingleTraceSetting.resize(340, 325)
        self.verticalLayout = QtWidgets.QVBoxLayout(SingleTraceSetting)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.label_3 = QtWidgets.QLabel(SingleTraceSetting)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.lineEdit_trace = QtWidgets.QLineEdit(SingleTraceSetting)
        self.lineEdit_trace.setObjectName("lineEdit_trace")
        self.horizontalLayout_4.addWidget(self.lineEdit_trace)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.label = QtWidgets.QLabel(SingleTraceSetting)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.checkBox_fft = QtWidgets.QCheckBox(SingleTraceSetting)
        self.checkBox_fft.setObjectName("checkBox_fft")
        self.horizontalLayout.addWidget(self.checkBox_fft)
        self.checkBox_Log = QtWidgets.QCheckBox(SingleTraceSetting)
        self.checkBox_Log.setEnabled(False)
        self.checkBox_Log.setObjectName("checkBox_Log")
        self.horizontalLayout.addWidget(self.checkBox_Log)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.checkBox_filter = QtWidgets.QCheckBox(SingleTraceSetting)
        self.checkBox_filter.setEnabled(False)
        self.checkBox_filter.setText("")
        self.checkBox_filter.setObjectName("checkBox_filter")
        self.horizontalLayout_5.addWidget(self.checkBox_filter)
        self.pushButton_filter = QtWidgets.QPushButton(SingleTraceSetting)
        self.pushButton_filter.setEnabled(False)
        self.pushButton_filter.setObjectName("pushButton_filter")
        self.horizontalLayout_5.addWidget(self.pushButton_filter)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem7)
        self.buttonBox = QtWidgets.QDialogButtonBox(SingleTraceSetting)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_4.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.verticalLayout_4)

        self.retranslateUi(SingleTraceSetting)
        self.buttonBox.accepted.connect(SingleTraceSetting.accept)
        self.buttonBox.rejected.connect(SingleTraceSetting.reject)
        QtCore.QMetaObject.connectSlotsByName(SingleTraceSetting)

    def retranslateUi(self, SingleTraceSetting):
        _translate = QtCore.QCoreApplication.translate
        SingleTraceSetting.setWindowTitle(_translate("SingleTraceSetting", "SingleTracesSetting"))
        self.label_3.setText(_translate("SingleTraceSetting", "trace："))
        self.label.setText(_translate("SingleTraceSetting", "frequency transform:"))
        self.checkBox_fft.setText(_translate("SingleTraceSetting", "fft"))
        self.checkBox_Log.setText(_translate("SingleTraceSetting", "Log"))
        self.pushButton_filter.setText(_translate("SingleTraceSetting", "Bandpass Filter"))

