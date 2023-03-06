import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

mpl.use('TkAgg')

# nodes_to_update - параметр задающий частоту обновления графика

np.random.seed(0)

fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = ax.plot([], [], 'ro')


def init():
    ax.set_xlim(0, 2 * 2 * np.pi)
    ax.set_ylim(-3, 3)
    return ln,


def update(frame):
    xdata.append(frame[0])
    ydata.append(frame[1])
    # ln.set_data(xdata, ydata)
    return ax.plot(xdata, ydata)


class NodesGenerator:
    def __init__(self, start, end, nodes, start_sequence, func):
        self.start = start
        self.end = end
        self.nodes = nodes
        self.sequence = start_sequence
        self.func = func


        self.array_x = start + np.arange(nodes) * (end - start) / (nodes - 1)
        self.array_true_y = np.full_like(self.array_x, np.nan, dtype=np.double)
        self.array_interpolated_y = np.full_like(self.array_x, np.nan, dtype=np.double)
        # np.

    def __len__(self):
        return self.nodes

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.nodes:

            next_point = self.find_next_point()

            self.sequence.append(next_point)
            print(next_point)

            self.n += 1
            return next_point, self.func(next_point)
        else:
            raise StopIteration


    def find_next_point(self):
        if np.random.rand() > 0.1:
            return self.n / 10
        else:
            return np.nan


gen = NodesGenerator(start=0, end=2 * 2 * np.pi, nodes=1000, start_sequence=[0, 1, 5], func=lambda x: np.sin(x) + np.sin(2 * x))

ani = FuncAnimation(fig, update, frames=gen, init_func=init, blit=True, repeat=False)
plt.show()

xs = np.linspace(-5, 5, 1000)
ys = np.rint(xs)

for k in range(40):
    print(-5 + k * 0.25, np.rint(-5 + k * 0.25))

plt.plot(xs, ys)
plt.show()