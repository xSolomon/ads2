''' Tests for lesson 10 solution. '''

import unittest
from typing import Tuple
from solution10_1 import Vertex, SimpleGraph

class DFSTests(unittest.TestCase):
    ''' Tests for DeepFirstSearch function. '''
    def setUp(self) -> None:
        ''' Test preparations. '''
        self.graph : SimpleGraph = SimpleGraph(5)

    def tearDown(self) -> None:
        ''' Aftertest cleanup. '''
        self.graph = None

    def test_is_connected_one_graph_with_one_vertex(self) -> None:
        ''' Graph with one vertex is always connected. '''
        self.graph.AddVertex(100)
        self.assertTrue(self.graph.is_connected())

    def test_is_connected_on_two_vertex_graph_without_edges(self) -> None:
        ''' Graph without edges is always disconnected. '''
        self.graph.AddVertex(100)
        self.graph.AddVertex(200)
        self.assertFalse(self.graph.is_connected())

    def test_is_connected_on_predefined_five_vertex_graphs(self) -> None:
        ''' Graphs are: list-like, star-like (all edges lead to central vertex),
            with one vertex disconnected. '''
        graphs_edges : list[list[Tuple[int, int]]] = [
            [(0, 1), (1, 2), (2, 3), (3, 4)],
            [(0, 1), (0, 2), (0, 3), (0, 4)],
            [(0, 1), (1, 3), (3, 2), (0, 3), (1, 3)]
        ]
        graph_connected : list[bool] = [
            True,
            True,
            False
        ]
        for i in range(5):
            self.graph.AddVertex(i)
        for i, edges in enumerate(graphs_edges):
            for edge in edges:
                self.graph.AddEdge(edge[0], edge[1])
            with self.subTest(i = i):
                self.assertEqual(self.graph.is_connected(), graph_connected[i])
            for edge in edges:
                self.graph.RemoveEdge(edge[0], edge[1])

unittest.main()
