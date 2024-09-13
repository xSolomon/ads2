''' Tests for lesson 2 Binary Search Tree methods. '''

import unittest
from solution2 import BSTNode, BSTFind, BST

class BSTTests(unittest.TestCase):
    ''' Tests for BST FindNodeByKey, AddKeyValue, FinMinMax, DeleteNodeByKey,
        Count methods. '''
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
        ''' Expected nodes count = 0.
            Find must have None in Node field.
            Delete must always be False.
            Min and Max should be None.'''
        self.assertEqual(self.tree.Count(), 0)
        self.assertIsNone(self.tree.FindNodeByKey(None).Node)
        self.assertIsNone(self.tree.FindNodeByKey(1).Node)
        self.assertIsNone(self.tree.FindNodeByKey('abc').Node)
        self.assertIsNone(self.tree.FindNodeByKey(True).Node)
        self.assertFalse(self.tree.DeleteNodeByKey(None))
        self.assertFalse(self.tree.DeleteNodeByKey(1))
        self.assertFalse(self.tree.DeleteNodeByKey('abc'))
        self.assertFalse(self.tree.DeleteNodeByKey(True))
        self.assertIsNone(self.tree.FinMinMax(self.tree.Root, True))
        self.assertIsNone(self.tree.FinMinMax(self.tree.Root, False))

    def test_add_find_delete_in_empty_tree(self) -> None:
        ''' Tree size should be 1, new node must be root node.
            Find must return root node, delete must be successful. '''
        self.assertTrue(self.tree.AddKeyValue(5, 5))
        self.assertEqual(self.tree.Count(), 1)
        self.assertIsNotNone(self.tree.Root)
        self.assertIs(self.tree.FindNodeByKey(5).Node, self.tree.Root)
        self.assertTrue(self.tree.DeleteNodeByKey(5))

    def test_on_small_predefined_tree(self) -> None:
        ''' Test functions on tree with three nodes (root with two childs).
            Root = 8, left child = 4, right child = 12. '''
        self.assertTrue(self.tree.AddKeyValue(8, 8))
        self.assertTrue(self.tree.AddKeyValue(4, 4))
        self.assertTrue(self.tree.AddKeyValue(12, 12))
        self.assertEqual(self.tree.Count(), 3)
        self.assertIs(self.tree.FindNodeByKey(4).Node, self.tree.Root.LeftChild)
        self.assertIs(self.tree.FindNodeByKey(3).Node, self.tree.Root.LeftChild)
        self.assertIs(self.tree.FindNodeByKey(5).Node, self.tree.Root.LeftChild)
        self.assertIs(self.tree.FindNodeByKey(8).Node, self.tree.Root)
        self.assertIs(self.tree.FindNodeByKey(12).Node, self.tree.Root.RightChild)
        self.assertIs(self.tree.FindNodeByKey(10).Node, self.tree.Root.RightChild)
        self.assertIs(self.tree.FindNodeByKey(14).Node, self.tree.Root.RightChild)
        self.assertTrue(self.tree.DeleteNodeByKey(8))
        self.assertIsNone(self.tree.Root.RightChild)
        self.assertIsNotNone(self.tree.Root.LeftChild)
        self.assertEqual(self.tree.Count(), 2)
        self.assertIs(self.tree.FindNodeByKey(4).Node, self.tree.Root.LeftChild)
        self.assertIs(self.tree.FindNodeByKey(12).Node, self.tree.Root)
        self.assertTrue(self.tree.DeleteNodeByKey(12))
        self.assertTrue(self.tree.DeleteNodeByKey(4))
        self.assertEqual(self.tree.Count(), 0)

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
        self.assertEqual(self.tree.Count(), 15)
        for i in range(15):
            with self.subTest(i = i, NodeValue = i + 1):
                search_result : BSTFind = self.tree.FindNodeByKey(i + 1)
                self.assertTrue(search_result.NodeHasKey)
                node_to_check : BSTNode = search_result.Node
                self.assertEqual(node_to_check.NodeKey, i + 1)
                if node_to_check.NodeKey % 2 == 1:
                    self.assertTrue(self.tree._IsLeaf(node_to_check))
                if node_to_check.NodeKey % 2 == 0:
                    self.assertFalse(self.tree._IsLeaf(node_to_check))
        self.tree.DeleteNodeByKey(2)
        self.assertFalse(self.tree._IsLeaf(self.tree.FindNodeByKey(3).Node))
        self.tree.DeleteNodeByKey(3)
        self.tree.DeleteNodeByKey(4)
        self.assertFalse(self.tree._IsLeaf(self.tree.FindNodeByKey(5).Node))
        self.tree.DeleteNodeByKey(8)
        self.assertFalse(self.tree._IsLeaf(self.tree.FindNodeByKey(9).Node))
        self.assertEqual(self.tree.Root.NodeKey, 9)
        self.tree.DeleteNodeByKey(13)
        self.tree.DeleteNodeByKey(9)
        self.assertEqual(self.tree.Root.NodeKey, 10)

unittest.main()
