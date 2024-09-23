''' Lesson 4 solution. '''

class aBST:
    ''' Binary search tree via array. '''
    def __init__(self, depth : int):
        if depth < 0:
            depth = 0
        tree_size : int = pow(2, depth + 1) - 1
        self.TreeDepth : int = depth # Store depth to simplify work with tree.
        self.Tree = [None] * tree_size # Array of keys (tree modes).
	
    def FindKeyIndex(self, key):
        # ищем в массиве индекс ключа
        return None # не найден
	
    def AddKey(self, key) -> int:
        ''' Adds key in tree and return its index, -1 if failed adding. '''
        current_node_index : int = 0
        for i in range(self.TreeDepth + 1):
            if self.Tree[current_node_index] is None or self.Tree[current_node_index] == key:
                self.Tree[current_node_index] = key
                return current_node_index
            if self.Tree[current_node_index] > key:
                    current_node_index = 2 * i + 1
                    continue
            current_node_index = 2 * i + 2
        return -1





