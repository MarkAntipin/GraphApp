import networkx as nx
import matplotlib.pyplot as plt


from .Database import Database


class GraphManager(Database):
    def __init__(self):
        self.greed = {l: i for i, l in enumerate(self.available_letters)}
        self.G = nx.Graph()
        super(GraphManager, self)

    def __generate_nodes(self) -> dict:
        nodes = {}
        words = super().get_all_words()
        for w in words:
            nodes[w] = (self.greed[w[0]], self.greed[w[1]])
        return nodes

    def __add_nodes(self, nodes: dict):
        for n in nodes:
            self.G.add_node(n, pos=nodes[n])

    def __add_ages(self, nodes: dict):
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

    def draw_graph(self):
        nodes = self.__generate_nodes()
        self.__add_nodes(nodes=nodes)
        self.__add_ages(nodes=nodes)
        nx.draw(self.G, nodes, with_labels=True, font_weight='bold')
        plt.show()
