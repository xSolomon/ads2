''' Lesson 6 task 1 solution. '''

class BSTNode:
    ''' Tree node with additional information about its depth level. '''
    def __init__(self, key, parent):
        self.NodeKey = key # Node key.
        self.Parent : BSTNode = parent # Parent node (None for root).
        self.LeftChild : BSTNode = None # Left child.
        self.RightChild : BSTNode = None # Right child.
        self.Level : int = 0 # Node depth level.

class BalancedBST:
    ''' Represents Balanced Binary Search Tree. '''
    def __init__(self):
        self.Root : BSTNode = None # Tree root.

    def GenerateBBST(self, root_node : BSTNode, array : list, left_border : int,
        right_border : int, depth_level : int) -> BSTNode:
        ''' Given ascending sorted array, produce BBST from its elements. '''
        middle_element_index : int = (left_border + right_border) // 2
        new_node : BSTNode = BSTNode(array[middle_element_index], root_node)
        new_node.Level = depth_level
        new_node.LeftChild = self.GenerateBBST(new_node, array, left_border,
            middle_element_index - 1, depth_level + 1)
        new_node.RightChild = self.GenerateBBST(new_node, array, middle_element_index + 1,
            right_border, depth_level + 1)
        return new_node

    def GenerateTree(self, a : list) -> None:
        ''' Generates BBST from raw unsorted array. '''
        a.sort()
        self.Root = self.GenerateBBST(None, a, 0, len(a) - 1, 0)




