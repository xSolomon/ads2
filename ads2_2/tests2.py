''' Tests for lesson 2 Binary Search Tree methods. '''

import unittest
from solution2 import BSTNode, BSTFind, BST
from typing import Tuple

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

    def insert_values(self, values : list[int]) -> None:
        ''' Adds values to the tree one-by-one. Assumes key is the same as value. '''
        for value in values:
            self.tree.AddKeyValue(value, value)

    def insert_values_in_tree(self, tree : BST, values : list[int]) -> None:
        ''' Adds values to the given tree one-by-one. Assumes key is the same as value. '''
        for value in values:
            tree.AddKeyValue(value, value)

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

    def test_on_three_node_tree(self) -> None:
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
        self.assertIs(self.tree.FinMinMax(self.tree.Root, True), self.tree.Root.RightChild)
        self.assertIs(self.tree.FinMinMax(self.tree.Root, False), self.tree.Root.LeftChild)
        self.assertTrue(self.tree.DeleteNodeByKey(8))
        self.assertIsNone(self.tree.Root.RightChild)
        self.assertIsNotNone(self.tree.Root.LeftChild)
        self.assertEqual(self.tree.Count(), 2)
        self.assertIs(self.tree.FindNodeByKey(4).Node, self.tree.Root.LeftChild)
        self.assertIs(self.tree.FindNodeByKey(12).Node, self.tree.Root)
        self.assertTrue(self.tree.DeleteNodeByKey(12))
        self.assertTrue(self.tree.DeleteNodeByKey(4))
        self.assertEqual(self.tree.Count(), 0)

    def test_on_fifteen_nodes_tree(self) -> None:
        ''' Test on tree with 15 nodes total (with keys from 1 to 15). '''
        self.insert_values([8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15])
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
        self.assertIs(self.tree.FinMinMax(self.tree.Root, True),
            self.tree.Root.RightChild.RightChild.RightChild)
        self.assertIs(self.tree.FinMinMax(self.tree.Root, False),
            self.tree.Root.LeftChild.LeftChild.LeftChild)
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

    def test_paths_finder_on_empty_tree(self) -> None:
        ''' Empty tree always gives empty path list. '''
        self.assertEqual([], self.tree.root_to_leaf_paths(-2))
        self.assertEqual([], self.tree.root_to_leaf_paths(-1))
        self.assertEqual([], self.tree.root_to_leaf_paths(0))
        self.assertEqual([], self.tree.root_to_leaf_paths(1))
        self.assertEqual([], self.tree.root_to_leaf_paths(2))

    def test_path_finder_on_one_node_tree(self) -> None:
        ''' Gives empty paths list for all cases except 1 length paths.
            For 1 legnth, returns single path consisting of tree root. '''
        self.insert_values([10])
        self.assertEqual([], self.tree.root_to_leaf_paths(-2))
        self.assertEqual([], self.tree.root_to_leaf_paths(-1))
        self.assertEqual([], self.tree.root_to_leaf_paths(0))
        self.assertEqual([[self.tree.Root]], self.tree.root_to_leaf_paths(1))
        self.assertEqual([], self.tree.root_to_leaf_paths(2))

    def test_path_finder_on_three_node_trees(self) -> None:
        ''' Expected one path for list-like trees and two paths for balanced version. '''
        trees : list[BST] = [BST(None) for _ in range(3)]
        for tree in trees:
            tree.AddKeyValue(8, 8)
        trees[0].AddKeyValue(4 ,4)
        trees[0].AddKeyValue(2, 2)
        trees[1].AddKeyValue(4, 4)
        trees[1].AddKeyValue(12, 12)
        trees[2].AddKeyValue(10, 10)
        trees[2].AddKeyValue(12, 12)
        lengths : list[int] = [i for i in range(-2, 5)]
        trees_paths_of_lengths : list[list[list[int]]] = [
            [[], [], [], [], [], [[trees[0].Root, trees[0].Root.LeftChild, trees[0].Root.LeftChild.LeftChild]], []],
            [[], [], [], [], [[trees[1].Root, trees[1].Root.LeftChild], [trees[1].Root, trees[1].Root.RightChild]], [], []],
            [[], [], [], [], [], [[trees[2].Root, trees[2].Root.RightChild, trees[2].Root.RightChild.RightChild]], []]
        ] # All results for paths with length from -2 to 4
        for i, tree in enumerate(trees):
            for j, paths_of_lengths in enumerate(trees_paths_of_lengths[i]):
                result : list[list[BSTNode]] = tree.root_to_leaf_paths(lengths[j])
                with self.subTest():
                    self.assertEqual(len(paths_of_lengths), len(result))
                    for k, path in enumerate(result):
                        with self.subTest(i = i, j = j, k = k, path = path):
                            self.assertEqual(len(path), len(paths_of_lengths[k]))
                            self.assertEqual(tree.root_to_leaf_paths(lengths[j]), paths_of_lengths)

    def test_sum_finder_on_empty_tree(self) -> None:
        ''' Empty tree results always gives empty path list. '''
        result : Tuple[int, list[list[BSTNode]]] = self.tree.paths_with_max_sum()
        self.assertEqual(result[1], [])

    def test_sum_finder_on_singlenode_tree(self) -> None:
        ''' Must return exactly one path consisting of root node,
            with max sum equal to root value. '''
        values : list[int] = [-5, -1, 0, 1, 5]
        for value in values:
            self.insert_values([value])
            with self.subTest():
                result : Tuple[int, list[list[BSTNode]]] = self.tree.paths_with_max_sum()
                self.assertEqual(result[0], value)
                self.assertEqual(len(result[1]), 1)
                self.assertEqual(result[1], [[self.tree.Root]])
            self.tree.DeleteNodeByKey(value)

    def test_sum_finder_on_predefined_trees(self) -> None:
        ''' Every case must return at least one path with maximum sum. '''
        trees : list[BST] = [BST(None) for _ in range(5)]
        trees_values : list[list[int]] = [
            [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15], # BBST
            [-8, -4, -12, -2, -6, -10, -14, -1, -3, -5, -7, -9, -11, -13, -15], # Same, negative values
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], # Only right childs
            [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1], # Only left childs
            [24, 25, 11, 13, 1, 10, 3] # 24 + 25 = 49, 24 + 11 + 10 + 3 + 1 = 49, 24 + 11 + 12 = 47
        ]
        for i, tree in enumerate(trees):
            self.insert_values_in_tree(tree, trees_values[i])
        # For every result:
        # maximum sum, number of paths, list of lengths of each path.
        expected_results : list[Tuple[int, int, list[int]]] = [
            (49, 1, [4]),
            (-15, 1, [4]),
            (120, 1, [15]),
            (120, 1, [15]),
            (49, 2, [2, 5])
        ]
        for i, tree in enumerate(trees):
            with self.subTest(i = i):
                method_result : Tuple(int, list[list[BSTNode]]) = tree.paths_with_max_sum()
                self.assertEqual(expected_results[i][0], method_result[0]) # Test if maximum sum is equal
                self.assertEqual(expected_results[i][1], len(method_result[1])) # Test if number of paths is equal
                path_lengths : list[int] = [len(path) for path in method_result[1]]
                for path_len in expected_results[i][2]:
                    self.assertIn(path_len, path_lengths)


unittest.main()
