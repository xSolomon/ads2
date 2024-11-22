''' Tests for lesson 9 task 1 solution. '''

import unittest
from solution10_1 import Vertex, SimpleGraph

class DFSTests(unittest.TestCase):
    ''' Tests for DeepFirstSearch function. '''
    def form_graph(self, size : int) -> SimpleGraph:
        ''' Prepares graph for tests. '''
        return SimpleGraph(size)

unittest.main()
