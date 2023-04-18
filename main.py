import librosa
from menu import Menu

x, fs = librosa.load('input/au_01.wav')
Menu.Menu1(x, fs)





