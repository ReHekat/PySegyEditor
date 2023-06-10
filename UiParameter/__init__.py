"""各种Ui参数

用于各模块和界面之间的参数传递

"""


class BandPassFilterParas:
    """
    Args:
        self.A_stop: 阻带衰减 (dB)
        self.F_stop1: 阻带边缘 (Hz)
        self.F_pass1: 通带边缘 (Hz)
        self.F_pass2: 通带的关闭边缘 (Hz)
        self.F_stop2: 第二个阻带的边缘 (Hz)
        self.A_pass: 通带中允许的纹波量 (dB)
        self.fs: 采样率
    """
    def __init__(self):
        self.A_stop = 60    # 阻带衰减 =  dB
        self.F_stop1 = 50   # 阻带边缘 =  Hz
        self.F_pass1 = 100  # 通带边缘 =  Hz
        self.F_pass2 = 400  # 通带的关闭边缘 = Hz
        self.F_stop2 = 450  # 第二个阻带的边缘 = Hz
        self.A_pass = 0.5  # 通带中允许的纹波量 = dB
        self.fs = 4000   # 采样率


class TraceUiParas:
    """
    Args:
        self.bandPassFilterParas(BandPassFilterParas): 滤波器参数实例
        self.gain(float): wiggle增益Gain
        self.showNum(int): 显示测线数量，超过200会使wiggle图绘制缓慢
        self.bfft(bool): 是否进行fft
        self.bfilter(bool): 是否进行带通滤波
        self.nX(int): 横纵坐标显示数
        self.nY(int):
        self.color(str): 绘制颜色, 默认绘制黑色
        self.bColorImage(bool): 是否绘制Image图
    """
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
    """
    Args:
        self.trace(int): 测线序号，绘制第几条测线
        self.blog(bool): 是否以对数坐标绘制
    """
    def __init__(self):
        super(SingleTraceUiParas, self).__init__()
        self.trace = 1
        self.blog = False


class TracesTraceUiParas(TraceUiParas):
    """
    Args:
        self.firstTrace(int): 测线序号，从第几条测线开始绘制
        self.interval(int): 绘制间隔，每间隔多少条测线绘制一次
    """
    def __init__(self):
        super(TracesTraceUiParas, self).__init__()
        self.firstTrace = 0
        self.interval = 10


class AllTracesTraceUiParas(TraceUiParas):
    """
    绘制所有测线，可以设定只显示其中多少条，以加快wiggle图绘制速度
    """
    def __init__(self):
        super(AllTracesTraceUiParas, self).__init__()


class CRGTraceUiParas(TraceUiParas):
    """
    绘制CRG Wiggle图
    """
    def __init__(self):
        super(CRGTraceUiParas, self).__init__()
        self.depth = 1


class CSGTraceUiParas(TraceUiParas):
    """
    绘制CSG Wiggle图
    """
    def __init__(self):
        super(CSGTraceUiParas, self).__init__()
        self.depth = 1


class ExportAcousticUiParas:
    """
    导出 Acoustic 文件

    Args:
        self.path(str): 导出路径
        self.freqNum(num): 频率点个数
        self.freqList(list): 频率
        self.sourceList(list): 源
        self.receiverList(list): 接收
        self.direction(int): 方向 - 0, 1, 2, 3; 值为0时为Acoustic文件，否则为Elastic文件
    """
    def __init__(self):
        self.path = ""
        self.freqNum = 0
        self.freqList = []
        self.sourceList = []
        self.receiverList = []
        self.direction = 0   # 方向:1, 2, 3 值为0时为Acoustic文件，否则为Elastic文件
