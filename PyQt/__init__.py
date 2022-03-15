from PyQt5.QtWidgets import QMainWindow, QMessageBox, QFileDialog, QColorDialog
from PyQt5.QtGui import QIntValidator, QColor
import matplotlib
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT
from matplotlib import pyplot
from PyQt.MainWindow import Ui_MainWindow
from PyQt.InfoDialog import InfoDialog
from PyQt.BandPassFilterDialog import BandPassFilterDialog
from PyQt.ExportDialog import ExportDialog
from PyQt.SettingWindow.SingleTraceSetting import SingleTraceSetting
from PyQt.SettingWindow.TracesSetting import TracesSetting
from PyQt.SettingWindow.AllTracesSetting import AllTracesSetting
from PyQt.SettingWindow.CRGSetting import CRGSetting
from PyQt.SettingWindow.CSGSetting import CSGSetting
from PyQt.WaitingDialog import WaitingDialog
from UiParameter import *
import PyQt.SegyEditor
import SeismicPlot
import sip

matplotlib.use('Qt5Agg')
pyplotClear = True  # 清除figure（会拖慢速度，默认false）


def pyplot_clear():
    if pyplotClear:
        pyplot.cla()
        pyplot.close("all")


class SeismicPlotMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 初始化参数
        self.fscale = 1  # 增益
        self.fmode = 'AllTraces'  # 显示模式: Traces, AllTraces, CRG, CSG
        self.fcolor = "#000000"    # 绘制颜色
        self.segyEditor = SegyEditor.SegyEditor()
        self.receiverAllList = []
        self.sourceAllList = []
        # 使用ui文件导入定义界面类
        self.ui = Ui_MainWindow()
        # 初始化Setting子窗口
        self.bandPassFilterDialog = BandPassFilterDialog()
        self.bandPassFilterUiParas = BandPassFilterParas()
        self.singleTraceDialog = SingleTraceSetting()
        self.singleTraceUiParas = SingleTraceUiParas()
        self.tracesDialog = TracesSetting()
        self.tracesUiParas = TracesTraceUiParas()
        self.allTracesDialog = AllTracesSetting()
        self.allTracesUiParas = AllTracesTraceUiParas()
        self.CRGDialog = CRGSetting()
        self.CRGUiParas = CRGTraceUiParas()
        self.CSGDialog = CSGSetting()
        self.CSGUiParas = CSGTraceUiParas()
        # 初始化info子窗口
        self.infoDialog = InfoDialog()
        # 初始化Export子窗口
        self.exportDialog = ExportDialog()
        #self.exportAcousticUiParas = ExportAcousticUiParas()
        # 初始化等待窗口
        self.waitingDialog = WaitingDialog()
        # 初始化界面
        self.ui.setupUi(self)
        self.ui_init(False)
        # 初始化绘图模块
        self.fSegyFilePath = ""
        # 添加事件
        self.ui.pushButton_SingleTrace.clicked.connect(self.pushButton_SingleTrace_clicked)
        self.ui.pushButton_Traces.clicked.connect(self.pushButton_Traces_clicked)
        self.ui.pushButton_AllTraces.clicked.connect(self.pushButton_AllTraces_clicked)
        self.ui.pushButton_CRG.clicked.connect(self.pushButton_CRG_clicked)
        self.ui.pushButton_CSG.clicked.connect(self.pushButton_CSG_clicked)
        self.ui.okButton.clicked.connect(self.okButton_clicked)
        self.ui.pushButton_color.clicked.connect(self.colorButton_clicked)
        self.ui.checkBox_filter.stateChanged.connect(self.filterCheck_changed)
        self.ui.actionOpen.triggered.connect(self.openFile)
        self.ui.actionInfo.triggered.connect(self.info)
        self.ui.action_Freq_Segy.triggered.connect(self.exportFreq)
        self.ui.actionAcoustic.triggered.connect(self.exportAcoustic)
        self.ui.actionElastic.triggered.connect(self.exportElastic)

    # <editor-fold desc="UI函数">
    def ui_init(self, enable):
        # 初始化按钮
        self.ui.actionOpen.setEnabled(not enable)
        #self.ui.lineEdit.setValidator(QIntValidator(0, 99))
        self.ui.lineEdit_nX.setValidator(QIntValidator(0, 500))
        self.ui.lineEdit_nY.setValidator(QIntValidator(0, 500))
        self.ui.okButton.setEnabled(enable)
        self.ui.pushButton_SingleTrace.setEnabled(enable)
        self.ui.pushButton_CRG.setEnabled(enable)
        self.ui.pushButton_AllTraces.setEnabled(enable)
        self.ui.pushButton_CSG.setEnabled(enable)
        self.ui.pushButton_Traces.setEnabled(enable)
        self.ui.pushButton_color.setEnabled(enable)
        self.ui.checkBox_filter.setEnabled(enable)
        self.ui.actionInfo.setEnabled(enable)
        self.ui.menuExport.setEnabled(enable)

    def plot_update(self):
        # 刷新参数
        self.para_update()
        # 刷新UI
        self.ui_update()
        # 调用显示
        if self.fmode == 'SingleTrace':
            self.singleTrace_show()
        elif self.fmode == 'Traces':
            self.traces_show()
        elif self.fmode == 'AllTraces':
            self.allTraces_show()
        elif self.fmode == 'CRG':
            self.CRG_show()
        elif self.fmode == 'CSG':
            self.CSG_show()
        else:
            raise Exception('fmode Error')

    def para_update(self):
        paras = self.getCurrentParas()
        paras.bfilter = self.ui.checkBox_filter.checkState()
        paras.gain = self.fscale
        paras.color = self.fcolor
        paras.nX = int(self.ui.lineEdit_nX.text())
        paras.nY = int(self.ui.lineEdit_nY.text())

    def ui_update(self):
        # update Scale(Gain)
        scale = str(self.fscale)
        self.ui.lineEdit.setText(scale)
        if self.fmode == 'Traces':
            self.tracesDialog.ui.GainEdit.setText(scale)
        elif self.fmode == 'AllTraces':
            self.allTracesDialog.ui.GainEdit.setText(scale)
        elif self.fmode == 'CRG':
            self.CRGDialog.ui.GainEdit.setText(scale)
        elif self.fmode == 'CSG':
            self.CSGDialog.ui.GainEdit.setText(scale)

    # </editor-fold>

    # <editor-fold desc="SeismicPlot函数">
    def SeismicInit(self, scale):
        pyplot_clear()
        self.F = SeismicPlot.SEGYProcess(self.fSegyFile)
        self.F.set_scale(scale)
        self.mpl_ntb = NavigationToolbar2QT(self.F, self)
        self.ui.horizontalLayout_3.addWidget(self.mpl_ntb)
        self.ui.gridLayout_1.addWidget(self.F)

    def singleTrace_show(self):
        sip.delete(self.F)
        sip.delete(self.mpl_ntb)
        self.SeismicInit(self.fscale)
        self.F.plot_singleTrace_wiggle(self.singleTraceUiParas)

    def traces_show(self):
        sip.delete(self.F)
        sip.delete(self.mpl_ntb)
        self.SeismicInit(self.fscale)
        self.F.plot_traces_wiggle(self.tracesUiParas)

    def allTraces_show(self):
        sip.delete(self.F)
        sip.delete(self.mpl_ntb)
        self.SeismicInit(self.fscale)
        self.F.plot_allTraces_wiggle(self.allTracesUiParas)

    def CRG_show(self):
        sip.delete(self.F)
        sip.delete(self.mpl_ntb)
        self.SeismicInit(self.fscale)
        self.F.plotCRG(self.CRGUiParas)

    def CSG_show(self):
        sip.delete(self.F)
        sip.delete(self.mpl_ntb)
        self.SeismicInit(self.fscale)
        self.F.plotCSG(self.CSGUiParas)
    # </editor-fold>

    # <editor-fold desc="信号槽函数">
    # 信号槽函数
    # <editor-fold desc="主界面信号槽函数">
    def openFile(self):
        self.fSegyFilePath = QFileDialog.getOpenFileName(self, '选择文件', '', 'Segy files(*.segy)')
        if len(self.fSegyFilePath[0]) > 1:
            try:
                self.fSegyFile = self.segyEditor.open(self.fSegyFilePath[0], ignore_geometry=True)
            except IOError:
                QMessageBox.critical(self, "Error", "文件打开失败")
                self.ui_init(False)
            else:
                self.SeismicInit(self.fscale)
                # 激活按钮
                self.ui_init(True)
                # 弹出提示框
                self.infoDialog.ui.label_inlines.setText(str(self.fSegyFile.ilines))
                self.infoDialog.ui.label_crosslines.setText(str(self.fSegyFile.xlines))
                self.infoDialog.ui.label_interval.setText(str(self.fSegyFile.header[0][117]))
                self.infoDialog.ui.label_samples.setText(str(self.fSegyFile.header[0][115]))
                self.infoDialog.ui.label_traces.setText(str(self.fSegyFile.tracecount))
                self.infoDialog.show()
                # 初始化CRG,CSG列表
                self.receiverAllList, self.sourceAllList = self.segyEditor.CRG_CSG_init()
                # 初始化CRG,CSG选项框
                self.CRGDialog.ui_update(self.receiverAllList)
                self.CSGDialog.ui_update(self.sourceAllList)

    def exportFreq(self):
        self.fSegyFilePath = QFileDialog.getSaveFileName(self, '选择文件', '', 'Segy files(*.segy)')
        if len(self.fSegyFilePath[0]) > 1:
            self.waitingDialog.show()
            try:
                self.segyEditor.export_freq_segy(self.fSegyFilePath[0], self.getCurrentParas())
            except IOError:
                QMessageBox.critical(self, "Error", "文件导出失败")
            else:
                pass
            self.waitingDialog.close()

    def exportAcoustic(self):
        self.exportDialog.show()
        self.exportDialog.ui_update("acoustic", self.sourceAllList, self.receiverAllList)
        # 连接信号
        self.exportDialog.signal.connect(self.exportAcoustic_ok_clicked)

    def exportElastic(self):
        self.exportDialog.show()
        self.exportDialog.ui_update("elastic", self.sourceAllList, self.receiverAllList)
        # 连接信号
        self.exportDialog.signal.connect(self.exportAcoustic_ok_clicked)

    def info(self):
        self.infoDialog.show()

    def pushButton_SingleTrace_clicked(self):
        self.singleTraceDialog.show()
        # 连接信号
        self.singleTraceDialog.signal.connect(self.singleTrace_ok_clicked)

    def pushButton_Traces_clicked(self):
        self.tracesDialog.show()
        # 连接信号
        self.tracesDialog.signal.connect(self.traces_ok_clicked)

    def pushButton_AllTraces_clicked(self):
        self.allTracesDialog.show()
        # 连接信号
        self.allTracesDialog.signal.connect(self.allTraces_ok_clicked)

    def pushButton_CRG_clicked(self):
        self.CRGDialog.show()
        # 连接信号
        self.CRGDialog.signal.connect(self.CRG_ok_clicked)

    def pushButton_CSG_clicked(self):
        self.CSGDialog.show()
        # 连接信号
        self.CSGDialog.signal.connect(self.CSG_ok_clicked)

    def okButton_clicked(self):
        scale = self.ui.lineEdit.text()
        if len(scale) == 0 or len(self.ui.lineEdit_nX.text()) == 0 or len(self.ui.lineEdit_nY.text()) == 0:
            QMessageBox.critical(self, "Error", "参数不允许为空")
            return
        else:
            self.fscale = float(scale)
        # 刷新显示
        self.plot_update()

    def colorButton_clicked(self):
        col = QColorDialog.getColor(QColor(self.fcolor), self)   # 新建颜色对话框
        if col.isValid():
            self.fcolor = col.name()
            # 刷新显示
            self.plot_update()

    def filterCheck_changed(self):
        paras = self.getCurrentParas()
        paras.bfilter = self.ui.checkBox_filter.checkState()
        if paras.bfilter:
            # 连接信号
            self.bandPassFilterDialog.signal.connect(self.filter_ok_clicked)
            state = self.bandPassFilterDialog.exec()
            if not state:
                self.ui.checkBox_filter.setCheckState(not self.ui.checkBox_filter.checkState())
                paras.bfilter = self.ui.checkBox_filter.checkState()
        else:
            self.plot_update()
    # </editor-fold>

    # <editor-fold desc="子界面信号槽函数">
    def singleTrace_ok_clicked(self, singleTraceUiParas):
        self.fmode = 'SingleTrace'
        self.singleTraceUiParas = singleTraceUiParas
        self.plot_update()

    def traces_ok_clicked(self, tracesUiParas):
        self.fmode = 'Traces'
        self.fscale = tracesUiParas.gain
        self.tracesUiParas = tracesUiParas
        self.plot_update()

    def allTraces_ok_clicked(self, allTracesUiParas):
        self.fmode = 'AllTraces'
        self.fscale = allTracesUiParas.gain
        self.allTracesUiParas = allTracesUiParas
        self.plot_update()

    def CRG_ok_clicked(self, CRG_UiParas):
        self.fmode = 'CRG'
        self.fscale = CRG_UiParas.gain
        self.CRGUiParas = CRG_UiParas
        self.plot_update()

    def CSG_ok_clicked(self, CSG_UiParas):
        self.fmode = 'CSG'
        self.fscale = CSG_UiParas.gain
        self.CSGUiParas = CSG_UiParas
        self.plot_update()

    def filter_ok_clicked(self, filter_UiParas):
        self.bandPassFilterUiParas = filter_UiParas
        if self.ui.checkBox_filter.checkState():
            self.plot_update()

    def exportAcoustic_ok_clicked(self, acoustic_UiParas):
        if len(acoustic_UiParas.path) > 1:
            self.waitingDialog.show()
            try:
                self.segyEditor.export_acoustic(acoustic_UiParas)
            except IOError:
                QMessageBox.critical(self, "Error", "文件导出失败")
            else:
                pass
            self.waitingDialog.close()
    # </editor-fold>
    # </editor-fold>

    def getCurrentParas(self):
        if self.fmode == 'SingleTrace':
            paras = self.singleTraceUiParas
        elif self.fmode == 'Traces':
            paras = self.tracesUiParas
        elif self.fmode == 'AllTraces':
            paras = self.allTracesUiParas
        elif self.fmode == 'CRG':
            paras = self.CRGUiParas
        elif self.fmode == 'CSG':
            paras = self.CSGUiParas
        else:
            raise Exception('fmode Error')
        return paras

#if __name__ == '__main__':
#    app = QApplication([])
#    mainWindow = SeismicPlotMainWindow()
#    mainWindow.show()
#    app.exec_()
