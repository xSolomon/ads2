''' Tests for lesson 7 tasks 1-3 solution. '''

import unittest
from solution7_1 import Heap

class HeapTests(unittest.TestCase):
    ''' Tests for MakeHeap, Add, GetMax functions. '''
    def setUp(self) -> None:
        ''' Test preparations. '''
        self.heap = Heap()

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

    def test_add_on_empty_one_element_heap(self) -> None:
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


unittest.main()
