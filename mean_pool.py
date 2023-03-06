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


# gen = NodesGenerator(start=0, end=2 * 2 * np.pi, nodes=1000, start_sequence=[0, 1, 5], func=lambda x: np.sin(x) + np.sin(2 * x))
#
# ani = FuncAnimation(fig, update, frames=gen, init_func=init, blit=True, repeat=False)
# plt.show()
#
# xs = np.linspace(-5, 5, 1000)
# ys = np.rint(xs)
#
# for k in range(40):
#     print(-5 + k * 0.25, np.rint(-5 + k * 0.25))
#
# plt.plot(xs, ys)
# plt.show()


# curr_nodes = [0.0, 100.0]
# prev_nodes = []
#
# for _ in range(4):
#
#     next_nodes = []
#     for i, elem in enumerate(curr_nodes):
#         for jlem in curr_nodes[i + 1:]:
#             next_nodes.append((elem + jlem) / 2)
#
#         for jlem in prev_nodes:
#             next_nodes.append((elem + jlem) / 2)
#
#     prev_nodes.extend(curr_nodes)
#     curr_nodes = next_nodes
#
#     print(prev_nodes, curr_nodes, len(curr_nodes), len(set(curr_nodes)))


# curr_nodes = [0.0, 100.0]
# prev_nodes = []
#
# for _ in range(5):
#
#     next_nodes = []
#     for i in range(len(curr_nodes) - 1):
#         next_nodes.append((curr_nodes[i] + curr_nodes[i + 1]) / 2)
#
#     for j in range(len(prev_nodes)):
#         for i in range(len(curr_nodes)):
#             next_nodes.append((curr_nodes[i] + prev_nodes[j]) / 2)
#         # for jlem in prev_nodes:
#         #     next_nodes.append((elem + jlem) / 2)
#
#     prev_nodes.extend(curr_nodes)
#     curr_nodes = next_nodes
#
#     print(len(curr_nodes), len(set(curr_nodes)), prev_nodes, curr_nodes)


# true_y_arr = np.full(101, np.nan, dtype=np.double)
# true_y_arr[0] = 5.0
# true_y_arr[100] = -3.0
#
# for _ in range(10):
#
#     next_indexes = []
#     a, b = None, None
#
#     for k in range(true_y_arr.shape[0]):
#         if np.isnan(true_y_arr[k]):
#             continue
#
#         if a is None:
#             a = k
#         elif b is None:
#             b = k
#             next_indexes.append(np.rint((a + b) / 2).astype(int))
#             a = k
#             b = None
#
#     print(next_indexes)
#
#     for index in next_indexes:
#
#         true_y_arr[index] = np.random.rand()


a, b = 0.0, 2 ** 7

all_nodes = []

curr_nodes = [(a, b)]
next_nodes = []

c_lst = []

for _ in range(7):

    for node in curr_nodes:
        # if node[1] - node[0] < 2:
        #     continue
        c = sum(node) / 2

        # c = np.rint(c)
        c_lst.append(c)

        if c - node[0] > 1:
            next_nodes.append((node[0], c))

        if node[1] - c > 1:
            next_nodes.append((c, node[1]))
        # next_nodes.extend([(node[0], c), (c, node[1])])

    print(len(all_nodes), len(curr_nodes), len(next_nodes), curr_nodes, next_nodes)
    print(all_nodes, '\n')
    curr_nodes = list(next_nodes)
    all_nodes.extend(next_nodes)
    next_nodes = []

print(len(c_lst), len(set(c_lst)), c_lst, '\n', sorted(c_lst))