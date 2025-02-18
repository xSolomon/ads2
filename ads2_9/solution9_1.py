''' Lesson 9 task 1 solution. '''

from typing import Tuple

class SimpleTreeNode:
    ''' New child node will be the most right child. '''
    def __init__(self, val, parent) -> None:
        self.NodeValue = val # Node value.
        self.Parent : SimpleTreeNode = parent # Parent (None for root node).
        self.Children : list[SimpleTreeNode] = [] # List of child nodes.

class SimpleTree:
    ''' Holds tree root, also stores nodes count. '''
    def __init__(self, root : SimpleTreeNode) -> None:
        self.Root : SimpleTreeNode = root # Root, can be None.
        self.NodesCount : int = 0 if self.Root is None else 1 # Total nodes in the tree.

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
        if OriginalNode is None:
            return
        if OriginalNode is NewParent:
            return
        OriginalNode.Parent.Children.remove(OriginalNode)
        self.NodesCount -= 1
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

    def _FormEdgesToCut(self, ParentNode : SimpleTreeNode, IsEvenTree : bool,
        VertecesBeingCut : list[SimpleTreeNode]) -> bool:
        ''' Recursively checks if subtree contains an even number of nodes
            (and, thus, vertex can be cut). '''
        for child in ParentNode.Children:
            if self._FormEdgesToCut(child, False, VertecesBeingCut):
                VertecesBeingCut.append(ParentNode)
                VertecesBeingCut.append(child)
                continue
            IsEvenTree = not IsEvenTree
        return IsEvenTree

    def EvenTrees(self) -> list[SimpleTreeNode]:
        ''' Returns list of nodes for which vertex must be cut
            to form maximum number of even trees. '''
        if self.Root is None:
            return []
        result : list[SimpleTreeNode] = []
        self._FormEdgesToCut(self.Root, False, result)
        return result

    def _count_even_subtrees(self, from_node : SimpleTreeNode) -> Tuple[int, bool]:
        ''' Recursively counts even subtrees for every child.
            Second return value indicates whether subtree is even. '''
        even_subtrees_counter : int = 0
        is_even : bool = False
        for child in from_node.Children:
            child_results : Tuple[int, bool] = self._count_even_subtrees(child)
            even_subtrees_counter += child_results[0]
            is_even = is_even == child_results[1]
        return (even_subtrees_counter + (1 if is_even else 0), is_even)

    def total_even_subtrees(self, root_node : SimpleTreeNode) -> int:
        ''' Returns total number of even subtress of given node. '''
        if root_node is None:
            return 0
        result : Tuple(int, bool) = self._count_even_subtrees(root_node)
        # Whole tree is not a subtree, so substract if tree is even.
        return result[0] - 1 if result[1] else result[0]
