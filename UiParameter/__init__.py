class BandPassFilterParas:
    def __init__(self):
        self.A_stop = 60    # 阻带衰减 =  dB
        self.F_stop1 = 50   # 阻带边缘 =  Hz
        self.F_pass1 = 100  # 通带边缘 =  Hz
        self.F_pass2 = 400  # 通带的关闭边缘 = Hz
        self.F_stop2 = 450  # 第二个阻带的边缘 = Hz
        self.A_pass = 0.5  # 通带中允许的纹波量 = dB
        self.fs = 4000   # 采样率


class TraceUiParas:
    def __init__(self):
        self.bandPassFilterParas = BandPassFilterParas()  # 滤波器参数实例
        self.gain = 1
        self.showNum = 0  # 0则全部显示
        self.bfft = False  # 是否进行fft
        self.bfilter = False  # 是否进行带通滤波
        self.nX = 10  # 横纵坐标显示数
        self.nY = 10
        self.color = 'k'    # 默认绘制黑色
        self.bColorImage = False


class SingleTraceUiParas(TraceUiParas):
    def __init__(self):
        super(SingleTraceUiParas, self).__init__()
        self.trace = 1
        self.blog = False


class TracesTraceUiParas(TraceUiParas):
    def __init__(self):
        super(TracesTraceUiParas, self).__init__()
        self.firstTrace = 0
        self.interval = 10


class AllTracesTraceUiParas(TraceUiParas):
    def __init__(self):
        super(AllTracesTraceUiParas, self).__init__()


class CRGTraceUiParas(TraceUiParas):
    def __init__(self):
        super(CRGTraceUiParas, self).__init__()
        self.depth = 1


class CSGTraceUiParas(TraceUiParas):
    def __init__(self):
        super(CSGTraceUiParas, self).__init__()
        self.depth = 1


class ExportAcousticUiParas:
    def __init__(self):
        self.path = ""
        self.freqNum = 0
        self.freqList = []
        self.sourceList = []
        self.receiverList = []
        self.direction = 0   # 方向:1, 2, 3 值为0时为Acoustic文件，否则为Elastic文件
