import librosa
import numpy as np
import matplotlib.pyplot as plt
from signal_class import Signal

class Show: 
    def show_do_thi( x, y):
        plt.figure(figsize=(10, 8))
        plt.subplot(1, 2, 1)
        plt.plot(x)
        plt.title('Đoạn âm thanh 1')
        plt.xlabel('Thời gian')
        plt.ylabel('Amplitude')

        plt.subplot(1, 2, 2)
        plt.plot(y)
        plt.title('Đoạn âm thanh 2')
        plt.xlabel('Thời gian')
        plt.ylabel('Amplitude')

        plt.tight_layout()
        plt.show()
  

    def show_pho( x, y):
        D1 = librosa.stft(x)
        mag1, phase1 = librosa.magphase(D1)

        D2 = librosa.stft(y)
        mag2, phase2 = librosa.magphase(D2)

        plt.figure(figsize=(10, 8))
        plt.subplot(1, 2, 1)
        librosa.display.specshow(librosa.amplitude_to_db(mag1, ref=np.max), y_axis='log', x_axis='time')
        # plt.colorbar(format='%+2.0f dB')
        plt.title('Phổ của âm thanh 1')
        plt.xlabel('Thời gian (giây)')
        plt.ylabel('Tần số (Hz)')

        plt.subplot(1, 2, 2)
        librosa.display.specshow(librosa.amplitude_to_db(mag2, ref=np.max), y_axis='log', x_axis='time')
        # plt.colorbar(format='%+2.0f dB')
        plt.title('Phổ của âm thanh 2')
        plt.xlabel('Thời gian (giây)')
        plt.ylabel('Tần số (Hz)')

        plt.tight_layout()
        plt.show()