import sys

from src.GraphManager import GraphManager
graph_manager = GraphManager()

if __name__ == '__main__':
    nodes_num = int(sys.argv[1])
    graph_manager.draw_graph(nodes_num=nodes_num)
