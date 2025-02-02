''' Solution for lesson 2. '''

from typing import Tuple

class BSTNode:
    ''' Value can be distinct with key if needed. '''
    def __init__(self, key, val, parent) -> None:
        self.NodeKey = key # Node key.
        self.NodeValue = val # Node value.
        self.Parent : BSTNode = parent # Parent (None for root).
        self.LeftChild : BSTNode = None # Left child.
        self.RightChild : BSTNode = None # Right child.

class BSTFind:
    ''' Holds results of BST FindNodeByKey function. '''    
    def __init__(self) -> None:
        self.Node : BSTNode = None # Can be None if tree is empty.
        self.NodeHasKey : bool = False # True if node found, false if it is parent.
        self.ToLeft : bool = False # True if new node must be left child.

class BST:
    ''' Binary search tree. '''
    def __init__(self, node : BSTNode) -> None:
        self.Root = node # Tree root, can be None.
        self.NodesCount : int = 0 if self.Root is None else 1 # Total nodes in the tree.

    def _IsLeaf(self, Node : BSTNode) -> bool:
        ''' Checks whether provided node has any childs. '''
        return Node.LeftChild is None and Node.RightChild is None

    def _FindNodeWithKey(self, FromNode : BSTFind, key) -> BSTFind:
        ''' Finds if there is node with matching key,
            or place where it should be. '''
        if FromNode.NodeKey > key and FromNode.LeftChild is not None:
            return self._FindNodeWithKey(FromNode.LeftChild, key)
        if FromNode.NodeKey < key and FromNode.RightChild is not None:
            return self._FindNodeWithKey(FromNode.RightChild, key)

        result : BSTFind = BSTFind()
        result.Node = FromNode
        if FromNode.NodeKey == key:
            result.NodeHasKey = True
            return result
        result.NodeHasKey = False
        result.ToLeft = True if FromNode.NodeKey > key else False
        return result

    def FindNodeByKey(self, key) -> BSTFind:
        ''' Try to find node by key and return with additional information about it. '''
        if self.Root is None:
            return BSTFind()
        return self._FindNodeWithKey(self.Root, key)

    def AddKeyValue(self, key, val) -> bool:
        ''' Try to add new node in the tree.
            Adds nothing and returns False if key is already presented. '''
        NodeParent : BSTFind = self.FindNodeByKey(key)
        if NodeParent.NodeHasKey:
            return False
        self.NodesCount += 1
        if NodeParent.Node is None:
            self.Root = BSTNode(key, val, None)
            return True
        new_node : BSTNode = BSTNode(key, val, NodeParent.Node)
        if NodeParent.ToLeft:
            NodeParent.Node.LeftChild = new_node
            return True
        NodeParent.Node.RightChild = new_node
        return True

    def _FinMin(self, FromNode : BSTNode) -> BSTNode:
        ''' Find minimum value in the tree. '''
        if FromNode.LeftChild is None:
            return FromNode
        return self._FinMin(FromNode.LeftChild)

    def _FinMax(self, FromNode : BSTNode) -> BSTNode:
        ''' Find maximum value in the tree. '''
        if FromNode.RightChild is None:
            return FromNode
        return self._FinMax(FromNode.RightChild)

    def FinMinMax(self, FromNode : BSTNode, FindMax) -> BSTNode:
        ''' Find minimum or maximum value in the tree. '''
        if FromNode is None:
            return None
        return self._FinMax(FromNode) if FindMax else self._FinMin(FromNode)

    def _FindSuccessor(self, CurNode : BSTNode) -> BSTNode:
        ''' Find node that should replace the node we deleting. '''
        if CurNode.LeftChild is None:
            return CurNode
        return self._FindSuccessor(CurNode.LeftChild)

    def _DeleteNode(self, NodeToDelete : BSTNode) -> bool:
        ''' Delete node and replace it with correct successor. '''
        if NodeToDelete is None: # Nothing to delete.
            return False
        # Cases where we delete leaf node:
        if self.Count() == 0: # Deleting last node.
            self.Root = None
            return True
        if self._IsLeaf(NodeToDelete) and NodeToDelete is NodeToDelete.Parent.LeftChild:
            # Deleting leaf node that is LEFT child of its parent.
            NodeToDelete.Parent.LeftChild = None
            return True
        if self._IsLeaf(NodeToDelete) and NodeToDelete is NodeToDelete.Parent.RightChild:
            # Deleting leaf node that is RIGHT child of its parent.
            NodeToDelete.Parent.RightChild = None
            return True
        # Cases where we delete node with only LEFT child:
        if NodeToDelete is self.Root and NodeToDelete.RightChild is None:
            # Deleting root with only left child.
            NodeToDelete.LeftChild.Parent = None
            self.Root = self.Root.LeftChild
            return True
        if NodeToDelete.RightChild is None and NodeToDelete is NodeToDelete.Parent.LeftChild:
            # Deleting parent's LEFT node with only left child.
            NodeToDelete.Parent.LeftChild = NodeToDelete.LeftChild
            NodeToDelete.LeftChild.Parent = NodeToDelete.Parent
            return True
        if NodeToDelete.RightChild is None and NodeToDelete is NodeToDelete.Parent.RightChild:
            # Deleting parent's RIGHT node with only left child.
            NodeToDelete.Parent.RightChild = NodeToDelete.LeftChild
            NodeToDelete.LeftChild.Parent = NodeToDelete.Parent
            return True
        # Node has right child, find successor in the right subtree,
        # copy values and delete successor node instead.
        successor : BSTNode = self._FindSuccessor(NodeToDelete.RightChild)
        NodeToDelete.NodeKey = successor.NodeKey
        NodeToDelete.NodeValue = successor.NodeValue
        return self._DeleteNode(successor)

    def DeleteNodeByKey(self, key) -> bool:
        ''' Deletes node by key, keeping tree balanced. '''
        node_to_delete : BSTFind = self.FindNodeByKey(key)
        if node_to_delete.Node is None or not node_to_delete.NodeHasKey: # Nothing to delete.
            return False
        self.NodesCount -= 1
        return self._DeleteNode(node_to_delete.Node)

    def Count(self) -> int:
        ''' Returns current nodes number in the tree. '''
        return self.NodesCount

    def _all_paths_with_length(self, from_node : BSTNode, path_length : int,
        current_path : list[BSTNode], found_paths : list[list[BSTNode]]) -> list[list[BSTNode]]:
        ''' Finds all paths from given node to leaves with given length. '''
        if from_node is None:
            return found_paths
        current_path.append(from_node)
        if path_length == 0 and self._IsLeaf(from_node):
            found_paths.append(current_path.copy())
            current_path.pop()
            return found_paths
        found_paths.extend(self._all_paths_with_length(
            from_node.LeftChild, path_length - 1, current_path, []))
        found_paths.extend(self._all_paths_with_length(
            from_node.RightChild, path_length - 1, current_path, []))
        current_path.pop()
        return found_paths

    def root_to_leaf_paths(self, path_length : int) -> list[list[BSTNode]]:
        ''' Finds all paths from root to leaves which have given length. '''
        if path_length < 0:
            return []
        return self._all_paths_with_length(self.Root, path_length - 1, [], [])

    def _all_paths_with_max_sum(self, from_node: BSTNode, highest_sum : int,
        current_path : list[BSTNode]) \
            -> Tuple[int, list[list[BSTNode]]]:
        ''' Uses dfs method. '''
        if from_node is None:
            return (highest_sum, current_path.copy())
        current_path.append(from_node)
        if self._IsLeaf(from_node):
            result : Tuple(int, list[list[BSTNode]]) = (highest_sum +from_node.NodeValue, [current_path.copy()])
            current_path.pop()
            return result
        left_subtree_paths : Tuple[int, list[list[BSTNode]]] = self._all_paths_with_max_sum(
            from_node.LeftChild, highest_sum + from_node.NodeValue, current_path)
        right_subtree_paths : Tuple[int, list[list[BSTNode]]] = self._all_paths_with_max_sum(
            from_node.RightChild, highest_sum + from_node.NodeValue, current_path)
        current_path.pop()
        if left_subtree_paths[0] == right_subtree_paths[0]:
            left_subtree_paths[1].extend(right_subtree_paths[1])
        return left_subtree_paths if left_subtree_paths[0] >= right_subtree_paths[0] \
            else right_subtree_paths

    def paths_with_max_sum(self) -> Tuple[int, list[list[BSTNode]]]:
        ''' Finds all paths from root to leaf with maximum sum. '''
        if not self.Root:
            return (None, [])
        return self._all_paths_with_max_sum(self.Root, 0, [])






