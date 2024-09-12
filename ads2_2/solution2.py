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
        if self.Root is None:
            return BSTFind()
        return self._FindNodeWithKey(self.Root, key)

    def AddKeyValue(self, key, val) -> bool:
        # добавляем ключ-значение в дерево
        return False # если ключ уже есть

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

    def DeleteNodeByKey(self, key) -> bool:
        # удаляем узел по ключу
        return False # если узел не найден

    def Count(self) -> int:
        return self.NodesCount




