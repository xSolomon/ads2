''' Lesson 6 task 1 solution. '''

class BSTNode:
    ''' Tree node with additional information about its depth level. '''
    def __init__(self, key : int, parent):
        self.NodeKey : int = key # Node key.
        self.Parent : BSTNode = parent # Parent node (None for root).
        self.LeftChild : BSTNode = None # Left child.
        self.RightChild : BSTNode = None # Right child.
        self.Level : int = 0 # Node depth level.
        self.HeightDifference : int = 0 # Subtree height difference (positive means left is longer).

class BalancedBST:
    ''' Represents Balanced Binary Search Tree. '''
    def __init__(self):
        self.Root : BSTNode = None # Tree root.

    def GenerateBBST(self, root_node : BSTNode, array : list, left_border : int,
        right_border : int, depth_level : int) -> BSTNode | None:
        ''' Given ascending sorted array, produce BBST from its elements. '''
        if right_border < left_border:
            return None
        middle_element_index : int = (left_border + right_border) // 2
        new_node : BSTNode = BSTNode(array[middle_element_index], root_node)
        new_node.Level = depth_level
        new_node.LeftChild = self.GenerateBBST(new_node, array, left_border,
            middle_element_index - 1, depth_level + 1)
        new_node.RightChild = self.GenerateBBST(new_node, array, middle_element_index + 1,
            right_border, depth_level + 1)
        return new_node

    def GenerateTree(self, a : list[int]) -> None:
        ''' Generates BBST from raw unsorted array. '''
        a.sort()
        self.Root = self.GenerateBBST(None, a, 0, len(a) - 1, 0)

    def CalculateTreeHeight(self, root_node : BSTNode) -> int:
        ''' Calculates tree height, writing value for each node. '''
        if root_node is None:
            return 0
        left_height : int = abs(self.CalculateTreeHeight(root_node.LeftChild))
        right_height : int = abs(self.CalculateTreeHeight(root_node.RightChild))
        root_node.HeightDifference = left_height - right_height
        return max(left_height, right_height) + 1

    def IsTreeBalanced(self, root_node : BSTNode) -> bool:
        ''' Checks whether height of subtrees of given node differs less than 2. '''
        if root_node is None:
            return True
        if not self.IsTreeBalanced(root_node.LeftChild):
            return False
        if not self.IsTreeBalanced(root_node.RightChild):
            return False
        return abs(root_node.HeightDifference) <= 1

    def IsBalanced(self, root_node : BSTNode) -> bool:
        ''' Calculates height difference between subtrees of every node,
            then checks for balance. '''
        self.CalculateTreeHeight(root_node)
        return self.IsTreeBalanced(root_node)


