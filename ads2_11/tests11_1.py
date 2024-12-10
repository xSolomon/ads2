''' Tests for lesson 11 task 1 solution. '''

import unittest
from solution12_1 import Vertex, SimpleGraph

class DFSTests(unittest.TestCase):
    ''' Tests for DeepFirstSearch function. '''
    def form_graph(self, size : int, verteces_values : list[int],
        edges : list[tuple]) -> SimpleGraph:
        ''' Prepares graph for tests. '''
        self.assertEqual(len(verteces_values), size)
        graph : SimpleGraph = SimpleGraph(size)
        for vertex_index, vertex_value in enumerate(verteces_values):
            graph.vertex[vertex_index] = None if not vertex_value else Vertex(vertex_value)
        for edge in edges:
            graph.AddEdge(edge[0], edge[1])
        return graph

unittest.main()
