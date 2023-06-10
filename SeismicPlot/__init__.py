"""SEGY剖面绘制模块

继承自``FigureCanvasQTAgg``的SEGY剖面绘制模块

用法:
  self.F = SeismicPlot.SEGYProcess(self.fSegyFile)
  self.F.set_scale(scale)
"""
import numpy as np
from matplotlib import pyplot
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from scipy import signal
import segyio
from UiParameter import *


class SEGYProcess(FigureCanvas):
    def __init__(self, segyFile):
        """
        初始化SEGY处理程序.

        Args:
            segyFile(str): segy文件路径.
        """
        self.fsegyfile = segyFile  # segyio
        self.fscale = 1  #
        self.fdt = self.fsegyfile.bin[3217] * 1e-6    # the sampling interval

        self.fig = pyplot.figure()
        self.pltList = []
        super(SEGYProcess, self).__init__(self.fig)

    def set_dt(self, dt):
        """
        设置采样率dt参数.

        Args:
            dt(float): 采样率 - sample rate in seconds.

        """
        self.fdt = dt

    def set_scale(self, scale):
        """
        设置缩放倍率.

        Args:
            scale(float): 缩放倍率.

        """
        self.fscale = scale

    def set_color(self, color):
        """设置绘制颜色.

        尚未实现.

        Args:
            color(str): 十六进制的颜色字符串，如 #abff4b.

        """
        pass
        # print("")
        # print(len(self.pltList))
        # print(len(self.pltList[0]))
        # for l in self.pltList:
        #     l[0].set_color(color)

    def seismic_image(self, section, ranges=None, cmap=pyplot.cm.seismic,
                      aspect=None, vmin=None, vmax=None, fft=False):
        """
        Plot a seismic section (numpy 2D array matrix) as an image.

        Args:
            section(2D array):  matrix of traces (first dimension time, second dimension traces).
            ranges((x1, x2)): min and max horizontal coordinate values (default trace number).
            cmap(colormap): color map to be used. (see pyplot.cm module)
            aspect(float): matplotlib imshow aspect parameter, ratio between axes.
            vmin(float): min values for imshow.
            vmax(float): max values for imshow.
            fft(bool): 是否使用fft变换 (True - 频域图, False - 时域图)

        """
        npts, maxtraces = section.shape  # time/traces
        if maxtraces < 1:
            raise IndexError("Nothing to plot")
        if npts < 1:
            raise IndexError("Nothing to plot")
        # fft处理
        if fft:
            t = np.linspace(0, 1 / self.fdt / 2, npts)
            pyplot.yticks(np.arange(section.shape[0]), t.astype(int))
            pyplot.ylabel('Freq (Hz)')
        else:
            pyplot.ylabel('Time (s)')
            t = np.linspace(0, self.fdt * npts, npts)
            pyplot.yticks(np.arange(section.shape[0]), np.around(t, 3))
        data = section
        if ranges is None:
            ranges = (0, maxtraces)
        x0, x1 = ranges
        extent = (x0, x1, t[-1:], t[0])
        if aspect is None:  # guarantee a rectangular picture
            aspect = np.round((x1 - x0) / np.max(t))
            aspect -= aspect * 0.2
        if vmin is None and vmax is None:
            scale = np.abs([section.max(), section.min()]).max()
            vmin = -scale
            vmax = scale

        #pyplot.ylim(max(t), 0)
        #pyplot.yticks(np.arange(data.shape[0]), t.astype(int))
        #pyplot.locator_params(axis='y', nbins=10)  # y轴标签显示数量
        #pyplot.imshow(data, aspect=aspect, cmap=cmap, origin='upper', vmin=vmin, vmax=vmax)
        pyplot.imshow(data, aspect='auto', cmap=cmap, origin='upper', vmin=vmin, vmax=vmax, interpolation='bilinear')
        pyplot.colorbar()
        self.fig.canvas.mpl_connect('button_press_event', self.onclick)

    def onclick(self, event):
        """
        忘记干啥用的了，意义不明，也许是调试的时候用的

        Args:
            event:

        """
        print(event.xdata, event.ydata)
        #self.coordinates.extend([event.xdata, event.ydata])

    def seismic_wiggle(self, section, ranges=None, color='k',
                       normalize=False):
        """绘制seismic wiggle.(已弃用，该函数为 ``plot_traces_wiggle`` 的原型)

        Plot a seismic section (numpy 2D array matrix) as wiggles.

        Args:
            section(2D array): matrix of traces (first dimension time, second dimension traces)
            ranges: 暂不使用，与traceRange冲突. (min and max horizontal values (default trace number))
            color: Color for filling the wiggle, positive  and negative lobes.
            normalize: True to normalizes all trace in the section using global max/min
                data will be in the range (-0.5, 0.5) zero centered

        .. warning::
            Slow for more than 200 traces, in this case decimate your
            data or use ``seismic_image``.
        """
        npts, ntraces = section.shape  # time/traces
        if ntraces < 1:
            raise IndexError("Nothing to plot")
        if npts < 1:
            raise IndexError("Nothing to plot")
        t = np.linspace(0, self.fdt * npts, npts)
        amp = 1.  # normalization factor
        gmin = 0.  # global minimum
        toffset = 0.  # offset in time to make 0 centered
        if normalize:
            gmax = section.max()
            gmin = section.min()
            amp = (gmax - gmin)
            toffset = 0.5
        pyplot.ylim(max(t), 0)
        if ranges is None:
            ranges = (0, ntraces)
        x0, x1 = ranges
        # horizontal increment
        dx = (x1 - x0)/ntraces
        pyplot.xlim(x0, x1)
        for i, trace in enumerate(section.transpose()):
            tr = (((trace - gmin)/amp) - toffset) * self.fscale * dx
            x = x0 + i*dx  # x positon for this trace
            pyplot.plot(x + tr, t, 'k')
            pyplot.fill_betweenx(t, x + tr, x, tr > 0, color=color)

    def plot_singleTrace_wiggle(self, singeTraceUiParas):
        """
        绘制单条测线的wiggle图

        Args:
            singeTraceUiParas(SingleTraceUiParas): 测线参数

        Returns:
            None
        """
        pyplot.locator_params(axis='x', nbins=singeTraceUiParas.nX)  # x轴标签显示数量
        pyplot.locator_params(axis='y', nbins=singeTraceUiParas.nY)  # y轴标签显示数量
        npts = len(self.fsegyfile.samples)
        traceData = self.fsegyfile.trace[singeTraceUiParas.trace]
        # Filter 处理
        if singeTraceUiParas.bfilter:
            N, Wn = signal.buttord([singeTraceUiParas.bandPassFilterParas.F_pass1, singeTraceUiParas.bandPassFilterParas.F_pass2],
                                   [singeTraceUiParas.bandPassFilterParas.F_stop1, singeTraceUiParas.bandPassFilterParas.F_stop2],
                                   singeTraceUiParas.bandPassFilterParas.A_pass, singeTraceUiParas.bandPassFilterParas.A_stop,
                                   analog=False, fs=1/self.fdt)
            sos = signal.butter(N, Wn, 'bandpass', False, fs=1/self.fdt, output='sos')
            traceData = signal.sosfiltfilt(sos, traceData)  # data为要过滤的信号

        # fft处理
        if singeTraceUiParas.bfft:
            trace_fft = (np.abs(np.fft.rfft(traceData)[:]))
            x = np.fft.rfftfreq(npts, d=self.fdt)
            pyplot.xlabel('Freq (Hz)')
            pyplot.plot(x, trace_fft, color=singeTraceUiParas.color)
        else:
            pyplot.xlabel('Time (s)')
            x = np.linspace(0, self.fdt * npts, npts)
            pyplot.plot(x, traceData, color=singeTraceUiParas.color)

    def plot_traces_wiggle(self, tracesUiParas, ranges=None, normalize=False):
        """绘制seismic wiggle.

        Plot a seismic section (numpy 2D array matrix) as wiggles.

        Args:
            tracesUiParas(TracesTraceUiParas): 测线参数
            ranges: 暂不使用，与traceRange冲突. (min and max horizontal values (default trace number))
            normalize: True to normalizes all trace in the section using global max/min
                data will be in the range (-0.5, 0.5) zero centered

        .. warning::
            Slow for more than 200 traces, in this case decimate your
            data or use ``seismic_image``.
        """
        tracesUiParas.showNum = (self.fsegyfile.tracecount - tracesUiParas.firstTrace) // tracesUiParas.interval
        if tracesUiParas.showNum < 0:
            raise IndexError("showNum Error, Nothing to plot")
        elif tracesUiParas.showNum == 0:
            section = self.fsegyfile.trace.raw[:]
            _x_ticks_len = section.shape[0]
            _x_ticks = np.zeros(_x_ticks_len)
        else:
            _x_ticks = np.zeros(tracesUiParas.showNum)
            _x_ticks_len = tracesUiParas.showNum
            section = np.zeros((tracesUiParas.showNum, len(self.fsegyfile.samples)))
            section_tmp = self.fsegyfile.trace.raw[:]
            for i in range(0, tracesUiParas.showNum):
                section[i] = section_tmp[i * tracesUiParas.interval]
                _x_ticks[i] = int(i * tracesUiParas.interval)
        # filter处理
        section = self._filter(tracesUiParas, section)
        # fft处理
        if tracesUiParas.bfft:
            section = self._fftPlot(tracesUiParas, section)
        pyplot.xlabel('Trace Number')
        section = section.T
        if tracesUiParas.bColorImage:
            self.seismic_image(section, fft=tracesUiParas.bfft)
            pyplot.xticks(np.arange(_x_ticks_len), _x_ticks.astype(int))
            pyplot.locator_params(axis='x', nbins=tracesUiParas.nX)  # x轴标签显示数量
            pyplot.locator_params(axis='y', nbins=tracesUiParas.nY)  # y轴标签显示数量
        else:
            self.fscale = tracesUiParas.gain
            npts, ntraces = section.shape  # time/traces
            if ntraces < 1:
                raise IndexError("Nothing to plot")
            if npts < 1:
                raise IndexError("Nothing to plot")
            # fft处理
            if tracesUiParas.bfft:
                t = np.linspace(0, 1 / self.fdt / 2, npts)
                pyplot.ylabel('Freq (Hz)')
            else:
                pyplot.ylabel('Time (s)')
                t = np.linspace(0, self.fdt * npts, npts)
            amp = 1.  # normalization factor
            gmin = 0.  # global minimum
            toffset = 0.  # offset in time to make 0 centered
            if normalize:
                gmax = section.max()
                gmin = section.min()
                amp = (gmax - gmin)
                toffset = 0.5
            pyplot.ylim(max(t), 0)
            if ranges is None:
                ranges = (0, ntraces)
            x0, x1 = ranges
            # horizontal increment
            dx = (x1 - x0)/ntraces
            pyplot.xlim(x0, x1)
            pyplot.xticks(np.arange(tracesUiParas.showNum), _x_ticks.astype(int))
            pyplot.locator_params(axis='x', nbins=tracesUiParas.nX)   # x轴标签显示数量
            pyplot.locator_params(axis='y', nbins=tracesUiParas.nY)  # y轴标签显示数量
            for i, trace in enumerate(section.transpose()):
                tr = (((trace - gmin)/amp) - toffset) * self.fscale * dx
                x = x0 + i*dx  # x positon for this trace
                pyplot.plot(x + tr, t, color=tracesUiParas.color)
                if not tracesUiParas.bfft:
                    pyplot.fill_betweenx(t, x + tr, x, tr > 0, color=tracesUiParas.color)

    def plot_allTraces_wiggle(self, tracesUiParas, ranges=None, normalize=False):
        """绘制seismic wiggle.

        Plot a seismic section (numpy 2D array matrix) as wiggles.

        Args:
            tracesUiParas(TracesTraceUiParas): 测线参数
            ranges: 暂不使用，与traceRange冲突. (min and max horizontal values (default trace number))
            normalize: True to normalizes all trace in the section using global max/min
                data will be in the range (-0.5, 0.5) zero centered

        .. warning::
            Slow for more than 200 traces, in this case decimate your
            data or use ``seismic_image``.
        """
        if tracesUiParas.showNum < 0:
            raise IndexError("showNum Error, Nothing to plot")
        elif tracesUiParas.showNum == 0:
            section = self.fsegyfile.trace.raw[:]
            _x_ticks_len = section.shape[0]
            _x_ticks = np.zeros(_x_ticks_len)
        else:
            _x_ticks = np.zeros(tracesUiParas.showNum)
            _x_ticks_len = tracesUiParas.showNum
            section = np.zeros((tracesUiParas.showNum, len(self.fsegyfile.samples)))
            section_tmp = self.fsegyfile.trace.raw[:]
            interval = int(self.fsegyfile.tracecount / tracesUiParas.showNum)
            for i in range(0, tracesUiParas.showNum):
                section[i] = section_tmp[i * interval]
                _x_ticks[i] = int(i * interval)
        # filter处理
        section = self._filter(tracesUiParas, section)
        # fft处理
        if tracesUiParas.bfft:
            section = self._fftPlot(tracesUiParas, section)
        section = section.T
        pyplot.xlabel('Trace Number')
        if tracesUiParas.bColorImage:
            self.seismic_image(section, fft=tracesUiParas.bfft)
            pyplot.xticks(np.arange(_x_ticks_len), _x_ticks.astype(int))
            pyplot.locator_params(axis='x', nbins=tracesUiParas.nX)  # x轴标签显示数量
            pyplot.locator_params(axis='y', nbins=tracesUiParas.nY)  # y轴标签显示数量
        else:
            self.fscale = tracesUiParas.gain
            npts, ntraces = section.shape  # time/traces
            if ntraces < 1:
                raise IndexError("Nothing to plot")
            if npts < 1:
                raise IndexError("Nothing to plot")
            # fft处理
            if tracesUiParas.bfft:
                t = np.linspace(0, 1 / self.fdt / 2, npts)
                pyplot.ylabel('Freq (Hz)')
            else:
                pyplot.ylabel('Time (s)')
                t = np.linspace(0, self.fdt * npts, npts)
            amp = 1.  # normalization factor
            gmin = 0.  # global minimum
            toffset = 0.  # offset in time to make 0 centered
            if normalize:
                gmax = section.max()
                gmin = section.min()
                amp = (gmax - gmin)
                toffset = 0.5
            pyplot.ylim(max(t), 0)
            if ranges is None:
                ranges = (0, ntraces)
            x0, x1 = ranges
            # horizontal increment
            dx = (x1 - x0)/ntraces
            pyplot.xlim(x0, x1)
            pyplot.xticks(np.arange(_x_ticks_len), _x_ticks.astype(int))
            pyplot.locator_params(axis='x', nbins=tracesUiParas.nX)   # x轴标签显示数量
            pyplot.locator_params(axis='y', nbins=tracesUiParas.nY)  # y轴标签显示数量
            for i, trace in enumerate(section.transpose()):
                tr = (((trace - gmin)/amp) - toffset) * self.fscale * dx
                x = x0 + i*dx  # x positon for this trace
                self.pltList.append(pyplot.plot(x + tr, t, color=tracesUiParas.color))
                if not tracesUiParas.bfft:
                    pyplot.fill_betweenx(t, x + tr, x, tr > 0, color=tracesUiParas.color)

    def plotCRG(self, CRGUiParas, ranges=None, normalize=False):
        """
        绘制CRG wiggle图

        Args:
            CRGUiParas(CRGTraceUiParas): CRG测线参数
            ranges: 暂不使用，与traceRange冲突. (min and max horizontal values (default trace number))
            normalize: True to normalizes all trace in the section using global max/min
                data will be in the range (-0.5, 0.5) zero centered

        """
        CRG_List = []
        CRG_x_List = []
        # 查找 receiver == receiver_depth 的trace
        for i in range(0, self.fsegyfile.header.length):
            depth_scalar = self.fsegyfile.header[i][69]
            traceReceiverDepth = self.fsegyfile.header[i][41]
            traceSourceDepth = self.fsegyfile.header[i][45]
            if depth_scalar > 0:
                traceReceiverDepth = traceReceiverDepth * depth_scalar
                traceSourceDepth = traceSourceDepth * depth_scalar
            else:
                traceReceiverDepth = traceReceiverDepth / abs(depth_scalar)
                traceSourceDepth = traceSourceDepth / abs(depth_scalar)
            if traceReceiverDepth == CRGUiParas.depth:
                CRG_List.append(i)
                CRG_x_List.append(traceSourceDepth)

        a = np.zeros((len(CRG_List), len(self.fsegyfile.samples)))
        traceTemp = self.fsegyfile.trace.raw[:]
        for i in range(0, len(CRG_List)):
            a[i] = traceTemp[CRG_List[i]]
        # 筛选showNum
        if CRGUiParas.showNum < 0:
            raise IndexError("showNum Error, Nothing to plot")
        elif CRGUiParas.showNum == 0:
            section = a
            _x_ticks_len = len(CRG_List)
            _x_ticks = np.asarray(CRG_x_List)
        else:
            _x_ticks_len = CRGUiParas.showNum
            _x_ticks = np.zeros(CRGUiParas.showNum)
            section = np.zeros((CRGUiParas.showNum, len(self.fsegyfile.samples)))
            section_tmp = a
            interval = int(len(CRG_List) / CRGUiParas.showNum)
            for i in range(0, CRGUiParas.showNum):
                section[i] = section_tmp[i * interval]
                _x_ticks[i] = CRG_x_List[i * interval]
        # 绘制
        # filter处理
        section = self._filter(CRGUiParas, section)
        # fft处理
        if CRGUiParas.bfft:
            section = self._fftPlot(CRGUiParas, section)
        section = section.T
        if CRGUiParas.bColorImage:
            self.seismic_image(section, fft=CRGUiParas.bfft)
            pyplot.xticks(np.arange(_x_ticks_len), _x_ticks.astype(int))
            pyplot.locator_params(axis='x', nbins=CRGUiParas.nX)  # x轴标签显示数量
            pyplot.locator_params(axis='y', nbins=CRGUiParas.nY)  # y轴标签显示数量
            pyplot.xlabel('Source Depth')
            pyplot.title("CRG plot, Receiver Depth=" + str(CRGUiParas.depth) + "ft")
        else:
            self.fscale = CRGUiParas.gain
            npts, ntraces = section.shape  # time/traces
            if ntraces < 1:
                print("Nothing to plot")
                #raise IndexError("Nothing to plot")
                return
            if npts < 1:
                print("Nothing to plot")
                #raise IndexError("Nothing to plot")
                return
            # fft处理
            if CRGUiParas.bfft:
                t = np.linspace(0, 1 / self.fdt / 2, npts)
                pyplot.ylabel('Freq (Hz)')
            else:
                pyplot.ylabel('Time (s)')
                t = np.linspace(0, self.fdt * npts, npts)
            amp = 1.  # normalization factor
            gmin = 0.  # global minimum
            toffset = 0.  # offset in time to make 0 centered
            if normalize:
                gmax = section.max()
                gmin = section.min()
                amp = (gmax - gmin)
                toffset = 0.5
            pyplot.ylim(max(t), 0)
            if ranges is None:
                ranges = (0, ntraces)
            x0, x1 = ranges
            # horizontal increment
            dx = (x1 - x0) / ntraces
            pyplot.xlim(x0, x1)
            pyplot.xticks(np.arange(_x_ticks_len), _x_ticks.astype(int))
            pyplot.locator_params(axis='x', nbins=CRGUiParas.nX)  # x轴标签显示数量
            pyplot.locator_params(axis='y', nbins=CRGUiParas.nY)  # y轴标签显示数量
            pyplot.title("CRG plot, Receiver Depth=" + str(CRGUiParas.depth) + "ft")
            for i, trace in enumerate(section.transpose()):
                tr = (((trace - gmin) / amp) - toffset) * self.fscale * dx
                x = x0 + i * dx  # x positon for this trace
                pyplot.plot(x + tr, t, color=CRGUiParas.color)
                if not CRGUiParas.bfft:
                    pyplot.fill_betweenx(t, x + tr, x, tr > 0, color=CRGUiParas.color)

    def plotCSG(self, CSGUiParas, ranges=None, normalize=False):
        """
        绘制CSG wiggle图

        Args:
            CSGUiParas(CSGTraceUiParas): CRG测线参数
            ranges: 暂不使用，与traceRange冲突. (min and max horizontal values (default trace number))
            normalize: True to normalizes all trace in the section using global max/min
                data will be in the range (-0.5, 0.5) zero centered

        """
        CSG_List = []
        CSG_x_List = []
        # 查找 source == source_depth 的trace
        for i in range(0, self.fsegyfile.header.length):
            depth_scalar = self.fsegyfile.header[i][69]
            traceReceiverDepth = self.fsegyfile.header[i][41]
            traceSourceDepth = self.fsegyfile.header[i][45]
            if depth_scalar > 0:
                traceReceiverDepth = traceReceiverDepth * depth_scalar
                traceSourceDepth = traceSourceDepth * depth_scalar
            else:
                traceReceiverDepth = traceReceiverDepth / abs(depth_scalar)
                traceSourceDepth = traceSourceDepth / abs(depth_scalar)
            if traceSourceDepth == CSGUiParas.depth:
                CSG_List.append(i)
                CSG_x_List.append(traceReceiverDepth)

        a = np.zeros((len(CSG_List), len(self.fsegyfile.samples)))
        traceTemp = self.fsegyfile.trace.raw[:]
        for i in range(0, len(CSG_List)):
            a[i] = traceTemp[CSG_List[i]]
        # 筛选showNum
        if CSGUiParas.showNum < 0:
            raise IndexError("showNum Error, Nothing to plot")
        elif CSGUiParas.showNum == 0:
            section = a
            _x_ticks_len = len(CSG_List)
            _x_ticks = np.asarray(CSG_x_List)
        else:
            _x_ticks_len = CSGUiParas.showNum
            _x_ticks = np.zeros(CSGUiParas.showNum)
            section = np.zeros((CSGUiParas.showNum, len(self.fsegyfile.samples)))
            section_tmp = a
            interval = int(len(CSG_List) / CSGUiParas.showNum)
            for i in range(0, CSGUiParas.showNum):
                section[i] = section_tmp[i * interval]
                _x_ticks[i] = CSG_x_List[i * interval]
        # 绘制
        # filter处理
        section = self._filter(CSGUiParas, section)
        # fft处理
        if CSGUiParas.bfft:
            section = self._fftPlot(CSGUiParas, section)
        # 图注处理
        pyplot.title("CSG plot, Source Depth=" + str(CSGUiParas.depth) + "ft")
        pyplot.xlabel('Receiver Depth')
        if CSGUiParas.bfft:
            pyplot.ylabel('Freq (Hz)')
        else:
            pyplot.ylabel('Time (s)')
        section = section.T
        if CSGUiParas.bColorImage:
            self.seismic_image(section, fft=CSGUiParas.bfft)
            pyplot.xticks(np.arange(_x_ticks_len), _x_ticks.astype(int))
            pyplot.locator_params(axis='x', nbins=CSGUiParas.nX)  # x轴标签显示数量
            pyplot.locator_params(axis='y', nbins=CSGUiParas.nY)  # y轴标签显示数量
        else:
            self.fscale = CSGUiParas.gain
            npts, ntraces = section.shape  # time/traces
            if ntraces < 1:
                print("Nothing to plot")
                # raise IndexError("Nothing to plot")
                return
            if npts < 1:
                print("Nothing to plot")
                # raise IndexError("Nothing to plot")
                return
            # fft处理
            if CSGUiParas.bfft:
                t = np.linspace(0, 1 / self.fdt / 2, npts)
            else:
                t = np.linspace(0, self.fdt * npts, npts)
            amp = 1.  # normalization factor
            gmin = 0.  # global minimum
            toffset = 0.  # offset in time to make 0 centered
            if normalize:
                gmax = section.max()
                gmin = section.min()
                amp = (gmax - gmin)
                toffset = 0.5
            pyplot.ylim(max(t), 0)
            if ranges is None:
                ranges = (0, ntraces)
            x0, x1 = ranges
            # horizontal increment
            dx = (x1 - x0) / ntraces
            pyplot.xlim(x0, x1)
            pyplot.xticks(np.arange(_x_ticks_len), _x_ticks.astype(int))
            pyplot.locator_params(axis='x', nbins=CSGUiParas.nX)  # x轴标签显示数量
            pyplot.locator_params(axis='y', nbins=CSGUiParas.nY)  # y轴标签显示数量
            for i, trace in enumerate(section.transpose()):
                tr = (((trace - gmin) / amp) - toffset) * self.fscale * dx
                x = x0 + i * dx  # x positon for this trace
                pyplot.plot(x + tr, t, color=CSGUiParas.color)
                if not CSGUiParas.bfft:
                    pyplot.fill_betweenx(t, x + tr, x, tr > 0, color=CSGUiParas.color)

    def _fftPlot(self, tracesUiParas, section):
        """
        对section剖面执行`FFT变换`，得到频域图

        """
        N = len(self.fsegyfile.samples)
        fft_len = section.shape[0]
        fftSection = np.zeros((fft_len, N // 2))
        # 获取freq刻度
        # fft_y_ticks = np.fft.rfftfreq(len(self.fsegyfile.samples) // 2, self.fdt)
        for i in range(0, fft_len):
            fftSection[i] = np.log10(np.abs(np.fft.fft(section[i])[:N // 2]))
        return fftSection

    def _filter(self, tracesUiParas, section):
        """
        对section剖面执行`滤波`处理

        """
        if tracesUiParas.bfilter:
            N, Wn = signal.buttord([tracesUiParas.bandPassFilterParas.F_pass1, tracesUiParas.bandPassFilterParas.F_pass2],
                                   [tracesUiParas.bandPassFilterParas.F_stop1, tracesUiParas.bandPassFilterParas.F_stop2],
                                   tracesUiParas.bandPassFilterParas.A_pass, tracesUiParas.bandPassFilterParas.A_stop,
                                   analog=False, fs=1/self.fdt)
            sos = signal.butter(N, Wn, 'bandpass', False, fs=1/self.fdt, output='sos')
            traceData = signal.sosfiltfilt(sos, section)  # data为要过滤的信号
            return traceData
        else:
            return section
