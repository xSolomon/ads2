''' Tests for lesson 3 task 3. '''

import unittest
from solution3 import BSTNode, BST
from solution3_3 import inverseBST

class BSTTests(unittest.TestCase):
    ''' Tests for inverseBST function. '''
    def setUp(self) -> None:
        ''' Test preparations. '''
        self.tree = BST(None)

    def tearDown(self) -> None:
        ''' Aftertest cleanup. '''
        while self.tree.Count() > 0:
            self.assertTrue(self.tree.DeleteNodeByKey(self.tree.Root.NodeKey))
        self.assertEqual(self.tree.Count(), 0)
        self.assertIsNone(self.tree.Root)
        del self.tree

    def test_on_empty_tree(self) -> None:
        ''' Expected nothing changes. '''
        inverseBST(self.tree)
        self.assertEqual(self.tree.Count(), 0)
        self.assertIsNone(self.tree.Root)

    def test_on_small_predefined_tree(self) -> None:
        ''' Test functions on tree with three nodes (root with two childs).
            Root = 8, left child = 4, right child = 12. '''
        self.assertTrue(self.tree.AddKeyValue(8, 8))
        self.assertTrue(self.tree.AddKeyValue(4, 4))
        self.assertTrue(self.tree.AddKeyValue(12, 12))
        tree_before_inverse : tuple[BSTNode] = self.tree.DeepAllNodes(0)
        inverseBST(self.tree)
        self.assertEqual(self.tree.Count(), 3)
        self.assertEqual(self.tree.DeepAllNodes(0), tree_before_inverse[::-1])

    def test_on_medium_predefined_tree(self) -> None:
        ''' Test on tree with 15 nodes total (with keys from 1 to 15) '''
        self.tree.AddKeyValue(8, 8)
        self.tree.AddKeyValue(4, 4)
        self.tree.AddKeyValue(12, 12)
        self.tree.AddKeyValue(2, 2)
        self.tree.AddKeyValue(6, 6)
        self.tree.AddKeyValue(10, 10)
        self.tree.AddKeyValue(14, 14)
        self.tree.AddKeyValue(1, 1)
        self.tree.AddKeyValue(3, 3)
        self.tree.AddKeyValue(5, 5)
        self.tree.AddKeyValue(7, 7)
        self.tree.AddKeyValue(9, 9)
        self.tree.AddKeyValue(11, 11)
        self.tree.AddKeyValue(13, 13)
        self.tree.AddKeyValue(15, 15)
        tree_before_inverse : tuple[BSTNode] = self.tree.DeepAllNodes(0)
        inverseBST(self.tree)
        self.assertEqual(self.tree.Count(), 15)
        self.assertEqual(self.tree.DeepAllNodes(0), tree_before_inverse[::-1])

unittest.main()
