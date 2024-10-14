''' Lesson 7 tasks 1-3 solution. '''

class Heap:
    ''' Binary heap. '''
    def __init__(self):
        self.HeapArray : list[int] = [] # Stores non-negative numbers-keys.
        self.heap_depth : int = 0 # Heap depth level.
        self.first_free_index : int = 0 # First index that is free for inserting.

    def MakeHeap(self, a : list[int], depth : int) -> None:
        ''' Makes heap from given array by calling Add for each element. '''
        self.heap_depth = depth
        self.HeapArray = [None] * pow(depth + 1, 2)
        for _, key in enumerate(a):
            self.Add(key)
        self.first_free_index = len(a)

    def GetMax(self) -> int:
        ''' Return value contained in rood, rebuilding heap via sift down. '''
        if self.first_free_index == 0: # Heap is empty.
            return -1
        deleted_key : int = self.HeapArray[0]
        self.HeapArray[0] = self.HeapArray[self.first_free_index - 1]
        self.HeapArray[self.first_free_index - 1] = None
        self.first_free_index -= 1
        if self.first_free_index == 0: # Deleted last element in heap.
            return deleted_key
        current_index : int = 0
        for _ in range(self.heap_depth + 1):
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





