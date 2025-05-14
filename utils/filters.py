import numpy as np

def moving_average(signal, window_size=5):
    """Apply a moving average filter to smooth the signal."""
    if len(signal) < window_size:
        return signal
    return np.convolve(signal, np.ones(window_size) / window_size, mode='valid').tolist()

def threshold_signal(signal, threshold=100):
    """Filter out values below the threshold to remove noise."""
    return [val for val in signal if val >= threshold]