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
        index = int(index)

        self.n += 1

        x = self.array_x[index]
        self.array_y[index] = self.func(x)
        self.mask[index] = True
        return {'number': self.n, 'index': index, 'mask': self.mask,
                'array_x': self.array_x, 'array_y': self.array_y}

    def next_index(self):

        for _ in range(self.degree):

            for node in self.prev_nodes:
                c = sum(node) / 2
                self.curr_nodes.extend([(node[0], c), (c, node[1])])

                yield c

            self.prev_nodes = list(self.curr_nodes)
            self.curr_nodes = []

