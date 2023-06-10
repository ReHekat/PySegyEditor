"""程序入口

基于PyQt5的SEGY文件的查看器与编辑器，支持：
    1.SEGY 2D显示与编辑(基于Matplotlib).
    2.Filter滤波处理.
    3.CRG、CSG显示.
    4.FFT变换.
    5.数据导出.

优化方向：
    1.载入segy文件至内存中，segyio直接操作内存虚拟io.
    2.crg、csg直接使用初始化时的list.
    3.主界面的Matplotlib绘制窗口，可以阅读时域电磁模拟客户端代码，对窗口的加载流程进行了优化.
"""
from PyQt5.QtWidgets import QApplication
from PyQt import SeismicPlotMainWindow
from PyQt5 import QtCore

if __name__ == '__main__':
    # 适应高DPI设备
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

    app = QApplication([])
    mainWindow = SeismicPlotMainWindow()
    mainWindow.show()
    app.exec_()
