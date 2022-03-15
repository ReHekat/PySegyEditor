from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt.SettingWindow.CSGSetting.CSGSettingUi import Ui_CSGSetting
from UiParameter import *


class CSGSetting(QDialog):
    # 定义信号
    signal = QtCore.pyqtSignal(CSGTraceUiParas)

    def __init__(self):
        super().__init__()
        self.ui = Ui_CSGSetting()
        self.ui.setupUi(self)
        # ui设置
        self.ui.comboBox_Depth.addItem("ft")
        # self.ui.comboBox_Depth.addItem("m")
        self.ui.comboBox_Depth.setCurrentIndex(0)

    def ui_update(self, CSG_ALL_LIST):
        for item in CSG_ALL_LIST:
            self.ui.comboBox_DepthEdit.addItem(str(int(item)))

    def accept(self):
        csg_UiParas = CSGTraceUiParas()
        csg_UiParas.depth = int(self.ui.comboBox_DepthEdit.currentText())
        # sourceDepth_Unit = self.ui.comboBox_Depth.currentText()
        csg_UiParas.gain = float(self.ui.GainEdit.text())
        #csg_UiParas.showNum = int(self.ui.ShowNumEdit.text())
        csg_UiParas.bfft = self.ui.checkBox_fft.checkState()
        csg_UiParas.bColorImage = self.ui.checkBox_Color.checkState()
        self.signal.emit(csg_UiParas)
        self.close()
