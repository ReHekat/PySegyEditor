import numpy as np
import segyio
from scipy import signal


class TracesInfo:
    def __init__(self, segy, sourceList, receiverList):
        self.segyFile = segy
        self.sourceList = sourceList
        self.receiverList = receiverList
        self.minX = self.segyFile.header[0][73]
        self.minY = self.segyFile.header[0][77]
        self.tracesIndex = []         # 符合选定范围的traces索引
        self.sourceTraceIndexDict = {}     # 源depth-测线序号列表 索引
        self.receiverIndexDict = {}   # 接收depth-测线序号列表 索引
        self.source_Freq_SourceDepth = {}   # 某频率对应的源depth列表 索引
        self.receiver_Source_ReceiverDepth = {}  # 某源对应的接收depth列表 索引
        # 频率
        tracesData = segyio.tools.collect(segy.trace[:])  # 转换为ndarray 加速计算
        self.fft_abs = np.abs(np.fft.rfft(tracesData))
        self.fft_freq = np.fft.rfftfreq(len(segy.samples), d=segy.bin[3217] * 1e-6)
        self.freqIndex = 0
        # 初始化源、接收字典
        for traceSourceDepth in sourceList:
            self.sourceTraceIndexDict[traceSourceDepth] = []
        for traceReceiverDepth in receiverList:
            self.receiverIndexDict[traceReceiverDepth] = []
        # 查找 source == source_depth 的trace
        for i in range(0, self.segyFile.header.length):
            depth_scalar = self.segyFile.header[i][69]
            traceReceiverDepth = self.segyFile.header[i][41]
            traceSourceDepth = self.segyFile.header[i][45]
            if depth_scalar > 0:
                traceReceiverDepth = traceReceiverDepth * depth_scalar
                traceSourceDepth = traceSourceDepth * depth_scalar
            else:
                traceReceiverDepth = traceReceiverDepth / abs(depth_scalar)
                traceSourceDepth = traceSourceDepth / abs(depth_scalar)
            if traceSourceDepth in sourceList and traceReceiverDepth in receiverList:
                self.tracesIndex.append(i)
                self.sourceTraceIndexDict[traceSourceDepth].append(i)
                self.receiverIndexDict[traceReceiverDepth].append(i)
            # 初始化相对坐标点
            sX = self.segyFile.header[i][73]
            sY = self.segyFile.header[i][77]
            rX = self.segyFile.header[i][81]
            rY = self.segyFile.header[i][85]
            x = sX if sX < rX else rX
            y = sY if sY < rY else rY
            self.minX = x if x < self.minX else self.minX
            self.minY = y if y < self.minY else self.minY

    def getSourceNum(self, freq):
        # 根据频率 返回源的个数
        sourceDepthList = []     # 保存源depth信息
        for i in self.tracesIndex:
            freqIndexList = np.where(self.fft_freq > freq)
            if len(freqIndexList) > 0:
                freqIndex = freqIndexList[0][0]
                preFreq = self.fft_freq[freqIndex - 1]
                curFreq = self.fft_freq[freqIndex]
                tempPreFreq = freq - preFreq
                tempCurFreq = curFreq - freq
                freqIndex = freqIndex if tempCurFreq < tempPreFreq else freqIndex - 1
            else:
                break
            if freqIndex >= 0 and abs(self.fft_freq[freqIndex] - freq) < 0.3 and self.fft_abs[i, freqIndex] > 0:
                self.freqIndex = freqIndex
                depth_scalar = self.segyFile.header[i][69]
                traceReceiverDepth = self.segyFile.header[i][41]
                traceSourceDepth = self.segyFile.header[i][45]
                if depth_scalar > 0:
                    traceReceiverDepth = traceReceiverDepth * depth_scalar
                    traceSourceDepth = traceSourceDepth * depth_scalar
                else:
                    traceReceiverDepth = traceReceiverDepth / abs(depth_scalar)
                    traceSourceDepth = traceSourceDepth / abs(depth_scalar)
                if traceSourceDepth not in sourceDepthList:
                    sourceDepthList.append(traceSourceDepth)
        sourceNum = len(sourceDepthList)
        self.source_Freq_SourceDepth[freq] = sourceDepthList
        return sourceNum

    def getSourceInfo(self, freq, index):
        # 根据频率 获取该频率第index个源的位置, 深度, 检波器个数
        receiverDepthList = []
        freqSourceDepths = self.source_Freq_SourceDepth[freq]  # 列表
        sourceDepth = freqSourceDepths[index]
        sourceTracesIndex = self.sourceTraceIndexDict[sourceDepth]
        header = self.segyFile.header[sourceTracesIndex[0]]  # 列表
        x = header[73] - self.minX
        y = header[77] - self.minY
        # 查找 receiver == receiver_depth 的trace
        for i in sourceTracesIndex:
            depth_scalar = self.segyFile.header[i][69]
            traceReceiverDepth = self.segyFile.header[i][41]
            traceSourceDepth = self.segyFile.header[i][45]
            if depth_scalar > 0:
                traceReceiverDepth = traceReceiverDepth * depth_scalar
                traceSourceDepth = traceSourceDepth * depth_scalar
            else:
                traceReceiverDepth = traceReceiverDepth / abs(depth_scalar)
                traceSourceDepth = traceSourceDepth / abs(depth_scalar)
            if traceReceiverDepth not in receiverDepthList:
                receiverDepthList.append(traceReceiverDepth)
        self.receiver_Source_ReceiverDepth[sourceDepth] = receiverDepthList
        receiverNum = len(receiverDepthList)
        return x, y, sourceDepth, receiverNum

    def getReceiverInfo(self, sourceDepth, index):
        # 根据源深度，获取对应第index个检波器的位置和场值列表
        receiverDepthList = self.receiver_Source_ReceiverDepth[sourceDepth]
        receiverDepth = receiverDepthList[index]
        tracesIndex = self.receiverIndexDict[receiverDepth]
        depth_scalar = self.segyFile.header[0][69]
        j = 0
        for i in tracesIndex:
            traceSourceDepth = self.segyFile.header[i][45]
            if depth_scalar > 0:
                traceSourceDepth = traceSourceDepth * depth_scalar
            else:
                traceSourceDepth = traceSourceDepth / abs(depth_scalar)
            if sourceDepth == traceSourceDepth:
                j = i
                break
        trace = self.segyFile.trace[j]
        header = self.segyFile.header[j]
        x = header[81] - self.minX
        y = header[85] - self.minY
        fft = np.fft.rfft(trace)
        real = np.real(fft)[self.freqIndex]
        imag = np.imag(fft)[self.freqIndex]
        return x, y, real, imag
