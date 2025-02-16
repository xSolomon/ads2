''' Lesson 5 task 3 solution. '''

from typing import Self, Callable

class BalancedBST():
    ''' AVL tree realisation. '''
    def __init__(self, depth : int):
        depth  = max(depth, 0)
        tree_size : int = pow(2, depth + 1) - 1
        self.tree : list[int] = [None] * tree_size
        self.depth : int = depth

    def _generate_bst(self, current_index : int, keys : list[int], left_border : int,
        right_border : int, depth_level : int) -> None:
        ''' Make middle element as root node, then recursively apply to
            its left and right subtrees. '''
        if right_border < left_border:
            return
        middle_element_index : int = (left_border + right_border) // 2
        self.tree[current_index] = keys[middle_element_index]
        self._generate_bst(current_index * 2  + 1, keys,
            left_border, middle_element_index - 1, depth_level + 1)
        self._generate_bst(current_index * 2 + 2, keys,
            middle_element_index + 1, right_border, depth_level + 1)

    def bst_from_sorted_array(self, depth : int, keys : list[int]) -> Self:
        ''' Given ascending sorted array, create and fill balanced BST from it. '''
        depth  = max(depth, 0)
        tree_size : int = pow(2, depth + 1) - 1
        self.tree : list[int] = [None] * tree_size
        self.depth : int = depth
        self._generate_bst(0, keys, 0, len(keys) - 1, 0)
        return self


    def inorder(self, parent_node_index : int, predicate : Callable[int, bool]) -> list[int]:
        ''' Returns all tree nodes whose matching predicate function. '''
        result : list[int] = []
        if parent_node_index >= len(self.tree):
            return result
        if self.tree[parent_node_index] is None:
            return result
        result.extend(self.inorder(parent_node_index * 2 + 1, predicate)) # left subtree
        if predicate(self.tree[parent_node_index]):
            result.append(self.tree[parent_node_index])
        result.extend(self.inorder(parent_node_index * 2 + 2, predicate)) # right subtree
        return result

    def delete_node_by_key(self, key : int) -> None:
        ''' Deletes node by key, rebalancing tree if needed.
            Does rebalancing by reforming tree from inorder traversal result. '''
        self.bst_from_sorted_array(self.depth, self.inorder(0, lambda other_key : key != other_key))
