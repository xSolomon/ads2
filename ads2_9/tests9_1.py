''' Tests for lesson 9 task 1 solution. '''

import unittest
from solution9_1 import SimpleTreeNode, SimpleTree

class HeapTests(unittest.TestCase):
    ''' Tests for MakeHeap, Add, GetMax functions. '''
    def setUp(self) -> None:
        ''' Test preparations. '''
        self.tree = SimpleTree(None)

    def tearDown(self) -> None:
        ''' Aftertest cleanup. '''
        self.tree = None

    def test_on_empty_tree(self) -> None:
        ''' Must return an empty list. '''
        self.assertEqual(self.tree.EvenTrees(), [])

unittest.main()
