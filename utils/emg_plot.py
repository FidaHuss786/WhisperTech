import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import deque

class LivePlot:
    def __init__(self, max_samples=100):
        matplotlib.use('agg')
        self.max_samples = max_samples
        self.data = deque([0]*max_samples, maxlen=max_samples)
        self.fig, self.ax = plt.subplots()
        self.line, = self.ax.plot(range(max_samples), self.data)
        self.ax.set_ylim(0, 1024)

    def update_plot(self, new_value):
        self.data.append(new_value)

    def animate(self, i):
        self.line.set_ydata(self.data)
        return self.line,

    def show(self):
        ani = animation.FuncAnimation(self.fig, self.animate, interval=50)
        plt.show()
