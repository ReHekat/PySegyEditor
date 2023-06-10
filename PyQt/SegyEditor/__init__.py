import segyio
import numpy as np
from PyQt5.QtCore import QCoreApplication
import PyQt.SegyEditor.EditorThread


class SegyEditor:
    def __init__(self):
        super().__init__()
        self.CRG_ALL_LIST = []
        self.CSG_ALL_LIST = []

    def open(self, filePath, ignore_geometry=True):
        self.fSegyFile = segyio.open(filePath, ignore_geometry=ignore_geometry)
        return self.fSegyFile

    def CRG_CSG_init(self):
        # 获取CRG_ALL_LIST，CSG_ALL_LIST:查找所有traceReceiverDepth，traceSourceDepth
        for i in range(0, self.fSegyFile.header.length):
            depth_scalar = self.fSegyFile.header[i][69]
            traceReceiverDepth = self.fSegyFile.header[i][41]
            traceSourceDepth = self.fSegyFile.header[i][45]
            if depth_scalar > 0:
                traceReceiverDepth = traceReceiverDepth * depth_scalar
                traceSourceDepth = traceSourceDepth * depth_scalar
            else:
                traceReceiverDepth = traceReceiverDepth / abs(depth_scalar)
                traceSourceDepth = traceSourceDepth / abs(depth_scalar)
            if traceReceiverDepth not in self.CRG_ALL_LIST:
                self.CRG_ALL_LIST.append(traceReceiverDepth)
            if traceSourceDepth not in self.CSG_ALL_LIST:
                self.CSG_ALL_LIST.append(traceSourceDepth)
        self.CRG_ALL_LIST.sort()
        self.CSG_ALL_LIST.sort()
        return self.CRG_ALL_LIST, self.CSG_ALL_LIST

    # <editor-fold desc="文件导出">

    def export_freq_segy(self, filePath, paras):
        self.resFlag = False
        thread1 = EditorThread.ExportFreqSegyThread(filePath, self.fSegyFile, paras)
        thread1.resSignal.connect(self.resSlot)
        thread1.start()
        while not self.resFlag:
            QCoreApplication.processEvents()

    def export_acoustic(self, paras):
        self.resFlag = False
        thread1 = EditorThread.ExportAcousticThread(paras, self.fSegyFile)
        thread1.resSignal.connect(self.resSlot)
        thread1.start()
        while not self.resFlag:
            QCoreApplication.processEvents()

    # export_elastic函数并未使用，两种文件导出共用 export_acoustic
    def export_elastic(self, paras):
        self.resFlag = False
        self.thread1 = EditorThread.ExportAcousticThread(paras, self.fSegyFile)
        self.thread1.resSignal.connect(self.resSlot)
        self.thread1.start()
        while not self.resFlag:
            QCoreApplication.processEvents()

    def resSlot(self, res):
        self.resFlag = res

    # </editor-fold>
