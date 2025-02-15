''' Tests for BST via array methods. '''

import unittest
from typing import Tuple
from solution4 import aBST

class ABSTTests(unittest.TestCase):
    ''' Tests for aBST FindKeyIndex and Addkey methods. '''
    def test_find_and_add_on_empty_tree(self) -> None:
        ''' Expected find to give root key (0).
            Also add must be root. '''
        tree : aBST = aBST(0)
        self.assertEqual(tree.FindKeyIndex(123), 0)
        self.assertEqual(tree.AddKey(123), 0)
        self.assertIsNotNone(tree.Tree[0])
        self.assertEqual(tree.FindKeyIndex(123), 0)

    def test_find_and_add_on_ten_node_tree(self) -> None:
        ''' Node values (in insert order) are:
            50, 25, 75, 37, 62, 84, 31, 43, 55, 92
            Expected correct BST form. '''
        tree : aBST = aBST(3)
        values : list[int] = [50, 25, 75, 37, 62, 84, 31, 43, 55, 92]
        indexes : list[int] = [0, 1, 2, 4, 5, 6, 9, 10, 11, 14]
        for i, key in enumerate(values):
            with self.subTest(i = i, key = key, index = indexes[i]):
                self.assertEqual(tree.AddKey(key), indexes[i])
        for i, key in enumerate(values):
            with self.subTest(i = i, key = key, index = indexes[i]):
                self.assertEqual(tree.FindKeyIndex(key), indexes[i])
                self.assertEqual(tree.AddKey(key), indexes[i])

    def test_lca_on_empty_tree(self) -> None:
        ''' Expected "None" value for each pair of values. '''
        tree : aBST = aBST(0)
        value_pairs : list[Tuple[int, int]] = [
            (-5, -8),
            (-3, -3),
            (0, 0),
            (4, 4),
            (-4, 4),
            (4, -4),
            (0, -1),
            (1, 0)
        ]
        for value_pair in value_pairs:
            with self.subTest():
                self.assertIsNone(tree.lca(value_pair[0], value_pair[1]))

    def test_lca_on_single_node_tree(self) -> None:
        ''' Only case with not "None" value is when either values are root value. '''
        tree : aBST = aBST(1)
        tree.AddKey(10)
        val_pairs_and_results : list[Tuple[int, int, int]] = [
            (-5, -8, None),
            (-3, -3, None),
            (0, 0, None),
            (4, 4, None),
            (-4, 4, None),
            (4, -4, None),
            (0, -1, None),
            (1, 0, None),
            (10, 10, 10)
        ]
        for val_pair_and_result in val_pairs_and_results:
            with self.subTest():
                self.assertEqual(tree.lca(val_pair_and_result[0], val_pair_and_result[1]),
                    val_pair_and_result[2])

    def test_lca_on_three_depth_tree(self) -> None:
        ''' Tests on 3-level tree with some missing nodes. '''
        tree : aBST = aBST(3)
        node_values : list[int] = [50, 25, 75, 37, 62, 84, 31, 43, 55, 92]
        for node_value in node_values:
            tree.AddKey(node_value)
        val_pairs_and_results : list[Tuple[int, int, int]] = [
            (31, 43, 37),
            (31, 37, 37),
            (31, 25, 25),
            (31, 50, 50),
            (31, 125, None),
            (50, 50, 50),
            (75, 25, 50),
            (43, 75, 50),
            (31, 55, 50),
            (55, 92, 75),
            (62, 84, 75)
            ]
        for val_pair_and_result in val_pairs_and_results:
            with self.subTest(value_pair_and_result = val_pair_and_result):
                self.assertEqual(tree.lca(val_pair_and_result[0], val_pair_and_result[1]),
                    val_pair_and_result[2])

    def test_bfs_on_empty_tree(self) -> None:
        ''' Expects empty tuple. '''
        tree : aBST = aBST(0)
        self.assertEqual(tree.bfs(), [])

    def test_bfs_on_single_node_tree(self) -> None:
        ''' Expects tuple with root node. '''
        tree : aBST = aBST(0)
        tree.AddKey(5)
        self.assertEqual(tree.bfs(), [5])

    def test_bfs_on_full_four_depth_tree(self) -> None:
        ''' Must return all 31 nodes in level-order way. '''
        tree : aBST = aBST(3)
        node_values : list[int] = [50, 25, 75, 37, 62, 84, 31, 43, 55, 92]
        for key in node_values:
            tree.AddKey(key)
        self.assertEqual(tree.bfs(), node_values)

unittest.main()
