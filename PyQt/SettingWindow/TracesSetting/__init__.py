from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt.SettingWindow.TracesSetting.TracesSettingUi import Ui_TracesSetting
from UiParameter import *


class TracesSetting(QDialog):
    # 定义信号
    signal = QtCore.pyqtSignal(TracesTraceUiParas)

    def __init__(self):
        super().__init__()
        self.ui = Ui_TracesSetting()
        self.ui.setupUi(self)

    def accept(self):
        tracesUiParas = TracesTraceUiParas()
        tracesUiParas.firstTrace = int(self.ui.FirstLineEdit.text())
        tracesUiParas.interval = int(self.ui.IntervalEdit.text())
        tracesUiParas.gain = float(self.ui.GainEdit.text())
        # tracesUiParas.showNum = int(self.ui.ShowNumEdit.text())
        tracesUiParas.bfft = self.ui.checkBox_fft.checkState()
        tracesUiParas.bColorImage = self.ui.checkBox_Color.checkState()
        #if tracesUiParas.showNum > (tracesUiParas.lastTrace - tracesUiParas.firstTrace):
        #    QMessageBox.critical(self, "Error", "showNum错误，请检查！")
        #    tracesUiParas.showNum = 1
        self.signal.emit(tracesUiParas)
        self.close()
