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

    def testMakeHeapOnEmptyArray(self) -> None:
        ''' Heap size = 1, no elements. '''
        self.heap.MakeHeap([], 0)
        self.assertEqual(len(self.heap.HeapArray), 1)
        self.assertEqual(self.heap.first_free_index, 0)
        self.assertIsNone(self.heap.HeapArray[0])

unittest.main()
