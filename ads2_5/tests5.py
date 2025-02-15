''' Tests for lesson 5 solution. '''

import unittest
from typing import Tuple
from solution5 import FormBBSTArray, GenerateBBSTArray, find_node_by_key, delete_node_by_key, nodes_except_one_inorder

class GenerateBBSTArrayTests(unittest.TestCase):
    ''' Tests for GenerateBBSTArray function. '''
    def test_on_empty_list(self) -> None:
        ''' Expected empty list. '''
        self.assertEqual(GenerateBBSTArray([]), [])

    def test_on_single_element_list(self) -> None:
        ''' Expected same list as passed. '''
        self.assertEqual(GenerateBBSTArray([5]), [5])

    def test_on_three_element_lists(self) -> None:
        ''' Expected same resulting list for each of 6 input combinations. '''
        test_lists : list[list[int]] = [[1, 2, 3], [1, 3, 2], [2, 1, 3],
            [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        result : list[int] = [2, 1, 3]
        for i, test_list in enumerate(test_lists):
            with self.subTest(i = i, test_list = test_list, expected_result = result):
                self.assertEqual(GenerateBBSTArray(test_list), result)

    def test_on_seven_element_list(self) -> None:
        ''' Expected same list as defined in the result variable. '''
        values : list[int] = [7, 5, 4, 3, 1, 2, 6]
        result : list[int] = [4, 2, 6, 1, 3, 5, 7]
        self.assertEqual(GenerateBBSTArray(values), result)

    def test_on_fifteen_element_list(self) -> None:
        ''' Expected same list as defined in the result variable. '''
        values : list[int] = [15, 14, 13, 12, 10, 11, 9, 8, 7, 1, 2, 3, 4, 6, 5]
        result : list[int] = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
        self.assertEqual(GenerateBBSTArray(values), result)

    def test_find_on_empty_list(self) -> None:
        ''' Expected "None" for each key. '''
        keys : list[int] = [-14256262637373632636512555, -1, 0, 1, 526373763478473621416765434]
        for key in keys:
            with self.subTest():
                self.assertIsNone(find_node_by_key([], key))

    def test_find_on_one_element_list(self) -> None:
        ''' The only case with non-None result is when key is exactly as in root. '''
        key_result_pairs : list[Tuple[int, int]] = [
            (-1, None),
            (0, None),
            (1, None),
            (3, None),
            (4, 0),
            (5, None)
        ]
        for key_result in key_result_pairs:
            with self.subTest():
                self.assertEqual(find_node_by_key([4], key_result[0]), key_result[1])

    def test_find_on_fifteen_element_list(self) -> None:
        ''' Found index must be the same as via standard python search for list. '''
        BBSTArray : list[int] = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
        keys : list[int] = [-100, -1, 0, 1, 4, 7, 15, 8, 55, 100]
        for key in keys:
            with self.subTest():
                self.assertEqual(find_node_by_key(BBSTArray, key),
                    BBSTArray.index(key) if key in BBSTArray else None)

    def test_nodes_except_inorder_on_empty_tree(self) -> None:
        ''' Expected empty list as the result. '''
        self.assertEqual(nodes_except_one_inorder([], 0, None), [])
        self.assertEqual(nodes_except_one_inorder([], 0, 0), [])

    def test_inorder_traversal_on_one_node_tree(self) -> None:
        ''' Expected list with root node. '''
        self.assertEqual(nodes_except_one_inorder([5], 0, -1), [5])
        self.assertEqual(nodes_except_one_inorder([5], 0, 5), [])

    def test_inorder_traversal_on_fifteen_node_tree(self) -> None:
        ''' Expected keys in sorted order. '''
        self.assertEqual(
            nodes_except_one_inorder([8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15], 0, -1),
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
        self.assertEqual(
            nodes_except_one_inorder([8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15], 0, 8),
            [1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15])

    def test_delete_node_on_empty_tree(self) -> None:
        ''' Expected empty tree as a result. '''
        self.assertEqual(delete_node_by_key([], 0), [])

    def test_delete_node_on_one_node_tree(self) -> None:
        ''' Returns empty tree only in case where key matches node key. '''
        keys : list[int] = [-5, -1, 0, 1, 5]
        for key in keys:
            with self.subTest():
                self.assertEqual(delete_node_by_key([5], key), [None] if key == 5 else [5])

    def test_delete_node_on_fifteen_node_tree(self) -> None:
        ''' Continiously delete keys until tree is empty. '''
        tree : list[int] = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
        keys_in_deletion_order : list[int] = [10, 12, 1, 3, 11, 5, 7, 8, 9, 2, 15, 6, 4, 13, 14]
        sorted_tree : list[int] = sorted(tree)
        for _, key in enumerate(keys_in_deletion_order):
            with self.subTest():
                sorted_tree.remove(key)
                expected_tree : list[int] = FormBBSTArray(
                    sorted_tree, 0, len(sorted_tree) - 1, 0, [None] * len(keys_in_deletion_order))
                tree = delete_node_by_key(tree, key)
                self.assertEqual(tree, expected_tree)

unittest.main()
