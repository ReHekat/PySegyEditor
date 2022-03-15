from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import QMovie
from PyQt.WaitingDialog.WaitingDialog import Ui_Dialog_Wating


class WaitingDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog_Wating()
        self.ui.setupUi(self)

        # 设置透明度
        self.setWindowOpacity(0.9)
        # 无边框窗口 窗口置顶
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        # 设置模态 应用窗口模式
        self.setWindowModality(QtCore.Qt.ApplicationModal)

        self.ui.label_movie.setStyleSheet("background-color: transparent")
        self.m_movie = QMovie("./Resource/waiting.gif")
        self.ui.label_movie.setMovie(self.m_movie)
        self.ui.label_movie.setScaledContents(True)
        self.m_movie.start()

    def __del__(self):
        self.m_movie.stop()
