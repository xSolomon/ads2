''' Tests for lesson 8 task 2 solution. '''

import unittest
from typing import Tuple
from solution8_2 import DirectedGraph

class DirectedGraphTests(unittest.TestCase):
    ''' Tests for DirectedGraph functions. '''
    def setUp(self) -> None:
        ''' Test preparation. '''
        self.graph : DirectedGraph = DirectedGraph(5)

    def tearDown(self) -> None:
        ''' Aftertest cleanup. '''
        self.graph = None

    def test_is_edge_on_empty_graph(self) -> None:
        ''' Empty graph has no edges. '''
        for from_vertex_index in range(self.graph.get_max_vertex()):
            for to_vertex_index in range(self.graph.get_max_vertex()):
                self.assertFalse(self.graph.is_edge(from_vertex_index, to_vertex_index))

    def test_remove_edge_on_empty_graph(self) -> None:
        ''' Deleting edge in empty graph always fail. '''
        for from_vertex_index in range(self.graph.get_max_vertex()):
            for to_vertex_index in range(self.graph.get_max_vertex()):
                self.assertFalse(self.graph.remove_edge(from_vertex_index, to_vertex_index))

    def test_remove_vertex_on_empty_graph(self) -> None:
        ''' Deleting vertex in empty graph always fail. '''
        for vertex_index in range(self.graph.get_max_vertex()):
            self.assertFalse(self.graph.remove_vertex(vertex_index))

    def test_add_edge_on_empty_graph(self) -> None:
        ''' Adding edge to graph without verteces always fail. '''
        for from_vertex_index in range(self.graph.get_max_vertex()):
            for to_vertex_index in range(self.graph.get_max_vertex()):
                self.assertFalse(self.graph.add_edge(from_vertex_index, to_vertex_index))

    def test_add_vertex_on_empty_graph(self) -> None:
        ''' Adding vertex to graph without verteces always succeeds. '''
        self.assertTrue(self.graph.add_vertex(100))

    def test_is_edge_on_one_vertex_graph(self) -> None:
        ''' Cause no edges added, should always fail. '''
        self.graph.add_vertex(100)
        for from_vertex_index in range(self.graph.get_max_vertex()):
            for to_vertex_index in range(self.graph.get_max_vertex()):
                self.assertFalse(self.graph.is_edge(from_vertex_index, to_vertex_index))

    def test_add_edge_on_one_vertex_graph(self) -> None:
        ''' One vertex graph could have only one edge. '''
        self.graph.add_vertex(100)
        for from_vertex_index in range(self.graph.get_max_vertex()):
            for to_vertex_index in range(self.graph.get_max_vertex()):
                if from_vertex_index == 0 and from_vertex_index == to_vertex_index:
                    self.assertTrue(self.graph.add_edge(from_vertex_index, to_vertex_index))
                    self.assertTrue(self.graph.is_edge(from_vertex_index, to_vertex_index))
                    continue
                self.assertFalse(self.graph.add_edge(from_vertex_index, to_vertex_index))

    def test_remove_edge_on_one_vertex_graph(self) -> None:
        ''' Removing edge in graph with one vertex always fail. '''
        self.graph.add_vertex(100)
        for from_vertex_index in range(self.graph.get_max_vertex()):
            for to_vertex_index in range(self.graph.get_max_vertex()):
                self.assertFalse(self.graph.remove_edge(from_vertex_index, to_vertex_index))

    def test_add_vertex_on_one_vertex_graph(self) -> None:
        ''' Adding second vertex succeeds for graphs with size 2 and more. '''
        self.graph.add_vertex(100)
        self.assertTrue(self.graph.add_vertex(50))
        full_graph : DirectedGraph = DirectedGraph(1)
        self.assertTrue(full_graph.add_vertex(100))
        self.assertFalse(full_graph.add_vertex(50))

    def test_remove_vertex_on_one_vertex_graph(self) -> None:
        ''' Removing vertex should succeed if correct index provided. '''
        self.graph.add_vertex(100)
        self.assertFalse(self.graph.remove_vertex(1))
        self.assertTrue(self.graph.remove_vertex(0))

    def test_filling_five_vertex_graph(self) -> None:
        ''' Adding new vertex must succeed until graph is full. '''
        for i in range(5):
            self.assertTrue(self.graph.add_vertex(i + 1))
        self.assertFalse(self.graph.add_vertex(6))

    def test_edge_manipulating_on_five_vertex_graph(self) -> None:
        ''' Add new edges between verteces, testing if they are created.
            Then remove them, testing they were deleted. '''
        for i in range(4):
            self.graph.add_vertex(i + 1)
            self.assertFalse(self.graph.add_edge(i, 4))
        self.graph.add_vertex(5)
        edges : list[Tuple[int, int]] = [
            (0, 3),
            (0, 2),
            (2, 3),
            (3, 3),
            (3, 4),
            (4, 1),
            (1, 0),
            (1, 4),
            (2, 0)
        ]
        for edge in edges:
            with self.subTest():
                self.assertTrue(self.graph.add_edge(edge[0], edge[1]))
                self.assertFalse(self.graph.add_edge(edge[0], edge[1]))
                self.assertTrue(self.graph.is_edge(edge[0], edge[1]))
        for edge in edges:
            with self.subTest():
                self.assertTrue(self.graph.remove_edge(edge[0], edge[1]))
                self.assertFalse(self.graph.remove_edge(edge[0], edge[1]))
                self.assertFalse(self.graph.is_edge(edge[0], edge[1]))

    def test_is_cyclic_on_empty_graph(self) -> None:
        ''' Empty graph is always acyclic. '''
        self.graph.add_vertex(100)
        self.assertFalse(self.graph.is_cyclic())

    def test_is_cyclic_on_one_vertex_graph(self) -> None:
        ''' Graph with one vertex is always acyclic. '''
        self.graph.add_vertex(100)
        self.assertFalse(self.graph.is_cyclic())

    def test_is_cyclic_on_fife_vertex_graph(self) -> None:
        ''' Test on initially cyclic graph.
            Then, test after removing cycles one by one. '''
        for i in range(5):
            self.graph.add_vertex(i + 1)
        edges : list[Tuple[int, int]] = [
            (0, 3),
            (0, 2),
            (2, 3),
            (3, 3),
            (3, 4),
            (4, 1),
            (1, 0),
            (1, 4),
            (2, 0)
        ]
        edges_to_remove : list[Tuple[int, int]] = [
            (3, 3),
            (2, 0),
            (1, 4),
            (1, 0)
        ]
        expected_results : list[bool] = [
            True,
            True,
            True,
            True,
            False
        ]
        for edge in edges:
            self.graph.add_edge(edge[0], edge[1])
        for i, expected_result in enumerate(expected_results):
            with self.subTest(i = i, expected_result = expected_result):
                self.assertEqual(self.graph.is_cyclic(), expected_result)
            if i < len(edges_to_remove):
                self.graph.remove_edge(edges_to_remove[i][0], edges_to_remove[i][1])

unittest.main()
