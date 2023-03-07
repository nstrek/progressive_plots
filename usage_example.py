# progressive_plot = ProgressivePlot()
#
# # Надо задать функцию и сетку узлов
#
# def f(x):
#     return x  # some function
#
#
# M = EquidistantNodesSet1d(start, end, step)
#
# progressive_plot.start(f, M)

from main import NodesGenerator
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

mpl.use('TkAgg')

# nodes_to_update - параметр задающий частоту обновления графика

fig, ax = plt.subplots()
ln, = ax.plot([], [], 'ro')


def init():
    ax.set_xlim(0, 2 * 2 * np.pi)
    ax.set_ylim(-3, 3)
    return ln,


def update(frame):
    return ax.plot(frame[0], frame[1], color='blue')


gen = NodesGenerator(start=0, end=2 * 2 * np.pi, degree=7, func=lambda x: np.sin(x) + np.sin(2 * x))

ani = FuncAnimation(fig, update, frames=gen, init_func=init, blit=True, repeat=False)
plt.show()
