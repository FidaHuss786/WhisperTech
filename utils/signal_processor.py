# utils/signal_processor.py
import numpy as np

class SignalProcessor:
    def __init__(self, window_size, threshold):
        """Initialize the signal processor with smoothing and thresholding parameters."""
        self.window_size = window_size
        self.threshold = threshold

    def moving_average(self, signal):
        """Apply a moving average filter to smooth the signal."""
        if len(signal) < self.window_size:
            return signal
        return np.convolve(signal, np.ones(self.window_size)/self.window_size, mode='valid')

    def threshold_signal(self, signal):
        """Filter out values below the threshold."""
        return [val for val in signal if val >= self.threshold]

    def process_signal(self, signal):
        """Apply smoothing and thresholding to the signal."""
        smoothed = self.moving_average(signal)
        thresholded = self.threshold_signal(smoothed)
        return thresholded