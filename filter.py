import numpy as np
from window import Window

class Filter:
    # def __init__(self):
    def lpf(self,fc, signal, N):
        cuaso = Window()
        # fc_normalized = fc / (fs / 2)
        # n = np.arange(self.N)
        h = np.sinc(2 * fc * np.arange(N) - (N - 1) / 2)
        window = cuaso.blackman(N)
        h = h * window
        h = h / np.sum(h)
        filtered_audio = np.convolve(signal, h, mode='same')
        return filtered_audio
      

    def hpf(self, fc, fs, N):
        fc_normalized = fc / (fs / 2)
        h = -np.sinc(2 * fc_normalized * np.arange(N) - (N - 1) / 2)
        h[(N - 1) // 2] += 1
        window = np.blackman(N)
        h = h * window
        h = h / np.sum(h)
        return h