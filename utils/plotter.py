import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')  # ✅ Correct backend for GUI

from matplotlib.animation import FuncAnimation
from collections import deque

class RealTimePlotter:
    def __init__(self, serial_reader, window_size=100):
        """Initialize real-time EMG signal plotter."""
        self.serial_reader = serial_reader
        self.window_size = window_size
        self.data = deque([0] * window_size, maxlen=window_size)
        self.fig, self.ax = plt.subplots()
        self.line, = self.ax.plot(range(window_size), self.data)
        self.ax.set_ylim(0, 1024)  # Arduino ADC range (0-1023)
        self.ax.set_title("Live EMG Signal")
        self.ax.set_xlabel("Time (samples)")
        self.ax.set_ylabel("Amplitude")
        self.ax.grid(True)
        self.ani = None

    def update(self, frame):
        """Update plot with new data."""
        new_data = self.serial_reader.read_data()
        if new_data is not None:
            self.data.append(new_data)
            self.line.set_ydata(self.data)
        return self.line,

    def start_plot(self):
        """Start the real-time plot."""
        self.ani = FuncAnimation(self.fig, self.update, interval=50, blit=True, cache_frame_data=False)
        plt.show()
