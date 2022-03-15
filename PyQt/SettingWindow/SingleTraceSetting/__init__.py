from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt.SettingWindow.SingleTraceSetting.SingleTraceSettingUi import Ui_SingleTraceSetting
from UiParameter import SingleTraceUiParas


class SingleTraceSetting(QDialog):
    # 定义信号
    signal = QtCore.pyqtSignal(SingleTraceUiParas)

    def __init__(self):
        super().__init__()
        self.ui = Ui_SingleTraceSetting()
        self.ui.setupUi(self)

    def accept(self):
        singleTraceTraceUiParas = SingleTraceUiParas()
        singleTraceTraceUiParas.trace = int(self.ui.lineEdit_trace.text())
        singleTraceTraceUiParas.bfft = self.ui.checkBox_fft.checkState()
        singleTraceTraceUiParas.blog = self.ui.checkBox_Log.checkState()
        singleTraceTraceUiParas.bfilter = self.ui.checkBox_filter.checkState()
        self.signal.emit(singleTraceTraceUiParas)
        self.close()
