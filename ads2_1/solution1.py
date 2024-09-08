''' Lesson 1 solution (simple tree). '''

class SimpleTreeNode:
    ''' New child node will be the most right child. '''
    def __init__(self, val, parent) -> None:
        self.NodeValue = val # Node value.
        self.Parent = parent # Parent (None for root node).
        self.Children : list[SimpleTreeNode] = [] # List of child nodes.

class SimpleTree:
    ''' Holds tree root, also stores nodes count. '''
    def __init__(self, root : SimpleTreeNode) -> None:
        self.Root = root # корень, может быть None
        self.NodesCount : int = 0 # Total nodes in the tree

    def AddChild(self, ParentNode : SimpleTreeNode, NewChild : SimpleTreeNode) -> None:
        ''' Adds new node as the most right child. '''
        if NewChild is None:
            return

        self.NodesCount += 1
        if ParentNode is None and self.Root is None:
            self.Root = NewChild
            return
        if ParentNode is None:
            NewChild.Children.append(self.Root)
            self.Root.Parent = NewChild
            self.Root = NewChild
            return

        NewChild.Parent = ParentNode
        ParentNode.Children.append(NewChild)

    def _DeleteSubtree(self, SubtreeRoot : SimpleTreeNode) -> None:
        ''' Recursively deletes tree with present root. '''
        for child in SubtreeRoot.Children:
            self._DeleteSubtree(child)
        SubtreeRoot.Children = []
        del SubtreeRoot
        self.NodesCount -= 1

    def DeleteNode(self, NodeToDelete : SimpleTreeNode) -> None:
        ''' Deletes subtree with present node as its root. '''
        if NodeToDelete is None:
            return
        if self.Root == NodeToDelete:
            self.Root = None
        if NodeToDelete.Parent is not None:
            NodeToDelete.Parent.Children.remove(NodeToDelete)
        self._DeleteSubtree(NodeToDelete)

    def _GetNodes(self, ParentNode : SimpleTreeNode,
        ResultNodes : list[SimpleTreeNode]) -> list[SimpleTreeNode]:
        ''' Recursively get all tree nodes. '''
        ResultNodes.append(ParentNode)
        for child in ParentNode.Children:
            self._GetNodes(child, ResultNodes)
        return ResultNodes

    def GetAllNodes(self) -> list[SimpleTreeNode]:
        ''' Get all nodes in the tree in root-first order. '''
        if self.Root is None:
            return []
        return self._GetNodes(self.Root, [])

    def _FindNodes(self, val, ParentNode : SimpleTreeNode,
        ResultNodes : list[SimpleTreeNode]) -> list[SimpleTreeNode]:
        ''' Recursively finds nodes that have present value. '''
        if ParentNode.NodeValue == val:
            ResultNodes.append(ParentNode)
        for child in ParentNode.Children:
            self._FindNodes(val, child, ResultNodes)
        return ResultNodes

    def FindNodesByValue(self, val) -> list[SimpleTreeNode]:
        ''' Find all nodes with given value. '''
        if self.Root is None:
            return []
        return self._FindNodes(val, self.Root, [])

    def MoveNode(self, OriginalNode : SimpleTreeNode, NewParent : SimpleTreeNode):
        if OriginalNode is None or NewParent is None:
            return
        OriginalNode.Parent.Children.remove(OriginalNode)
        self.AddChild(NewParent, OriginalNode)

    def Count(self) -> int:
        ''' Returns nodes count in the tree. '''
        return self.NodesCount

    def _GetLeafCount(self, ParentNode : SimpleTreeNode, LeavesCount : int) -> int:
        ''' Recursively counts number of leaves. '''
        for child in ParentNode.Children:
            LeavesCount += self._GetLeafCount(child, 0)
        if len(ParentNode.Children) == 0:
            LeavesCount += 1
        return LeavesCount

    def LeafCount(self) -> int:
        ''' Returns leaves count in the tree. '''
        if self.Root is None:
            return 0
        return self._GetLeafCount(self.Root, 0)

    def _WriteNodeLevels(self, ParentNode : SimpleTreeNode, Level : int) -> None:
        ''' Recursively replaces node value with their level. '''
        ParentNode.NodeValue = Level
        for child in ParentNode.Children:
            self._WriteNodeLevels(child, Level  + 1)

    def WriteLevelInNodeVal(self) -> None:
        ''' Sets each node value equal to its level in the tree. '''
        if self.Root is None:
            return
        self._WriteNodeLevels(self.Root, 0)





