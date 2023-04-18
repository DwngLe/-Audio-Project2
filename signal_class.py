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
    
  
    