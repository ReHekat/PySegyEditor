from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt.SettingWindow.CRGSetting.CRGSettingUi import Ui_CRGSetting
from UiParameter import *


class CRGSetting(QDialog):
    # 定义信号
    signal = QtCore.pyqtSignal(CRGTraceUiParas)

    def __init__(self):
        super().__init__()
        self.ui = Ui_CRGSetting()
        self.ui.setupUi(self)
        # ui设置
        self.ui.comboBox_Depth.addItem("ft")
        # self.ui.comboBox_Depth.addItem("m")
        self.ui.comboBox_Depth.setCurrentIndex(0)

    def ui_update(self, CRG_ALL_LIST):
        for item in CRG_ALL_LIST:
            self.ui.comboBox_DepthEdit.addItem(str(int(item)))

    def accept(self):
        crg_UiParas = CRGTraceUiParas()
        crg_UiParas.depth = int(self.ui.comboBox_DepthEdit.currentText())
        # receiverDepth_Unit = self.ui.comboBox_ReceiverDepth.currentText()
        crg_UiParas.gain = float(self.ui.GainEdit.text())
        #crg_UiParas.showNum = int(self.ui.ShowNumEdit.text())
        crg_UiParas.bfft = self.ui.checkBox_fft.checkState()
        crg_UiParas.bColorImage = self.ui.checkBox_Color.checkState()
        self.signal.emit(crg_UiParas)
        self.close()
