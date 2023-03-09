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

from src.ProgressivePlots.main import NodesGenerator
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

mpl.use('TkAgg')

# nodes_to_update - параметр задающий частоту обновления графика

start = 0.0
end = 8 * np.pi
degree = 8

params = np.random.rand(6)


def f(x):
    v = np.array([np.sin(x), np.cos(x),
                  np.sin(2 * x), np.cos(2 * x),
                  np.sin(3 * x), np.cos(3 * x)])

    return np.dot(params, v)


fig, axes = plt.subplots(ncols=2)
title = plt.suptitle(t='', fontsize=20)
ln, = axes[0].plot([], [])
#####
xs = np.linspace(start, end, 2 ** degree)
ys = [f(xs[k]) for k in range(2 ** degree)]
true_curve, = axes[1].plot(xs, ys, color='green')
height = max(abs(min(ys)), max(ys)) * 1.05


#####


def init():
    axes[0].set_xlim(start, end)
    axes[0].set_ylim(-height, height)

    axes[1].set_xlim(start, end)
    axes[1].set_ylim(-height, height)
    return ln,


def update(frame):
    # print(frame[0])
    # axes[0].set_title(f'{frame[0]}')
    # fig.suptitle(f'{frame[0]}')

    title.set_text(f'{frame["number"]}')
    axes[0].clear()
    axes[0].set_xlim(start, end)
    axes[0].set_ylim(-height, height)
    axes[0].scatter(frame['array_x'][frame['index']], 0, color='red')
    a, = axes[0].plot(frame['array_x'][frame['mask']], frame['array_y'][frame['mask']], color='blue')
    return a, true_curve


gen = NodesGenerator(start=start, end=end, degree=degree, func=f)

ani = FuncAnimation(fig, update, frames=gen, init_func=init, blit=True, repeat=False)
# plt.show()

from matplotlib import animation

# f = r"D:\PycharmProjects\ProgressivePlots\for_article\anim.html"
# writergif = animation.HTMLWriter(fps=30)
# ani.save(f, writer=writergif)
f = r"D:\PycharmProjects\ProgressivePlots\for_article\animation.gif"
ani.save(f, writer='Pillow', fps=30)
