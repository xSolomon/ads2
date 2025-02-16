''' Tests for lesson 5 task 3 solution. '''

import unittest
from typing import Tuple
from solution5_3 import BalancedBST

class BalancedBSTTests(unittest.TestCase):
    ''' Tests for inorder, bst_from_sorted_array and delete_node_by_key functions. '''
    def setUp(self) -> None:
        ''' Test preparations. '''
        self.tree : BalancedBST = BalancedBST(0)

    def tearDown(self) -> None:
        ''' Aftertest cleanup. '''
        self.tree = None

    def test_inorder_on_empty_tree(self) -> None:
        ''' Expected empty list independent of predicate function. '''
        self.assertEqual(self.tree.inorder(0, lambda key : True), [])
        self.assertEqual(self.tree.inorder(0, lambda key : False), [])
        self.assertEqual(self.tree.inorder(0, lambda key : key == 0), [])

    def test_inorder_on_one_node_tree(self) -> None:
        ''' Expected list with root node for second and third predicates. '''
        self.tree.bst_from_sorted_array(0, [5])
        self.assertEqual(self.tree.inorder(0, lambda key : False), [])
        self.assertEqual(self.tree.inorder(0, lambda key : True), [5])
        self.assertEqual(self.tree.inorder(0, lambda key : key == 5), [5])

    def test_inorder_traversal_on_fifteen_node_tree(self) -> None:
        ''' Expected keys in sorted order for first case.
            Expected empty list in second case.
            List with only even values in third case.
            Values less than 10 in fourth case.'''
        values : list[int] = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
        self.tree.bst_from_sorted_array(3, sorted(values))
        self.assertEqual(self.tree.inorder(0, lambda key : True), sorted(values))
        self.assertEqual(self.tree.inorder(0, lambda key : False), [])
        self.assertEqual(self.tree.inorder(0, lambda key : key % 2 == 0), [2, 4, 6, 8, 10, 12, 14])
        self.assertEqual(self.tree.inorder(0, lambda key : key < 10), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_bst_from_sorted_array(self) -> None:
        ''' Tries to make bst from different input arrays. '''
        trees : Tuple[int, list[int]] = [
            (0, []),
            (0, [0]),
            (1, [1, 2, 3]),
            (2, [1, 2, 3, 4, 5, 6, 7]),
            (3, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
        ]
        for tree in trees:
            with self.subTest():
                self.tree.bst_from_sorted_array(tree[0], tree[1])
                self.assertEqual(
                    self.tree.inorder(0, lambda key : True),
                    tree[1])

    def test_delete_node_on_empty_tree(self) -> None:
        ''' Expected empty list for each key. '''
        keys : list[int] = [-5, 1, 0, 1, 5]
        for key in keys:
            with self.subTest():
                self.tree.delete_node_by_key(key)
                self.assertEqual(self.tree.inorder(0, lambda key : True), [])

    def test_delete_node_on_one_node_tree(self) -> None:
        ''' Returns empty tree only in case where key matches node key. '''
        keys : list[int] = [-5, -1, 0, 1, 5]
        for key in keys:
            with self.subTest():
                self.tree.bst_from_sorted_array(0, [0])
                self.tree.delete_node_by_key(key)
                self.assertEqual(self.tree.inorder(0, lambda key : True),
                    [] if key == 0 else [0])

    def test_delete_node_on_fifteen_node_tree(self) -> None:
        ''' Continiously delete keys until tree is empty. '''
        keys : list[int] = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
        keys_in_deletion_order : list[int] = [10, 12, 1, 3, 11, 5, 7, 8, 9, 2, 15, 6, 4, 13, 14]
        inorder_keys : list[int] = sorted(keys)
        self.tree.bst_from_sorted_array(3, inorder_keys)
        for _, key in enumerate(keys_in_deletion_order):
            with self.subTest(key_to_delete = key):
                inorder_keys.remove(key)
                self.tree.delete_node_by_key(key)
                self.assertEqual(self.tree.inorder(0, lambda key : True), inorder_keys)

unittest.main()
