''' Tests for lesson 10 task 2 solution. '''

import unittest
from typing import Tuple
from solution10_2 import DirectedGraph

class DirectedGraphTests(unittest.TestCase):
    ''' Tests for longest_path_len function. '''
    def setUp(self) -> None:
        ''' Test preparation. '''
        self.graph : DirectedGraph = DirectedGraph(5)

    def tearDown(self) -> None:
        ''' Aftertest cleanup. '''
        self.graph = None

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

    def test_longest_path_len_on_graph_without_edges(self) -> None:
        ''' Cause there is no any pathes, maximum length is zero. '''
        self.graph.add_vertex(100)
        self.graph.add_vertex(200)
        self.graph.add_vertex(300)
        self.assertEqual(self.graph.longest_path_length(), 0)

    def test_longest_path_on_graphs_with_one_edge(self) -> None:
        ''' Path length must be 1 except when edge connects same vertex. '''
        self.graph.add_vertex(100)
        self.graph.add_vertex(200)
        self.graph.add_vertex(300)
        self.graph.add_vertex(400)
        self.graph.add_vertex(500)
        self.graph.add_edge(0, 0)
        with self.subTest():
            self.assertEqual(self.graph.longest_path_length(), 0)
        self.graph.add_edge(2, 3)
        with self.subTest():
            self.assertEqual(self.graph.longest_path_length(), 1)
        self.graph.remove_edge(2, 3)
        self.graph.add_edge(0, 3)
        with self.subTest():
            self.assertEqual(self.graph.longest_path_length(), 1)

unittest.main()
