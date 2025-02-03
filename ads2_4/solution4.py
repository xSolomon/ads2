''' Lesson 4 solution. '''

class aBST:
    ''' Binary search tree via array. '''
    def __init__(self, depth : int):
        depth = max(depth, 0)
        tree_size : int = pow(2, depth + 1) - 1
        self.TreeDepth : int = depth # Store depth to simplify work with tree.
        self.Tree = [None] * tree_size # Array of keys (tree modes).

    def FindKeyIndex(self, key) -> int | None:
        ''' Returns key index if it was found.
            Returns key index * (-1) if no key found, but there is valid place for it.
            If no valid space, returns None. '''
        current_node_index : int = 0
        for _ in range(self.TreeDepth + 1):
            if self.Tree[current_node_index] is None: # Reached empty node, can insert key here.
                return -current_node_index
            if self.Tree[current_node_index] == key: # Found key.
                return current_node_index
            current_node_index = current_node_index * 2 + \
                (1 if self.Tree[current_node_index] > key else 2) # Choose left or right child.
        return None

    def AddKey(self, key) -> int:
        ''' Adds key in tree and return its index, -1 if failed adding. '''
        add_key_index : int | None = self.FindKeyIndex(key)
        if add_key_index is None: # No space for key.
            return -1
        if add_key_index < 0 or (add_key_index == 0 and self.Tree[0] is None):
            add_key_index *= -1
            self.Tree[add_key_index] = key
        return add_key_index

    def lca(self) ->
        ''' '''
        return




