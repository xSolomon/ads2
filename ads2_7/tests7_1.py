''' Tests for lesson 7 tasks 1-3 solution. '''

import unittest
from typing import Tuple
from solution7_1 import Heap

class HeapTests(unittest.TestCase):
    ''' Tests for MakeHeap, Add, GetMax functions. '''
    def setUp(self) -> None:
        ''' Test preparations. '''
        self.heap : Heap = Heap()

    def tearDown(self) -> None:
        ''' Aftertest cleanup. '''
        self.heap = None

    def test_make_heap_on_empty_array(self) -> None:
        ''' Heap size = 1, no elements. '''
        self.heap.MakeHeap([], 0)
        self.assertEqual(len(self.heap.HeapArray), 1)
        self.assertEqual(self.heap.first_free_index, 0)
        self.assertIsNone(self.heap.HeapArray[0])

    def test_get_max_on_empty_one_element_heap(self) -> None:
        ''' Nothing should change. '''
        self.heap.MakeHeap([], 0)
        self.assertEqual(self.heap.GetMax(), -1)
        self.assertEqual(self.heap.first_free_index, 0)
        self.assertIsNone(self.heap.HeapArray[0])

    def test_add_on_empty_heap(self) -> None:
        ''' Element must be exactly first in the list. '''
        self.heap.MakeHeap([], 0)
        self.assertTrue(self.heap.Add(5))
        self.assertEqual(self.heap.first_free_index, 1)
        self.assertEqual(self.heap.HeapArray[0], 5)

    def test_make_heap_on_one_element_array(self) -> None:
        ''' Element must be root for each of input. '''
        input_arrays : list[list[int]] = [[5], [1], [2], [4], [81]]
        depths : list[int] = [0, 1, 2, 4, 10]
        for i, _ in enumerate(input_arrays):
            with self.subTest():
                test_heap : Heap = Heap()
                test_heap.MakeHeap(input_arrays[i], depths[i])
                self.assertEqual(len(test_heap.HeapArray), pow(2, depths[i] + 1) - 1)
                self.assertEqual(test_heap.first_free_index, 1)
                self.assertEqual(test_heap.HeapArray[0], input_arrays[i][0])

    def test_is_correct_on_empty_heap(self) -> None:
        ''' Empty heap is always correct. '''
        self.heap.MakeHeap([], 0)
        self.assertTrue(self.heap.is_correct())

    def test_is_correct_on_one_element_heap(self) -> None:
        ''' Heap with one element is always correct. '''
        self.heap.MakeHeap([5], 0)
        self.assertTrue(self.heap.is_correct())

    def test_on_correct_fifteen_element_heap(self) -> None:
        ''' Test varios methods for heap with 15 starting elements. '''
        self.heap.MakeHeap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 4)
        self.assertTrue(self.heap.is_correct())
        self.assertTrue(self.heap.Add(0))
        self.assertTrue(self.heap.is_correct())
        self.assertTrue(self.heap.Add(20))
        self.assertTrue(self.heap.is_correct())
        self.assertTrue(self.heap.Add(20))
        self.assertTrue(self.heap.is_correct())
        self.assertEqual(self.heap.GetMax(), 20)
        self.assertTrue(self.heap.is_correct())
        self.assertTrue(self.heap.Add(20))
        self.assertTrue(self.heap.is_correct())
        self.assertEqual(self.heap.GetMax(), 20)
        self.assertEqual(self.heap.GetMax(), 20)
        self.assertEqual(self.heap.GetMax(), 15)
        self.assertTrue(self.heap.is_correct())

    def test_range_search_on_empty_heap(self) -> None:
        ''' Must return -1 for any search range. '''
        self.heap.MakeHeap([], 0)
        search_ranges : list[Tuple[int, int]] = [
            (-100, 100),
            (-1, 1),
            (0, 0),
            (1, -1)
        ]
        for search_range in search_ranges:
            with self.subTest():
                self.assertEqual(self.heap.find_max_in_range(search_range[0], search_range[1]), -1)

    def test_range_search_on_one_element_heap(self) -> None:
        ''' Must return that element when it's in search range.
            Otherwise must return -1. '''
        self.heap.MakeHeap([10], 0)
        search_ranges : list[Tuple[int, int]] = [
            (-100, 100),
            (-1, 1),
            (0, 0),
            (1, -1),
            (10, 10),
            (15, 8),
            (10, 11),
            (9, 10)
        ]
        for search_range in search_ranges:
            expected_result : int = 10 if 10 >= search_range[0] and 10 <= search_range[1] else -1
            with self.subTest():
                self.assertEqual(self.heap.find_max_in_range(search_range[0], search_range[1]),
                    expected_result)

    def test_range_search_on_fifteen_element_heap(self) -> None:
        ''' Must return max element if any matches range.
            Must return -1 otherwise. '''
        elements : list[int] = range(1, 16)
        self.heap.MakeHeap(elements,4)
        self.assertTrue(self.heap.is_correct())
        self.assertEqual(self.heap.size(), 15)
        search_ranges : list[Tuple[int, int]] = [
            (-100, 100),
            (-1, 1),
            (0, 0),
            (1, -1),
            (10, 10),
            (15, 8),
            (10, 11),
            (9, 10),
            (-1, 1),
            (15, 16),
            (15, 15),
            (1, 1),
            (7, 8),
            (5, 15),
            (1, 15),
            (0, 15),
            (1, 16),
        ]
        elements_set : set = set(elements)
        for search_range in search_ranges:
            ranges_intersection : set = elements_set.intersection(
                range(search_range[0], search_range[1] + 1))
            expected_result : int = max(ranges_intersection) if ranges_intersection else -1
            with self.subTest(search_range = search_range, expected_max = expected_result):
                self.assertEqual(self.heap.find_max_in_range(search_range[0], search_range[1]),
                    expected_result)

    def test_size_on_empty_heap(self) -> None:
        ''' Must return 0. '''
        self.heap.MakeHeap([], 1)
        self.assertEqual(self.heap.size(), 0)
        self.heap.GetMax()
        self.assertEqual(self.heap.size(), 0)

    def test_size_on_one_element_heap(self) -> None:
        ''' Adds one element to the heap, then removes it and adds again.
            Size must change accordingly. '''
        self.heap.MakeHeap([8], 0)
        self.heap.Add(5)
        self.assertEqual(self.heap.size(), 1)
        self.heap.GetMax()
        self.assertEqual(self.heap.size(), 0)
        self.heap.Add(10)
        self.heap.Add(10)
        self.assertEqual(self.heap.size(), 1)

    def test_size_on_fifteen_element_heap(self) -> None:
        ''' Creates fully filled heap, then emptyies it and fills again.
            After every operation, size must change accordingly. '''
        self.heap.MakeHeap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 3)
        self.assertEqual(self.heap.size(), 15)
        with self.subTest():
            for i in range(15):
                self.heap.GetMax()
                self.assertEqual(self.heap.size(), 15 - i - 1)
            self.heap.GetMax()
            self.assertEqual(self.heap.size(), 0)
        with self.subTest():
            for i in range(15):
                self.heap.Add(i)
                self.assertEqual(self.heap.size(), i + 1)
            self.heap.Add(100)
            self.assertEqual(self.heap.size(), 15)

    def test_merge_on_empty_heaps(self) -> None:
        ''' Must create another empty heap. '''
        first_heap : Heap = Heap()
        second_heap : Heap = Heap()
        first_heap.MakeHeap([], 0)
        second_heap.MakeHeap([], 0)
        merged_heap : Heap = first_heap.merge_heap(second_heap)
        self.assertTrue(merged_heap.is_correct())
        self.assertEqual(merged_heap.size(), 0)

    def test_merge_with_one_empty_heap(self) -> None:
        ''' Test merging non-empty and empty heap.
            New heap size must be equal to non-empty heap size. '''
        first_heap : Heap = Heap()
        second_heap : Heap = Heap()
        first_heap.MakeHeap([1, 2, 3], 1)
        second_heap.MakeHeap([], 0)
        with self.subTest():
            merged_heap : Heap = first_heap.merge_heap(second_heap)
            self.assertTrue(merged_heap.is_correct())
            self.assertEqual(merged_heap.size(), 3)
        first_heap.MakeHeap([], 0)
        second_heap.MakeHeap([1, 2, 3], 1)
        with self.subTest():
            merged_heap : Heap = first_heap.merge_heap(second_heap)
            self.assertTrue(merged_heap.is_correct())
            self.assertEqual(merged_heap.size(), 3)

    def test_merge_on_predefined_heaps(self) -> None:
        ''' New heap must be correct and have enough size for all elements. '''
        first_heap : Heap = Heap()
        second_heap : Heap = Heap()
        first_heap.MakeHeap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 3)
        second_heap.MakeHeap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 3)
        with self.subTest(i = 0):
            merged_heap : Heap = first_heap.merge_heap(second_heap)
            self.assertTrue(merged_heap.is_correct())
            self.assertEqual(merged_heap.size(), 30)
        first_heap.MakeHeap([1, 2, 3, 4, 5, 6, 7], 2)
        second_heap.MakeHeap([8, 9, 10, 11, 12, 13, 14, 15], 3)
        with self.subTest(i = 1):
            merged_heap : Heap = first_heap.merge_heap(second_heap)
            self.assertTrue(merged_heap.is_correct())
            self.assertEqual(merged_heap.size(), 15)
        first_heap.MakeHeap([1, 2, 3, 4, 5, 6, 7], 2)
        second_heap.MakeHeap([8, 9, 10, 11, 12, 13, 14, 15, 16], 3)
        with self.subTest(i = 2):
            merged_heap : Heap = first_heap.merge_heap(second_heap)
            self.assertTrue(merged_heap.is_correct())
            self.assertEqual(merged_heap.size(), 16)
        first_heap.MakeHeap([1, 1, 1, 1, 1, 1, 1], 2)
        second_heap.MakeHeap([1, 1, 1, 1, 1, 1, 1, 1, 1], 3)
        with self.subTest(i = 3):
            merged_heap : Heap = first_heap.merge_heap(second_heap)
            self.assertTrue(merged_heap.is_correct())
            self.assertEqual(merged_heap.size(), 16)

unittest.main()
