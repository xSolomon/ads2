''' Tests for lesson 12 task 1 solution. '''

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

    def test_on_empty_graphs(self) -> None:
        ''' Must return empty list for each graph. '''
        graphs : list[SimpleGraph] = [SimpleGraph(1), SimpleGraph(2),
            self.form_graph(3, [None, None, None], [])]
        for graph in graphs:
            with self.subTest():
                self.assertEqual(graph.WeakVertices(), [])

    def test_on_singlenode_graphs(self) -> None:
        ''' Must return that single node independent of vertex. '''
        graphs : list[SimpleGraph] = [self.form_graph(1, [5], []),
            self.form_graph(1, [7], [(0, 0)]), self.form_graph(3, [2, None, None], []),
            self.form_graph(3, [2, None, None], [(1, 1)])]
        for graph in graphs:
            with self.subTest():
                self.assertEqual(graph.WeakVertices(), [graph.vertex[0]])

    def test_on_predefined_graphs(self) -> None:
        ''' For each graph, resulting list must be exactly the same as in the results list. '''
        graphs : list[SimpleGraph] = [
            self.form_graph(5, [1, 2, 3, 4, 5], [(0, 1), (0, 2), (0, 3), (1, 3), (1, 4), (2, 3), (3, 3), (3, 4)]),
            self.form_graph(5, [1, 2, 3, 4, 5], []),
            self.form_graph(5, [1, 2, 3, 4, 5], [(0, 1), (0, 2), (1, 4), (3, 3)]),
            self.form_graph(5, [1, 2, 3, 4, 5], [(0, 1), (0, 2), (0, 3), (1, 3), (1, 4), (2, 3), (3, 3)]),
            self.form_graph(5, [1, 2, 3, 4, 5], [(0, 1), (0, 2), (1, 3), (1, 4), (2, 3), (3, 3), (3, 4)]),
            self.form_graph(5, [1, 2, 3, 4, 5], [(0, 1), (0, 2), (0, 3), (1, 3), (1, 4), (2, 3), (3, 4)]),
            self.form_graph(5, [1, 2, 3, 4, 5], [(0, 1), (0, 3), (1, 3), (1, 4), (2, 3), (3, 3), (3, 4)]),
            self.form_graph(5, [1, 2, 3, 4, 5], [(0, 1), (0, 3), (1, 3), (2, 3), (3, 3), (3, 4)]),
            self.form_graph(5, [1, 2, 3, 4, 5],[(0, 1), (0, 3), (1, 3), (3, 3)]),
        ]
        results : list[list[Vertex]] = [
            [],
            [graphs[1].vertex[0], graphs[1].vertex[1], graphs[1].vertex[2], graphs[1].vertex[3], graphs[1].vertex[4]],
            [graphs[2].vertex[0], graphs[2].vertex[1], graphs[2].vertex[2], graphs[2].vertex[3], graphs[2].vertex[4]],
            [graphs[3].vertex[4]],
            [graphs[4].vertex[0], graphs[4].vertex[2]],
            [],
            [graphs[6].vertex[2]],
            [graphs[7].vertex[2], graphs[7].vertex[4]],
            [graphs[8].vertex[2], graphs[8].vertex[4]]
        ]
        for i, graph in enumerate(graphs):
            with self.subTest(i = i):
                self.assertEqual(graph.WeakVertices(), results[i])

unittest.main()
