# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CRGSettingUi.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CRGSetting(object):
    def setupUi(self, CRGSetting):
        CRGSetting.setObjectName("CRGSetting")
        CRGSetting.resize(464, 375)
        self.verticalLayout = QtWidgets.QVBoxLayout(CRGSetting)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label_2 = QtWidgets.QLabel(CRGSetting)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.comboBox_DepthEdit = QtWidgets.QComboBox(CRGSetting)
        self.comboBox_DepthEdit.setMinimumSize(QtCore.QSize(150, 0))
        self.comboBox_DepthEdit.setObjectName("comboBox_DepthEdit")
        self.horizontalLayout_2.addWidget(self.comboBox_DepthEdit)
        self.comboBox_Depth = QtWidgets.QComboBox(CRGSetting)
        self.comboBox_Depth.setObjectName("comboBox_Depth")
        self.horizontalLayout_2.addWidget(self.comboBox_Depth)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.label_3 = QtWidgets.QLabel(CRGSetting)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.GainEdit = QtWidgets.QLineEdit(CRGSetting)
        self.GainEdit.setObjectName("GainEdit")
        self.horizontalLayout_4.addWidget(self.GainEdit)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.label_4 = QtWidgets.QLabel(CRGSetting)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.ShowNumEdit = QtWidgets.QLineEdit(CRGSetting)
        self.ShowNumEdit.setEnabled(False)
        self.ShowNumEdit.setObjectName("ShowNumEdit")
        self.horizontalLayout_5.addWidget(self.ShowNumEdit)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.checkBox_fft = QtWidgets.QCheckBox(CRGSetting)
        self.checkBox_fft.setObjectName("checkBox_fft")
        self.horizontalLayout_3.addWidget(self.checkBox_fft)
        self.checkBox_Color = QtWidgets.QCheckBox(CRGSetting)
        self.checkBox_Color.setObjectName("checkBox_Color")
        self.horizontalLayout_3.addWidget(self.checkBox_Color)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem8)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem9)
        self.buttonBox = QtWidgets.QDialogButtonBox(CRGSetting)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_4.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.verticalLayout_4)

        self.retranslateUi(CRGSetting)
        self.buttonBox.accepted.connect(CRGSetting.accept)
        self.buttonBox.rejected.connect(CRGSetting.reject)
        QtCore.QMetaObject.connectSlotsByName(CRGSetting)

    def retranslateUi(self, CRGSetting):
        _translate = QtCore.QCoreApplication.translate
        CRGSetting.setWindowTitle(_translate("CRGSetting", "CRGSetting"))
        self.label_2.setText(_translate("CRGSetting", "   receiverDepth："))
        self.label_3.setText(_translate("CRGSetting", "   Gain："))
        self.label_4.setText(_translate("CRGSetting", "ShowNum："))
        self.checkBox_fft.setText(_translate("CRGSetting", "fft(log)"))
        self.checkBox_Color.setText(_translate("CRGSetting", "Color"))

