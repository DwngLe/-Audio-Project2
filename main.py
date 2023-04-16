import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
from filter import Filter
from window import Window
from signal_class import Signal

x, fs = librosa.load('au_01.wav')
sound = Signal(x, fs)

boloc = Filter()

# Tạo tần số cắt và độ dài của cửa sổ
fc = 2000
fs = sound.sample_rate
signal = sound.samples
N = 69
h = boloc.lpf(fc, signal, N)
new_signal = np.convolve(fs, h)
new_sound = Signal(new_signal, fs)

plt.figure(figsize=(10, 8))
plt.subplot(2, 2, 1)
sound.show("Doan am thanh goc")
plt.subplot(2, 2, 2)
new_sound.show("Doan am thanh sau khi bien doi")
plt.tight_layout()
plt.show()