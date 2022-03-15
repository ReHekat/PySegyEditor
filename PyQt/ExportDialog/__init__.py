from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt.ExportDialog.ExportDialog import Ui_Dialog_Export
from UiParameter import ExportAcousticUiParas


class ExportDialog(QDialog):
    # 定义信号
    signal = QtCore.pyqtSignal(ExportAcousticUiParas)

    def __init__(self):
        super().__init__()
        # 参数定义
        self.type = "acoustic"  # "acoustic"  or  "elastic"
        self.sourceAllList = []
        self.receiverAllList = []
        # ui设置
        self.ui = Ui_Dialog_Export()
        self.ui.setupUi(self)
        self.source_pButtonGroup = QButtonGroup()
        self.receiver_pButtonGroup = QButtonGroup()
        self.source_pButtonGroup.setExclusive(True)
        self.receiver_pButtonGroup.setExclusive(True)
        self.source_pButtonGroup.addButton(self.ui.radioButton_AllSource)
        self.source_pButtonGroup.addButton(self.ui.radioButton_RangeSource)
        self.receiver_pButtonGroup.addButton(self.ui.radioButton_RangeReceiver)
        self.receiver_pButtonGroup.addButton(self.ui.radioButton_AllReceiver)
        # 信号连接
        self.ui.lineEdit_FreqNum.textChanged.connect(self.freqNumChanged)
        self.ui.pushButton_Open.clicked.connect(self.open_clicked)
        #  注：以下应使用QButtonGroup来实现互斥效果，不必手工重写逻辑
        self.ui.radioButton_AllSource.clicked.connect(self.sourceRadioClicked)
        self.ui.radioButton_RangeSource.clicked.connect(self.sourceRadioClicked)
        self.ui.radioButton_AllReceiver.clicked.connect(self.receiverRadioClicked)
        self.ui.radioButton_RangeReceiver.clicked.connect(self.receiverRadioClicked)

    def ui_update(self, fileType, sourceAllList, receiverAllList):
        if fileType == "acoustic":
            self.type = fileType
            self.ui.label_Direction.setVisible(False)
            self.ui.comboBox_Direction.setVisible(False)
            self.ui.comboBox_Direction.addItem("0")
            self.ui.comboBox_Direction.setCurrentIndex(0)
        elif fileType == "elastic":
            self.type = fileType
            # 先清除控件
            for i in range(0, self.ui.comboBox_Direction.count()):
                self.ui.comboBox_Direction.removeItem(0)
            self.ui.label_Direction.setVisible(True)
            self.ui.comboBox_Direction.setVisible(True)
            self.ui.comboBox_Direction.addItem("1")
            self.ui.comboBox_Direction.addItem("2")
            self.ui.comboBox_Direction.addItem("3")
        self.sourceAllList = sourceAllList
        self.receiverAllList = receiverAllList
        for i in range(0, len(sourceAllList)):
            self.ui.comboBox_Source1.addItem(str(sourceAllList[i]))
            self.ui.comboBox_Source2.addItem(str(sourceAllList[i]))
        for i in range(0, len(receiverAllList)):
            self.ui.comboBox_Receiver1.addItem(str(receiverAllList[i]))
            self.ui.comboBox_Receiver2.addItem(str(receiverAllList[i]))

    def freqNumChanged(self):
        if self.ui.lineEdit_FreqNum.text() and int(self.ui.lineEdit_FreqNum.text()) > 0:
            # 先清除控件
            for i in range(0, self.ui.verticalLayout_Freq.count()):
                item = self.ui.verticalLayout_Freq.itemAt(0)
                self.ui.verticalLayout_Freq.removeItem(item)
                if item.widget():
                    item.widget().deleteLater()
            # 重置窗口尺寸
            self.resize(436, 397)
            # 重新添加控件
            for i in range(0, int(self.ui.lineEdit_FreqNum.text())):
                self.ui.verticalLayout_Freq.addWidget(QLineEdit(self))

    def sourceRadioClicked(self):
        if self.ui.radioButton_AllSource.isChecked():
            #self.ui.radioButton_RangeSource.setChecked(False)
            for i in range(0, self.ui.horizontalLayout_SourceRange.count()):
                item = self.ui.horizontalLayout_SourceRange.itemAt(i)
                if item.widget():
                    item.widget().setEnabled(False)
        if self.ui.radioButton_RangeSource.isChecked():
            #self.ui.radioButton_AllSource.setChecked(False)
            for i in range(0, self.ui.horizontalLayout_SourceRange.count()):
                item = self.ui.horizontalLayout_SourceRange.itemAt(i)
                if item.widget():
                    item.widget().setEnabled(True)

    def receiverRadioClicked(self):
        if self.ui.radioButton_AllReceiver.isChecked():
            #self.ui.radioButton_RangeReceiver.setChecked(False)
            for i in range(0, self.ui.horizontalLayout_ReceiverRange.count()):
                item = self.ui.horizontalLayout_ReceiverRange.itemAt(i)
                if item.widget():
                    item.widget().setEnabled(False)
        if self.ui.radioButton_RangeReceiver.isChecked():
            #self.ui.radioButton_AllReceiver.setChecked(False)
            for i in range(0, self.ui.horizontalLayout_ReceiverRange.count()):
                item = self.ui.horizontalLayout_ReceiverRange.itemAt(i)
                if item.widget():
                    item.widget().setEnabled(True)

    def open_clicked(self):
        if self.type == "acoustic":
            path = QFileDialog.getSaveFileName(self, '选择文件', '', 'acoustic files(*.segy_acoustic.rec)')
        elif self.type == "elastic":
            path = QFileDialog.getSaveFileName(self, '选择文件', '', 'elastic files(*.segy_elastic.rec)')
        else:
            raise Exception('acoustic type Error')
        if len(path[0]) > 1:
            self.ui.lineEdit_Path.setText(path[0])

    def accept(self):
        super(ExportDialog, self).accept()
        paras = ExportAcousticUiParas()
        paras.path = str(self.ui.lineEdit_Path.text())
        paras.freqNum = int(self.ui.lineEdit_FreqNum.text())
        for i in range(0, self.ui.verticalLayout_Freq.count()):
            paras.freqList.append(float(self.ui.verticalLayout_Freq.itemAt(i).widget().text()))
        if self.ui.radioButton_AllSource.isChecked():
            paras.sourceList = self.sourceAllList
        else:
            source_min = float(self.ui.comboBox_Source1.currentText())
            source_max = float(self.ui.comboBox_Source2.currentText())
            min_index = self.sourceAllList.index(source_min)
            max_index = self.sourceAllList.index(source_max)
            paras.sourceList = self.sourceAllList[min_index:max_index + 1]
        if self.ui.radioButton_AllReceiver.isChecked():
            paras.receiverList = self.receiverAllList
        else:
            receiver_min = float(self.ui.comboBox_Receiver1.currentText())
            receiver_max = float(self.ui.comboBox_Receiver2.currentText())
            min_index = self.receiverAllList.index(receiver_min)
            max_index = self.receiverAllList.index(receiver_max)
            paras.receiverList = self.receiverAllList[min_index:max_index + 1]
        paras.direction = int(self.ui.comboBox_Direction.currentText())
        self.signal.emit(paras)
