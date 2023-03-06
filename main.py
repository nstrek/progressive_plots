import numpy as np
import matplotlib.pyplot as plt
# import matplotlib.cm as cm
# import pandas as pd
import time
import matplotlib.animation as animation
import matplotlib as mpl

mpl.use('TkAgg')

NUMBER_X: int = 2
NUMBER_Y: int = 1

CANVAS_WIDTH:  int = 10
CANVAS_HEIGHT: int = 10

def heatmap_animation1():
    fig, ax_lst = plt.subplots(NUMBER_X, NUMBER_Y)
    ax_lst = ax_lst.ravel()

    def plot(data):
        data = np.random.rand(CANVAS_WIDTH, CANVAS_HEIGHT)
        heatmap = ax_lst[0].pcolor(data)

    ani = animation.FuncAnimation(fig, plot, interval=1)
    plt.show()

def heatmap_animation2():
    fig, ax_lst = plt.subplots(NUMBER_X, NUMBER_Y)
    ax_lst = ax_lst.ravel()

    data = np.random.rand(CANVAS_WIDTH, CANVAS_HEIGHT)
    im = ax_lst[0].imshow(data)

    while True:
        t_start = time.time()
        data = np.random.rand(CANVAS_WIDTH, CANVAS_HEIGHT)
        im.set_data(data)
        plt.pause(0.001)
        t_end = time.time()
        print("fps = {0}".format(999 if t_end == t_start else 1/(t_end-t_start)))

def heatmap_animation3():
    fig, ax_lst = plt.subplots(NUMBER_X, NUMBER_Y)
    ax_lst = ax_lst.ravel()

    data = np.random.rand(CANVAS_WIDTH, CANVAS_HEIGHT)
    heatmap = ax_lst[0].pcolor(data)
    fig.canvas.draw()
    fig.show()

    while True:
        data = np.random.rand(CANVAS_WIDTH, CANVAS_HEIGHT)
        t_start = time.time()
        heatmap = ax_lst[0].pcolor(data)
        ax_lst[0].draw_artist(ax_lst[0].patch)
        ax_lst[0].draw_artist(heatmap)
        fig.canvas.blit(ax_lst[0].bbox)
        fig.canvas.flush_events()
        t_end = time.time()
        print("fps = {0}".format(999 if t_end == t_start else 1/(t_end-t_start)))


def main():
    """
    Entry function
    :called when: the program starts
    :param none: no parameter
    :return: none
    :rtype: none
    """
    heatmap_animation3()



if __name__ == '__main__':
    main()


class CalculationProcess: # или AnimationProcess или ProgressiveHeatmap
    # Здесь вычислять значения в узлах для истинной таблицы,
    # выбирать следующие координаты
    # и модифицировать значения ускоренной таблицы
    def step(self):
        pass