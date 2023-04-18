import sounddevice as sd

class Play:
    def phat(x, fs):
        sd.play(x, fs)
        sd.wait()


