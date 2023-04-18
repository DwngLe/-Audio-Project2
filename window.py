import numpy as np

class Window:
    def hanning(N):
        n = np.arange(N)
        return 0.5 - 0.5 * np.cos(2 * np.pi * n / (N - 1))
      
    def hamming(N):
        n = np.arange(N)
        return 0.54 - 0.46 * np.cos(2 * np.pi * n / (N - 1))
    
    def rectangular(N):
        return np.ones(N)
    
    def blackman(N):
        n = np.arange(N)
        return 0.42 - 0.5 * np.cos(2 * np.pi * n / (N - 1)) + 0.08 * np.cos(4 * np.pi * n / (N - 1))
    
    def triangular(N):
        n = np.arange(N)
        return 1 - 2 * np.abs(n - (N - 1) / 2) / (N - 1)