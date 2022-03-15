# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AllTracesSettingUi.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AllTracesSetting(object):
    def setupUi(self, AllTracesSetting):
        AllTracesSetting.setObjectName("AllTracesSetting")
        AllTracesSetting.resize(327, 304)
        self.verticalLayout = QtWidgets.QVBoxLayout(AllTracesSetting)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.label_3 = QtWidgets.QLabel(AllTracesSetting)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.GainEdit = QtWidgets.QLineEdit(AllTracesSetting)
        self.GainEdit.setObjectName("GainEdit")
        self.horizontalLayout_4.addWidget(self.GainEdit)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.label_4 = QtWidgets.QLabel(AllTracesSetting)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.ShowNumEdit = QtWidgets.QLineEdit(AllTracesSetting)
        self.ShowNumEdit.setObjectName("ShowNumEdit")
        self.horizontalLayout_5.addWidget(self.ShowNumEdit)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.checkBox_fft = QtWidgets.QCheckBox(AllTracesSetting)
        self.checkBox_fft.setObjectName("checkBox_fft")
        self.horizontalLayout.addWidget(self.checkBox_fft)
        self.checkBox_Color = QtWidgets.QCheckBox(AllTracesSetting)
        self.checkBox_Color.setObjectName("checkBox_Color")
        self.horizontalLayout.addWidget(self.checkBox_Color)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem7)
        self.buttonBox = QtWidgets.QDialogButtonBox(AllTracesSetting)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_4.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.verticalLayout_4)

        self.retranslateUi(AllTracesSetting)
        self.buttonBox.accepted.connect(AllTracesSetting.accept)
        self.buttonBox.rejected.connect(AllTracesSetting.reject)
        QtCore.QMetaObject.connectSlotsByName(AllTracesSetting)

    def retranslateUi(self, AllTracesSetting):
        _translate = QtCore.QCoreApplication.translate
        AllTracesSetting.setWindowTitle(_translate("AllTracesSetting", "AllTracesSetting"))
        self.label_3.setText(_translate("AllTracesSetting", "   Gain："))
        self.label_4.setText(_translate("AllTracesSetting", "ShowNum："))
        self.checkBox_fft.setText(_translate("AllTracesSetting", "fft(log)"))
        self.checkBox_Color.setText(_translate("AllTracesSetting", "Color"))

