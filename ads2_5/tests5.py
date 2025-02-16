''' Tests for lesson 5 solution. '''

import unittest
from typing import Tuple
from solution5 import GenerateBBSTArray, find_node_by_key

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
        Balanced_BST : list[int] = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
        keys : list[int] = [-100, -1, 0, 1, 4, 7, 15, 8, 55, 100]
        for key in keys:
            with self.subTest():
                self.assertEqual(find_node_by_key(Balanced_BST, key),
                    Balanced_BST.index(key) if key in Balanced_BST else None)

unittest.main()
