''' Tests for lesson 5 solution. '''

import unittest
from solution5 import GenerateBBSTArray

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

unittest.main()
