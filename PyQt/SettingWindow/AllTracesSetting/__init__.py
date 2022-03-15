from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt.SettingWindow.AllTracesSetting.AllTracesSettingUi import Ui_AllTracesSetting
from UiParameter import *


class AllTracesSetting(QDialog):
    # 定义信号
    signal = QtCore.pyqtSignal(AllTracesTraceUiParas)

    def __init__(self):
        super().__init__()
        self.ui = Ui_AllTracesSetting()
        self.ui.setupUi(self)

    def accept(self):
        allTracesUiParas = AllTracesTraceUiParas()
        allTracesUiParas.gain = float(self.ui.GainEdit.text())
        allTracesUiParas.showNum = int(self.ui.ShowNumEdit.text())
        allTracesUiParas.bfft = self.ui.checkBox_fft.checkState()
        allTracesUiParas.bColorImage = self.ui.checkBox_Color.checkState()
        self.signal.emit(allTracesUiParas)
        self.close()
