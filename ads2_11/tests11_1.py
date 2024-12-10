''' Tests for lesson 11 task 1 solution. '''

import unittest
from solution11_1 import Vertex, SimpleGraph

class DFSTests(unittest.TestCase):
    ''' Tests for DeepFirstSearch function. '''
    def form_graph(self, size : int) -> SimpleGraph:
        ''' Prepares graph for tests. '''
        return SimpleGraph(size)

    def create_edges(self, graph : SimpleGraph, edges : list[tuple]) -> SimpleGraph:
        ''' Creates edges in graph according to the list (from_vertex, to_vertex). '''
        for vertex_pair in edges:
            for from_vertex, to_vertex in vertex_pair:
                graph.AddEdge(from_vertex, to_vertex)
        return graph

    def create_verteces(self, graph : SimpleGraph, verteces : list[int]) -> SimpleGraph:
        ''' Creates verteces in graph according to the values list. '''

unittest.main()
