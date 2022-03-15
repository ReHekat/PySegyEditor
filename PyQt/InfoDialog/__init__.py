from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt.InfoDialog.Dialog_info import Ui_Dialog_info


class InfoDialog(QDialog):
    # 定义信号
    #signal = QtCore.pyqtSignal(AllTracesUiParas)

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog_info()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.accept)
