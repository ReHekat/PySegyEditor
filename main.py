from PyQt5.QtWidgets import QApplication
from PyQt import SeismicPlotMainWindow
from PyQt5 import QtCore
'''
    优化方向：
    1.载入segy文件至内存中，segyio直接操作内存虚拟io
    2.crg、csg直接使用初始化时的list
'''
if __name__ == '__main__':
    # 适应高DPI设备
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

    app = QApplication([])
    mainWindow = SeismicPlotMainWindow()
    mainWindow.show()
    app.exec_()
