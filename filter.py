import numpy as np
from window import Window

class Filter:
    # def __init__(self):
    def lpf(fc, fs, N, window_func):
        fc_norm = fc/fs
        wc = fc_norm*2*np.pi
        n = np.arange(N)

        h = (wc/np.pi) * np.sinc(wc*(n-(N-1)/2))
        hd = h * window_func
        return hd

    def bpf(fc1, fc2, fs, N, window_func):
        fc_norm1 = fc1/fs
        fc_norm2 = fc2/fs
        wc1 = fc_norm1*2*np.pi
        wc2 = fc_norm2*2*np.pi
        n = np.arange(N)
        h = (wc2/np.pi) * (np.sinc(wc2*(n - (N-1)/2))) - (wc1/np.pi) * (np.sinc(wc1*(n - (N-1)/2)))
        hd = h * window_func
        return hd

    def bsf(fc1, fc2, fs, N, window_func):
        fc_norm1 = fc1/fs
        fc_norm2 = fc2/fs
        wc1 = fc_norm1*2*np.pi
        wc2 = fc_norm2*2*np.pi
        n = np.arange(N)
        delta = np.zeros(N)
        delta[(N-1)//2] = 1

        h = (wc1/np.pi) * (np.sinc(wc1*(n - (N-1)/2))) - (wc2/np.pi) * (np.sinc(wc2*(n - (N-1)/2))) + delta
        hd = h * window_func
        return hd
    
    def hpf(fc, fs, N, window_func):
        fc_norm = fc/fs
        wc = fc_norm*2*np.pi
        n = np.arange(N)
        delta = np.zeros(N)
        delta[(N-1)//2] = 1

        h = -(wc/np.pi) * np.sinc(wc*(n-(N-1)/2)) + delta
        hd = h * window_func
        return hd