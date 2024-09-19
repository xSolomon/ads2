''' Solution for lesson 3. '''

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

    def _BreadthAllNodes(self, ResultNodes : list[BSTNode],
        CurrentLevelNodes : list[BSTNode]) -> tuple[BSTNode]:
        ''' Breadth traversal. '''
        nodes_in_next_level : list[BSTNode] = []
        for Node in CurrentLevelNodes:
            if Node.LeftChild is not None:
                nodes_in_next_level.append(Node.LeftChild)
            if Node.RightChild is not None:
                nodes_in_next_level.append(Node.RightChild)
            ResultNodes.append(Node)
        if len(nodes_in_next_level) > 0:
            self._BreadthAllNodes(ResultNodes, nodes_in_next_level)
        if CurrentLevelNodes[0] is self.Root:
            return tuple(ResultNodes)

    def WideAllNodes(self) -> tuple[BSTNode]:
        ''' Forms list of all tree nodes using breadth-first search. '''
        if self.Root is None:
            return tuple()
        return self._BreadthAllNodes([], [self.Root])

    def _InOrder(self, CurNode : BSTNode, ResultNodes : list[BSTNode]) -> tuple[BSTNode]:
        ''' In-order version of depth traversal. '''
        if CurNode.LeftChild is not None:
            self._InOrder(CurNode.LeftChild, ResultNodes)
        ResultNodes.append(CurNode)
        if CurNode.RightChild is not None:
            self._InOrder(CurNode.RightChild, ResultNodes)
        if CurNode is self.Root:
            return tuple(ResultNodes)

    def _PostOrder(self, CurNode : BSTNode, ResultNodes : list[BSTNode]) -> tuple[BSTNode]:
        ''' Post-order version of depth traversal. '''
        if CurNode.LeftChild is not None:
            self._PostOrder(CurNode.LeftChild, ResultNodes)
        if CurNode.RightChild is not None:
            self._PostOrder(CurNode.RightChild, ResultNodes)
        ResultNodes.append(CurNode)
        if CurNode is self.Root:
            return tuple(ResultNodes)

    def _PreOrder(self, CurNode : BSTNode, ResultNodes : list[BSTNode]) -> tuple[BSTNode]:
        ''' Pre-order version of depth traversal. '''
        ResultNodes.append(CurNode)
        if CurNode.LeftChild is not None:
            self._PreOrder(CurNode.LeftChild, ResultNodes)
        if CurNode.RightChild is not None:
            self._PreOrder(CurNode.RightChild, ResultNodes)
        if CurNode is self.Root:
            return tuple(ResultNodes)

    def DeepAllNodes(self, search_order : int) -> tuple[BSTNode]:
        ''' Forms list of all tree nodes using deep-first search.
            Second parameter defines exact order, where:
            0 - in order,
            1 - post-order,
            2 - pre-order. '''
        if self.Root is None or search_order not in [0, 1, 2]:
            return tuple()
        traversal_version : dict = {
            0: self._InOrder,
            1: self._PostOrder,
            2: self._PreOrder
        }
        return traversal_version[search_order](self.Root, [])








