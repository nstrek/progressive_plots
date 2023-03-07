import numpy as np


# TODO: nodes_to_update - параметр задающий частоту обновления графика


class NodesGenerator:
    def __init__(self, start, end, degree:int, func):
        self.start = start
        self.end = end
        self.degree = degree
        self.length = 2 ** degree
        self.func = func

        self.prev_nodes = None
        self.curr_nodes = None

        self.array_x = np.linspace(start, end, self.length)
        self.array_y = np.full_like(self.array_x, np.nan, dtype=np.double)
        self.mask = np.full_like(self.array_x, False, dtype=bool)

    def __len__(self):
        return self.length

    def __iter__(self):
        self.array_y[0] = self.func(self.array_x[0])
        self.mask[0] = True
        self.array_y[-1] = self.func(self.array_x[-1])
        self.mask[-1] = True

        self.prev_nodes = [(0, -1 + 2 ** self.degree)]
        self.curr_nodes = []
        self.n = 1
        self.next_index_generator = self.next_index()
        return self

    def __next__(self):
        if self.n == self.length:
            raise StopIteration

        index = next(self.next_index_generator)
        # print(self.n, index)
        index = int(index)

        self.n += 1

        x = self.array_x[index]
        self.array_y[index] = self.func(x)
        self.mask[index] = True

        # print(*self.array_y)
        # if self.n > 120:
        #     print(*self.array_y)
        #     print(*self.array_y[self.mask])
        return self.array_x[self.mask], self.array_y[self.mask]

    def next_index(self):

        for _ in range(self.degree):

            for node in self.prev_nodes:
                c = sum(node) / 2

                # c = np.rint(c)

                # if c - node[0] > 1:
                #     self.curr_nodes.append((node[0], c))
                #
                # if node[1] - c > 1:
                #     self.curr_nodes.append((c, node[1]))
                self.curr_nodes.extend([(node[0], c), (c, node[1])])

                yield c

            self.prev_nodes = list(self.curr_nodes)
            self.curr_nodes = []

# fig, ax = plt.subplots()
# xdata, ydata = [], []
# ln, = ax.plot([], [], 'ro')
#
#
# def init():
#     ax.set_xlim(0, 2 * 2 * np.pi)
#     ax.set_ylim(-3, 3)
#     return ln,
#
#
# def update(frame):
#     # xdata.append(frame[0])
#     # ydata.append(frame[1])
#     # ln.set_data(xdata, ydata)
#     # print(frame)
#     return ax.plot(frame[0], frame[1])

# gen = NodesGenerator(start=0, end=2 * 2 * np.pi, degree=7, func=lambda x: np.sin(x) + np.sin(2 * x))
#
# ani = FuncAnimation(fig, update, frames=gen, init_func=init, blit=True, repeat=False)
# plt.show()
