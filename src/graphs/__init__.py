from .GraphManager import GraphManager
from .GraphManager3d import GraphManager3d


graph_manager = GraphManager()
graph_manager_3d = GraphManager3d()

__all__ = [
    'graph_manager',
    'graph_manager_3d'
]
