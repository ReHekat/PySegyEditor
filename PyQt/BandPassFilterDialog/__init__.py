from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt.BandPassFilterDialog.BandPassFilterDialog import Ui_BandPassFilterDialog
from UiParameter import BandPassFilterParas


class BandPassFilterDialog(QDialog):
    # 定义信号
    signal = QtCore.pyqtSignal(BandPassFilterParas)

    def __init__(self):
        super().__init__()
        self.ui = Ui_BandPassFilterDialog()
        self.ui.setupUi(self)
        # 设置示例图片
        self.ui.label_jpg.setPixmap(QtGui.QPixmap('./Resource/bandpass.jpg'))

    def accept(self):
        super(BandPassFilterDialog, self).accept()
        bandPassFilterParas = BandPassFilterParas()
        bandPassFilterParas.A_stop = float(self.ui.lineEdit_A_stop.text())
        bandPassFilterParas.F_stop1 = float(self.ui.lineEdit_F_stop1.text())
        bandPassFilterParas.F_pass1 = float(self.ui.lineEdit_F_pass1.text())
        bandPassFilterParas.F_pass2 = float(self.ui.lineEdit_F_pass2.text())
        bandPassFilterParas.F_stop2 = float(self.ui.lineEdit_F_stop2.text())
        bandPassFilterParas.A_pass = float(self.ui.lineEdit_A_pass.text())
        bandPassFilterParas.fs = float(self.ui.lineEdit_fs.text())
        self.signal.emit(bandPassFilterParas)
