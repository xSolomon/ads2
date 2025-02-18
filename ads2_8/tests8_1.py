''' Tests for lesson 8 task 1 solution. '''

import unittest
from typing import Tuple
from solution8_1 import SimpleGraph

class SimpleGraphTests(unittest.TestCase):
    ''' Tests for is_edge, remove_edge, add_edge, add_vertex, remove_vertex functions. '''
    def setUp(self) -> None:
        ''' Test preparations. '''
        self.graph : SimpleGraph = SimpleGraph(5)

    def tearDown(self) -> None:
        ''' Aftertest cleanup. '''
        self.graph = None

    def test_is_edge_on_empty_graph(self) -> None:
        ''' Empty graph has no edges. '''
        for from_vertex_index in range(self.graph.get_max_vertex()):
            for to_vertex_index in range(self.graph.get_max_vertex()):
                self.assertFalse(self.graph.IsEdge(from_vertex_index, to_vertex_index))

    def test_remove_edge_on_empty_graph(self) -> None:
        ''' Deleting edge in empty graph always fail. '''
        for from_vertex_index in range(self.graph.get_max_vertex()):
            for to_vertex_index in range(self.graph.get_max_vertex()):
                self.assertFalse(self.graph.RemoveEdge(from_vertex_index, to_vertex_index))

    def test_remove_vertex_on_empty_graph(self) -> None:
        ''' Deleting vertex in empty graph always fail. '''
        for vertex_index in range(self.graph.get_max_vertex()):
            self.assertFalse(self.graph.RemoveVertex(vertex_index))

    def test_add_edge_on_empty_graph(self) -> None:
        ''' Adding edge to graph without verteces always fail. '''
        for from_vertex_index in range(self.graph.get_max_vertex()):
            for to_vertex_index in range(self.graph.get_max_vertex()):
                self.assertFalse(self.graph.AddEdge(from_vertex_index, to_vertex_index))

    def test_add_vertex_on_empty_graph(self) -> None:
        ''' Adding vertex to graph without verteces always succeeds. '''
        self.assertTrue(self.graph.AddVertex(100))

    def test_is_edge_on_one_vertex_graph(self) -> None:
        ''' Cause no edges added, should always fail. '''
        self.graph.AddVertex(100)
        for from_vertex_index in range(self.graph.get_max_vertex()):
            for to_vertex_index in range(self.graph.get_max_vertex()):
                self.assertFalse(self.graph.IsEdge(from_vertex_index, to_vertex_index))

    def test_add_edge_on_one_vertex_graph(self) -> None:
        ''' One vertex graph could have only one edge. '''
        self.graph.AddVertex(100)
        for from_vertex_index in range(self.graph.get_max_vertex()):
            for to_vertex_index in range(self.graph.get_max_vertex()):
                if from_vertex_index == 0 and from_vertex_index == to_vertex_index:
                    self.assertTrue(self.graph.AddEdge(from_vertex_index, to_vertex_index))
                    self.assertTrue(self.graph.IsEdge(from_vertex_index, to_vertex_index))
                    continue
                self.assertFalse(self.graph.AddEdge(from_vertex_index, to_vertex_index))

    def test_remove_edge_on_one_vertex_graph(self) -> None:
        ''' Removing edge in graph with one vertex always fail. '''
        self.graph.AddVertex(100)
        for from_vertex_index in range(self.graph.get_max_vertex()):
            for to_vertex_index in range(self.graph.get_max_vertex()):
                self.assertFalse(self.graph.RemoveEdge(from_vertex_index, to_vertex_index))

    def test_add_vertex_on_one_vertex_graph(self) -> None:
        ''' Adding second vertex succeeds for graphs with size 2 and more. '''
        self.graph.AddVertex(100)
        self.assertTrue(self.graph.AddVertex(50))
        full_graph : SimpleGraph = SimpleGraph(1)
        self.assertTrue(full_graph.AddVertex(100))
        self.assertFalse(full_graph.AddVertex(50))

    def test_remove_vertex_on_one_vertex_graph(self) -> None:
        ''' Removing vertex should succeed if correct index provided. '''
        self.graph.AddVertex(100)
        self.assertFalse(self.graph.RemoveVertex(1))
        self.assertTrue(self.graph.RemoveVertex(0))

    def test_filling_five_vertex_graph(self) -> None:
        ''' Adding new vertex must succeed until graph is full. '''
        for i in range(5):
            self.assertTrue(self.graph.AddVertex(i + 1))
        self.assertFalse(self.graph.AddVertex(6))

    def test_edge_manipulating_on_five_vertex_graph(self) -> None:
        ''' Add new edges between verteces, testing if they are created.
            Then remove them, testing they were deleted. '''
        for i in range(4):
            self.graph.AddVertex(i + 1)
            self.assertFalse(self.graph.AddEdge(i, 4))
        self.graph.AddVertex(5)
        edges : list[Tuple[int, int]] = [
            (0, 3),
            (0, 2),
            (2, 3),
            (3, 3),
            (3, 4),
            (4, 1),
            (1, 0),
        ]
        for edge in edges:
            with self.subTest(edge = edge):
                self.assertTrue(self.graph.AddEdge(edge[0], edge[1]))
                self.assertFalse(self.graph.AddEdge(edge[0], edge[1]))
                self.assertTrue(self.graph.IsEdge(edge[0], edge[1]))
        for edge in edges:
            with self.subTest():
                self.assertTrue(self.graph.RemoveEdge(edge[0], edge[1]))
                self.assertFalse(self.graph.RemoveEdge(edge[0], edge[1]))
                self.assertFalse(self.graph.IsEdge(edge[0], edge[1]))

unittest.main()
