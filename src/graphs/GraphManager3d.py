import string

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from .GraphManager import GraphManager


class GraphManager3d(GraphManager):
    words_available_sizes = 3

    def draw_graph(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        words = super().get_words(word_length=self.words_available_sizes)

        nodes = {
            (
                string.ascii_lowercase.index(j[0]),
                string.ascii_lowercase.index(j[1]),
                string.ascii_lowercase.index(j[2])
            ): j for j in words
        }
        X, Y, Z = zip(*[(i[0], i[1], i[2]) for i in nodes.keys()])

        ax.scatter(X, Y, Z, c='r', marker='o')

        ages = []
        for n1 in nodes:
            for n2 in nodes:
                if (
                        (nodes[n1][0] == nodes[n2][0] or
                         nodes[n1][1] == nodes[n2][1] or
                         nodes[n1][2] == nodes[n2][2]) and
                        (n1, n2) not in ages and n1 != n2
                ):
                    ages.append((n1, n2))

        for line in ages:
            x, y, z = zip(*((dot[0], dot[1], dot[2]) for dot in line))
            ax.plot(x, y, z, color='r')

        for i, txt in enumerate(words):
            ax.text(X[i], Y[i], Z[i], txt, size=10)

        plt.show()
