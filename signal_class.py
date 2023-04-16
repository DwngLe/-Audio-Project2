import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt

class Signal:
    def __init__(self, samples, sample_rate):
        self.samples = samples
        self.start_pos= 0
        self.sample_rate = sample_rate
        self.length = len(self.samples)
    
    def show(self, title):
        duration = len(self.samples) /self.sample_rate
        time = np.linspace(0, duration, num=len(self.samples))
        plt.plot(time, self.samples)
        plt.title(title)
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
    