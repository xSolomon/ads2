''' Solution for lesson 2. '''

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
    ''' Binary sorted tree. '''
    def __init__(self, node : BSTNode) -> None:
        self.Root = node # Tree root, can be None.
        self.NodesCount : int = 0 if self.Root is None else 1 # Total nodes in the tree.
    
    def _FindNodeWithKey(self, FromNode : BSTFind, key) -> BSTFind:
        ''' Finds if there is node with matching key,
            or place where it should be. '''
        if FromNode.NodeKey < key and FromNode.LeftChild is not None:
            return _FindNodeWithKey(FromNode.LeftChild, key)
        if FromNode.NodeKey > key and FromNode.RightChild is not None:
            return _FindNodeWithKey(FromNode.RightChild, key)

        result : BSTFind = BSTFind()
        result.Node = FromNode
        if FromNode.NodeKey == key:
            result.NodeHasKey = True
            return result
        result.NodeHasKey = False
        result.ToLeft = True if FromNode.NodeKey < key else False
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
        NewNode : BSTNode = BSTNode(key, val, result.Node)
        if NodeParent.ToLeft:
            NodeParent.LeftChild = NewNode
            return True
        NodeParent.RightChild = NewNode
        return True

    def _FinMin(self, FromNode : BSTNode) -> BSTNode:
        ''' Find minimum value in the tree. '''
        if FromNode.LeftChild is None:
            return FromNode
        return FinMin(FromNode.LeftChild)

    def _FinMax(self, FromNode : BSTNode) -> BSTNode:
        ''' Find maximum value in the tree. '''
        if FromNode.RightChild is None:
            return FromNode
        return FinMin(FromNode.RightChild)

    def FinMinMax(self, FromNode : BSTNode, FindMax) -> BSTNode:
        ''' Find minimum or maximum value in the tree. '''
        if FromNode is None:
            return None
        return self._FinMax if FindMax else self._FinMin

    def _FindSuccessor(self, CurNode) -> BSTNode:
        if CurNode.LeftChild is None and CurNode.RightChild is None:
            return ForNode
        if CurNode.LeftChild is None:
            return CurNode.RightChild
        return _FindSuccessor(CurNode.LeftChild)

    def _DeleteNode(self, NodeToDelete : BSTNode) -> bool:
        if NodeToDelete is None: # Nothing to delete.
            return False
        if NodeToDelete is self.Root and NodeToDelete.RightChild is None:
            # Deleting root with only left child.
            NodeToDelete.LeftChild.Parent = None
            self.Root = self.Root.LeftChild
            return True
        if NodeToDelete.LeftChild is None and NodeToDelete.RightChild is None and \
            NodeToDelete is NodeToDelete.Parent.LeftChild: # Deleting left leaf child.
            NodeToDelete.Parent.LeftChild = None
            return True
        if NodeToDelete.LeftChild is None and NodeToDelete.RightChild is None and \
            NodeToDelete is NodeToDelete.Parent.LeftChild: # Deleting right leaf child.
            NodeToDelete.Parent.RightChild = None
            return True
        if NodeToDelete.RightChild is None and NodeToDelete is NodeToDelete.Parent.LeftChild:
            # Deleting left node with only left child.
            NodeToDelete.Parent.LeftChild = NodeToDelete.LeftChild
            NodeToDelete.LeftChild.Parent = NodeToDelete.Parent
            return True
        if NodeToDelete.RightChild is None and NodeToDelete is NodeToDelete.Parent.RightChild:
            # Deleting right node with only left child.
            NodeToDelete.Parent.RightChild = NodeToDelete.RightChild
            NodeToDelete.LeftChild.Parent = NodeToDelete.Parent
            return True
        Successor : BSTNode = self._FindSuccessor(NodeToDelete.RightChild)
        NodeToDelete.key = Successor.NodeKey
        NodeToDelete.value = Successor.NodeValue
        return self._DeleteNode(Successor)

    def DeleteNodeByKey(self, key) -> bool:
        ''' Deletes node by key, keeping tree balanced. '''
        NodeToDelete : BSTFind = self.FindNodeByKey(key)
        if NodeToDelete.Node is None or not NodeToDelete.NodeHasKey: # Nothing to delete.
            return False
        self.NodesCount -= 1
        if self.NodesCount == 0: # Deleting last node in the tree.
            self.Root = None
            return True
        return self._DeleteNode(NodeToDelete.Node)

    def Count(self) -> int:
        return self.NodesCount




