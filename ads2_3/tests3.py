''' Tests for lesson 2 Binary Search Tree methods. '''

import unittest
from solution3 import BSTNode, BSTFind, BST

class BSTTests(unittest.TestCase):
    ''' Tests for BST depth and breadth traversals. '''
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
        ''' Expected each traversal to return empty tuple. '''
        self.assertEqual(self.tree.DeepAllNodes(0), ())
        self.assertEqual(self.tree.DeepAllNodes(1), ())
        self.assertEqual(self.tree.DeepAllNodes(2), ())
        self.assertEqual(self.tree.WideAllNodes(), ())

    def test_on_small_predefined_tree(self) -> None:
        ''' Test functions on tree with three nodes (root with two childs).
            Root = 8, left child = 4, right child = 12. '''
        self.assertTrue(self.tree.AddKeyValue(8, 8))
        self.assertTrue(self.tree.AddKeyValue(4, 4))
        self.assertTrue(self.tree.AddKeyValue(12, 12))
        self.assertEqual(self.tree.DeepAllNodes(0),
            (self.tree.Root.LeftChild, self.tree.Root, self.tree.Root.RightChild))
        self.assertEqual(self.tree.DeepAllNodes(1),
            (self.tree.Root.LeftChild, self.tree.Root.RightChild, self.tree.Root))
        self.assertEqual(self.tree.DeepAllNodes(2),
            (self.tree.Root, self.tree.Root.LeftChild, self.tree.Root.RightChild))
        self.assertEqual(self.tree.WideAllNodes(),
            (self.tree.Root, self.tree.Root.LeftChild, self.tree.Root.RightChild))

    def test_on_medium_predefined_tree(self) -> None:
        ''' Test on tree with 15 nodes total (with keys from 1 to 15). '''
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
        root = self.tree.Root
        breadth_traversal : tuple[BSTNode] = (root, root.LeftChild, root.RightChild,
        root.LeftChild.LeftChild, root.LeftChild.RightChild, root.RightChild.LeftChild,
        root.RightChild.RightChild, root.LeftChild.LeftChild.LeftChild,
        root.LeftChild.LeftChild.RightChild, root.LeftChild.RightChild.LeftChild,
        root.LeftChild.RightChild.RightChild, root.RightChild.LeftChild.LeftChild,
        root.RightChild.LeftChild.RightChild, root.RightChild.RightChild.LeftChild,
        root.RightChild.RightChild.RightChild)
        depth_in_order : tuple[BSTNode] = (breadth_traversal[7],)
        self.assertEqual(self.tree.WideAllNodes(), breadth_traversal)

unittest.main()
