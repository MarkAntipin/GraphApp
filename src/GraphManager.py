import string
import random
from itertools import product

import networkx as nx
import matplotlib.pyplot as plt


class GraphManager(object):

    def __init__(self):
        self.letters = [l for l in string.ascii_lowercase]
        self.word_size = 2
        self.G = nx.Graph()

    def __generate_words(self, words_number):
        comb = product(self.letters, repeat=self.word_size)
        words = [''.join(c) for c in comb]
        return [random.choice(words) for _ in range(words_number)]

    def __generate_nodes(self, nodes_num):
        greed = {l: i for i, l in enumerate(self.letters)}
        nodes = {}
        words = self.__generate_words(words_number=nodes_num)
        for w in words:
            nodes[w] = (greed[w[0]], greed[w[1]])
        return nodes

    def __add_nodes(self, nodes):
        for n in nodes:
            self.G.add_node(n, pos=nodes[n])

    def __add_ages(self, nodes):
        ages = []
        for n1 in nodes:
            for n2 in nodes:
                if (
                        (nodes[n1][0] == nodes[n2][0] or
                         nodes[n1][1] == nodes[n2][1]) and
                        (n1, n2) not in ages
                ):
                    ages.append((n1, n2))
        self.G.add_edges_from(ages)

    def draw_graph(self, nodes_num):
        nodes = self.__generate_nodes(nodes_num)
        self.__add_nodes(nodes=nodes)
        self.__add_ages(nodes=nodes)
        nx.draw(self.G, nodes, with_labels=True, font_weight='bold')
        plt.show()
