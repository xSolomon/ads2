''' Lesson 7 tasks 1-3 solution. '''

from typing import Self
import copy
from queue import Queue

class Heap:
    ''' Binary heap. '''
    def __init__(self):
        self.HeapArray : list[int] = [] # Stores non-negative numbers-keys.
        self.heap_depth : int = 0 # Heap depth level.
        self.first_free_index : int = 0 # First index that is free for inserting.

    def MakeHeap(self, a : list[int], depth : int) -> None:
        ''' Makes heap from given array by calling Add for each element. '''
        self.heap_depth = depth
        self.HeapArray = [None] * (pow(2, depth + 1) - 1)
        self.first_free_index = 0
        for _, key in enumerate(a):
            self.Add(key)

    def GetMax(self) -> int:
        ''' Return value contained in root, rebuilding heap via sift down. '''
        if self.size() == 0: # Heap is empty.
            return -1
        deleted_key : int = self.HeapArray[0]
        self.HeapArray[0] = self.HeapArray[self.first_free_index - 1]
        self.HeapArray[self.first_free_index - 1] = None
        self.first_free_index -= 1
        if self.first_free_index == 0: # Deleted last element in heap.
            return deleted_key
        current_index : int = 0
        for _ in range(self.heap_depth):
            left_child_index : int = 2 * current_index + 1
            right_child_index : int = 2 * current_index + 2
            left_value : int = -1 if self.HeapArray[left_child_index] is None \
                else self.HeapArray[left_child_index]
            right_value : int = -1 if self.HeapArray[right_child_index] is None \
                else self.HeapArray[right_child_index]
            max_value : int = max(left_value, right_value)
            if max_value <= self.HeapArray[current_index]:
                return deleted_key
            index_to_swap : int = left_child_index if max_value == left_value else right_child_index
            self.HeapArray[current_index], self.HeapArray[index_to_swap] = \
            self.HeapArray[index_to_swap], self.HeapArray[current_index]
            current_index = index_to_swap
        return deleted_key

    def Add(self, key : int) -> bool:
        ''' Adds element to the heap, sifting it up.
            Returns false if heap is full. '''
        if self.first_free_index == len(self.HeapArray): # Heap if full.
            return False
        if key < 0: # Only non-negative keys are valid.
            return False
        self.HeapArray[self.first_free_index] = key
        current_index : int = self.first_free_index
        self.first_free_index += 1
        for parent_index in range(self.heap_depth + 1):
            parent_index = (current_index - 1) // 2
            if parent_index < 0 or self.HeapArray[parent_index] >= self.HeapArray[current_index]:
                return True
            self.HeapArray[parent_index], self.HeapArray[current_index] = \
                self.HeapArray[current_index], self.HeapArray[parent_index]
            current_index = parent_index
        return True

    def is_correct(self) -> bool:
        ''' Returns True if heap is correct (parent key is greater-equal than children keys). '''
        for node_index, parent_key in enumerate(self.HeapArray):
            if parent_key is None:
                continue
            left_child_index : int = node_index * 2 + 1
            if left_child_index < len(self.HeapArray) and \
                self.HeapArray[left_child_index] is not None and \
                parent_key < self.HeapArray[left_child_index]:
                return False
            right_child_index : int = node_index * 2 + 2
            if right_child_index < len(self.HeapArray) and \
                self.HeapArray[right_child_index] is not None and \
                parent_key < self.HeapArray[right_child_index]:
                return False
        return True

    def find_max_in_range(self, min_val : int, max_val : int) -> int:
        ''' Search for maximum value in range [min, max].
            Returns -1 if no such element. '''
        current_max : int = -1
        index_queue : Queue = Queue()
        index_queue.put(0)
        while not index_queue.empty():
            current_index : int = index_queue.get()
            if current_index >= self.size(): # Index out of heap range.
                continue
            if self.HeapArray[current_index] > max_val: # Not reached search range, continue.
                index_doubled : int = current_index * 2
                index_queue.put(index_doubled + 1)
                index_queue.put(index_doubled + 2)
                continue
            if self.HeapArray[current_index] < min_val: # Passed search range.
                continue
            current_max = max(current_max, self.HeapArray[current_index])
        return current_max

    def size(self) -> int:
        ''' Returns number of keys stored. '''
        return self.first_free_index

    def merge_heap(self, other_heap : Self) -> Self:
        ''' Merges heap with other using only public interface. '''
        merge_heap : Self = copy.deepcopy(self)
        merge_with_heap : Self = copy.deepcopy(other_heap)
        new_heap : Heap = Heap()
        total_elements : int = merge_heap.size() + merge_with_heap.size()
        new_heap_depth : int = 0
        max_elements_with_depth : int = 1
        while max_elements_with_depth < total_elements: # Calculate depth of new heap.
            max_elements_with_depth = max_elements_with_depth * 2 + 1
            new_heap_depth += 1
        new_heap.MakeHeap([], new_heap_depth)
        this_heap_max : int = merge_heap.GetMax()
        other_heap_max : int = merge_with_heap.GetMax()
        while this_heap_max != -1 and other_heap_max != -1:
            if this_heap_max <= other_heap_max:
                new_heap.Add(other_heap_max)
                other_heap_max = merge_with_heap.GetMax()
                continue
            new_heap.Add(this_heap_max)
            this_heap_max = merge_with_heap.GetMax()
        new_heap.Add(this_heap_max)
        new_heap.Add(other_heap_max)
        non_empty_heap : Heap = merge_heap if other_heap_max == -1 else merge_with_heap
        while new_heap.Add(non_empty_heap.GetMax()):
            pass
        return new_heap
