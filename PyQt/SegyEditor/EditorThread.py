from PyQt5.Qt import QThread
from PyQt5 import QtCore
import numpy as np
import segyio
from scipy import signal
from PyQt.SegyEditor.TraceInfo import TracesInfo


class ExportFreqSegyThread(QThread):  # FreqSegy线程
    resSignal = QtCore.pyqtSignal(bool)

    def __init__(self, filePath, srcfile, paras):
        super().__init__()
        self.filePath = filePath
        self.fSegyFile = srcfile
        self.paras = paras
        self.fdt = srcfile.bin[3217] * 1e-6  # the sampling interval

    def run(self):
        src = self.fSegyFile
        spec = segyio.tools.metadata(src)
        # spec.samples = np.linspace(0, 1 / (src.bin[3217] * 1e-6) / 2, 1601)
        spec.samples = np.fft.rfftfreq(len(src.samples), d=src.bin[3217] * 1e-6)
        with segyio.create(self.filePath, spec) as dst:
            dst.text[0] = src.text[0]
            dst.bin = src.bin
            dst.bin = {segyio.BinField.Samples: len(src.samples) // 2 + 1,
                       segyio.BinField.Traces: src.tracecount,
                       segyio.BinField.Interval: int((spec.samples[1] - spec.samples[0]) * 1000)
                       }
            dst.header = src.header
            dst.trace = src.trace[:len(src.samples) // 2 + 1]
            tracesData = segyio.tools.collect(src.trace[:])  # 转换为ndarray 加速计算
            # Filter 处理
            if self.paras.bfilter:
                N, Wn = signal.buttord(
                    [self.paras.bandPassFilterParas.F_pass1, self.paras.bandPassFilterParas.F_pass2],
                    [self.paras.bandPassFilterParas.F_stop1, self.paras.bandPassFilterParas.F_stop2],
                    self.paras.bandPassFilterParas.A_pass, self.paras.bandPassFilterParas.A_stop,
                    analog=False, fs=1 / self.fdt)
                sos = signal.butter(N, Wn, 'bandpass', False, fs=1 / self.fdt, output='sos')
                tracesData = signal.sosfiltfilt(sos, tracesData)  # data为要过滤的信号
            # fft 处理
            dst.trace = np.abs(np.fft.rfft(tracesData))
        # 完成信号
        self.Resematin = True
        self.resSignal.emit(self.Resematin)


class ExportAcousticThread(QThread):  # SegyAcoustic线程
    resSignal = QtCore.pyqtSignal(bool)

    def __init__(self, paras, srcfile):
        super().__init__()
        self.paras = paras
        self.fSegyFile = srcfile

    def run(self):
        src = self.fSegyFile
        paras = self.paras
        direction = paras.direction
        traceInfo = TracesInfo(self.fSegyFile, paras.sourceList, paras.receiverList)
        with open(paras.path, "w") as f:
            # 频率个数
            f.write("     " + str(paras.freqNum))
            f.write("\n")
            # 第n个频率
            for i in range(0, paras.freqNum):
                freq = paras.freqList[i]
                f.write("    " + format(freq, '.4f'))
                f.write("\n")
                # 第i个频率 对应源的个数
                sourceNum = traceInfo.getSourceNum(freq)
                f.write("   " + str(sourceNum))
                f.write("\n")
                # 循环打印所有源
                # 第i个频率 对应第j个源坐标和方向
                for j in range(0, sourceNum):
                    x, y, sourceDepth, receiverNum = traceInfo.getSourceInfo(freq, j)
                    f.write("    " + format(x, '.4f'))
                    f.write("    " + format(y, '.4f'))
                    if direction > 0:
                        f.write(" " + str(direction))
                    f.write("\n")
                    # 第i个频率 第j个源的receiver个数
                    f.write("    " + str(receiverNum))
                    f.write("\n")
                    # 第i个频率 第j个源 第k个接收的坐标、方向、傅里叶系数
                    for k in range(0, receiverNum):
                        x, y, real, imag = traceInfo.getReceiverInfo(sourceDepth, k)
                        # 坐标、方向
                        f.write("    " + format(x, '.4f') + "    " + format(y, '.4f'))
                        if direction > 0:
                            f.write(" " + str(direction))
                        f.write("\n")
                        # 傅里叶系数
                        f.write("  " + format(real, '.8e'))
                        f.write("  " + format(imag, '.8e'))
                        f.write("\n")

            #f.write("    " + )
        # 完成信号
        self.Resematin = True
        self.resSignal.emit(self.Resematin)
