''' Lesson 3 task 3 solution. '''

from solution3 import BST, BSTNode

def inverse_tree(cur_node : BSTNode) -> None:
    ''' Uses pre-order tree traversal. '''
    cur_node.LeftChild, cur_node.RightChild = cur_node.RightChild, cur_node.LeftChild
    if cur_node.LeftChild is not None:
        inverse_tree(cur_node.LeftChild)
    if cur_node.RightChild is not None:
        inverse_tree(cur_node.RightChild)

def inverseBST(tree : BST) -> None:
    ''' Inverse tree so that all values greater will be in the left subtree. '''
    if tree.Root is None:
        return
    BST(inverse_tree(tree.Root))
