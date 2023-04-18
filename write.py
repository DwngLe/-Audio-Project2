import librosa
from signal_class import Signal

class Write:
    def ghi_am_thanh(y, fs):
        output_path = 'output/output.wav'
        librosa.output.write_wav(output_path, y, fs)
