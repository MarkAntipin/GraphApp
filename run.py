import argparse

from src import database
from src.graphs import graph_manager, graph_manager_3d

parser = argparse.ArgumentParser(description='GraphApp')
parser.add_argument(
    '--graph', type=str, default=None, help='2d or 3d graph (options `2d`, `3d`)'
)
parser.add_argument(
    '--add', type=str, default=None, help='word to add in db'
)
parser.add_argument(
    '--get', type=str, default=None, help='type `--get all`'
)

if __name__ == '__main__':
    # args = parser.parse_args()
    # if args.graph == '2d':
    #     graph_manager.draw_graph()
    # elif args.graph == '3d':
    #     graph_manager_3d.draw_graph()
    # else:
    #     print('no such command type help')
    # if args.add:
    #     try:
    #         database.add_word(args.add)
    #     except Exception as e:
    #         print(e)
    # if args.get == 'all':
    #     database.get_words()
    graph_manager_3d.draw_graph()
