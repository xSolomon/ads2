''' Tests for lesson 10 task 2 solution. '''

import unittest
from solution10_2 import DirectedGraph

class DirectedGraphTests(unittest.TestCase):
    ''' Tests for longest_path_len function. '''
    def setUp(self) -> None:
        ''' Test preparation. '''
        self.graph : DirectedGraph = DirectedGraph(5)

    def tearDown(self) -> None:
        ''' Aftertest cleanup. '''
        self.graph = None

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
