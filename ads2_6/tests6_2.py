''' Tests for lesson 6 task 2 solution. '''

import unittest
from solution6_1 import BSTNode, BalancedBST

class BalancedBSTTests(unittest.TestCase):
    ''' Tests for IsTreeBalanced function. '''
    def setUp(self) -> None:
        ''' Test preparations. '''
        self.tree = BalancedBST()

    def tearDown(self) -> None:
        ''' Aftertest cleanup. '''
        del self.tree

    def test_on_empty_tree(self) -> None:
        ''' Tree without nodes should count as balanced BST. '''
        self.assertTrue(self.tree.IsBST(self.tree.Root))
        self.assertTrue(self.tree.IsBalanced(None))

    def test_on_single_node_tree(self) -> None:
        ''' Tree with only root node is always balanced. '''
        self.tree.GenerateTree([5])
        self.assertTrue(self.tree.IsBST(self.tree.Root))
        self.assertTrue(self.tree.IsBalanced(self.tree.Root))

    def test_on_two_node_tree(self) -> None:
        ''' Tree must be balanced independent of child node being left or right child. '''
        root_node : BSTNode = BSTNode(10, None)
        left_child : BSTNode = BSTNode(5, root_node)
        right_child : BSTNode = BSTNode(15, root_node)
        self.assertTrue(self.tree.IsBST(root_node))

        root_node.LeftChild = left_child
        self.assertTrue(self.tree.IsBST(root_node))
        self.assertTrue(self.tree.IsBalanced(root_node))

        root_node.LeftChild = None
        root_node.RightChild = right_child
        self.assertTrue(self.tree.IsBST(root_node))
        self.assertTrue(self.tree.IsBalanced(root_node))

    def test_on_three_node_tree(self) -> None:
        ''' The only case of balanced tree is when it is root with exactly two childs. '''
        root_node : BSTNode = BSTNode(10, None)
        first_child : BSTNode = BSTNode(5, None)
        second_child : BSTNode = BSTNode(15, None)
        self.assertTrue(self.tree.IsBST(root_node))

        root_node.LeftChild = first_child
        first_child.LeftChild = second_child
        self.assertFalse(self.tree.IsBST(root_node))
        self.assertFalse(self.tree.IsBalanced(root_node))

        first_child.LeftChild = None
        first_child.RightChild = second_child
        self.assertTrue(self.tree.IsBST(root_node))
        self.assertFalse(self.tree.IsBalanced(root_node))

        first_child.RightChild = None
        root_node.RightChild = second_child
        self.assertTrue(self.tree.IsBST(root_node))
        self.assertTrue(self.tree.IsBalanced(root_node))

        root_node.LeftChild = None
        second_child.LeftChild = first_child
        self.assertTrue(self.tree.IsBST(root_node))
        self.assertFalse(self.tree.IsBalanced(root_node))

        second_child.LeftChild = None
        second_child.RightChild = first_child
        self.assertFalse(self.tree.IsBST(root_node))
        self.assertFalse(self.tree.IsBalanced(root_node))

    def unform_tree(self, tree_nodes : list[BSTNode]) -> None:
        ''' Removes all child links between given nodes. '''
        for node in tree_nodes:
            node.LeftChild = None
            node.RightChild = None

    def form_tree(self, tree_nodes : list[BSTNode],
        node_childs : list[list[BSTNode | None]]) -> None:
        ''' Makes tree by trasforming array of links to nodes into corresponding childs. '''
        for node_index, childs in enumerate(node_childs):
            tree_nodes[node_index].LeftChild = childs[0]
            tree_nodes[node_index].RightChild = childs[1]

    def test_balance_of_five_node_tree(self) -> None:
        ''' Tests all variants of five-node trees. '''
        nodes : list[BSTNode] = [BSTNode(10, None), BSTNode(5, None),
            BSTNode(15, None), BSTNode(3, None), BSTNode(7, None)]
        # Stores all possible five-node tree variants.
        # Most inner list represents two childs being None or other node.
        # Second inner list represents one of tree variants.
        tree_variants : list[list[list[BSTNode | None]]] = [
            # Root has only left child cases, no balanced variants:
            [[nodes[1], None], [nodes[2], None], [nodes[3], None], [nodes[4], None]], # 1
            [[nodes[1], None], [nodes[2], None], [nodes[3], None], [None, nodes[4]]], # 2
            [[nodes[1], None], [nodes[2], None], [None, nodes[3]], [nodes[4], None]], # 3
            [[nodes[1], None], [nodes[2], None], [None, nodes[3]], [None, nodes[4]]], # 4
            [[nodes[1], None], [nodes[2], nodes[3]], [nodes[4], None], [None, None]], # 5
            [[nodes[1], None], [nodes[2], nodes[3]], [None, nodes[4]], [None, None]], # 6
            [[nodes[1], None], [nodes[2], nodes[3]], [None, None], [nodes[4], None]], # 7
            [[nodes[1], None], [nodes[2], nodes[3]], [None, None], [None, nodes[4]]], # 8
            [[nodes[1], None], [None, nodes[2]], [nodes[3], None], [nodes[4], None]], # 9
            [[nodes[1], None], [None, nodes[2]], [nodes[3], None], [None, nodes[4]]], # 10
            [[nodes[1], None], [None, nodes[2]], [None, nodes[3]], [nodes[4], None]], # 11
            [[nodes[1], None], [None, nodes[2]], [None, nodes[3]], [None, nodes[4]]], # 12
            # Root right subtree contains only one node, variant 15 is balanced:
            [[nodes[1], nodes[2]], [nodes[3], None], [None, None], [nodes[4], None]], # 13
            [[nodes[1], nodes[2]], [nodes[3], None], [None, None], [None, nodes[4]]], # 14
            [[nodes[1], nodes[2]], [nodes[3], nodes[4]], [None, None], [None, None]], # 15
            [[nodes[1], nodes[2]], [None, nodes[3]], [None, None], [nodes[4], None]], # 16
            [[nodes[1], nodes[2]], [None, nodes[3]], [None, None], [None, nodes[4]]], # 17
            # Root left and right subtrees contains 2 nodes each, all variants are balanced:
            [[nodes[1], nodes[2]], [nodes[3], None], [nodes[4], None], [None, None]], # 18
            [[nodes[1], nodes[2]], [nodes[3], None], [None, nodes[4]], [None, None]], # 19
            [[nodes[1], nodes[2]], [None, nodes[3]], [nodes[4], None], [None, None]], # 20
            [[nodes[1], nodes[2]], [None, nodes[3]], [None, nodes[4]], [None, None]], # 21
            # Root left subtree sontains only one node, variant 24 is balanced:
            [[nodes[1], nodes[2]], [None, None], [nodes[3], None], [nodes[4], None]], # 22
            [[nodes[1], nodes[2]], [None, None], [nodes[3], None], [None, nodes[4]]], # 23
            [[nodes[1], nodes[2]], [None, None], [nodes[3], nodes[4]], [None, None]], # 24
            [[nodes[1], nodes[2]], [None, None], [None, nodes[3]], [nodes[4], None]], # 25
            [[nodes[1], nodes[2]], [None, None], [None, nodes[3]], [None, nodes[4]]], # 26
            # Root has only right child cases, no balanced variants:
            [[None, nodes[1]], [nodes[2], None], [nodes[3], None], [nodes[4], None]], # 27
            [[None, nodes[1]], [nodes[2], None], [nodes[3], None], [None, nodes[4]]], # 28
            [[None, nodes[1]], [nodes[2], None], [None, nodes[3]], [nodes[4], None]], # 29
            [[None, nodes[1]], [nodes[2], None], [None, nodes[3]], [None, nodes[4]]], # 30
            [[None, nodes[1]], [nodes[2], nodes[3]], [nodes[4], None], [None, None]], # 31
            [[None, nodes[1]], [nodes[2], nodes[3]], [None, nodes[4]], [None, None]], # 32
            [[None, nodes[1]], [nodes[2], nodes[3]], [None, None], [nodes[4], None]], # 33
            [[None, nodes[1]], [nodes[2], nodes[3]], [None, None], [None, nodes[4]]], # 34
            [[None, nodes[1]], [None, nodes[2]], [nodes[3], None], [nodes[4], None]], # 35
            [[None, nodes[1]], [None, nodes[2]], [nodes[3], None], [None, nodes[4]]], # 36
            [[None, nodes[1]], [None, nodes[2]], [None, nodes[3]], [nodes[4], None]], # 37
            [[None, nodes[1]], [None, nodes[2]], [None, nodes[3]], [None, nodes[4]]]] # 38

        balanced_trees : list[int] = [15, 18, 19, 20, 21, 24]
        for i, tree_variant in enumerate(tree_variants):
            with self.subTest(test_number = i + 1):
                self.form_tree(nodes, tree_variant)
                if i + 1 in balanced_trees:
                    self.assertTrue(self.tree.IsBalanced(nodes[0]))
                    continue
                self.assertFalse(self.tree.IsBalanced(nodes[0]))
                self.unform_tree(nodes)

    def test_on_predefined_fifteen_nodes_tree(self) -> None:
        ''' Forms full tree of 3 depth level. Then, deletes root left subtree.
            Tree must be unbalanced. '''
        root_node_50 : BSTNode = BSTNode(50, None)
        node_25 : BSTNode = BSTNode(25, None)
        node_75 : BSTNode = BSTNode(75, None)
        node_37 : BSTNode = BSTNode(37, None)
        node_31 : BSTNode = BSTNode(31, None)
        node_43 : BSTNode = BSTNode(43, None)
        node_62 : BSTNode = BSTNode(62, None)
        node_84 : BSTNode = BSTNode(84, None)
        node_55 : BSTNode = BSTNode(55, None)
        node_92 : BSTNode = BSTNode(92, None)

        root_node_50.LeftChild = node_25
        node_25.RightChild = node_37
        node_37.LeftChild = node_31
        node_37.RightChild = node_43
        root_node_50.RightChild = node_75
        node_75.LeftChild = node_62
        node_62.LeftChild = node_55
        node_75.RightChild = node_84
        node_84.RightChild = node_92

        self.assertFalse(self.tree.IsBalanced(root_node_50))
        self.assertTrue(self.tree.IsBST(root_node_50))
        root_node_50.LeftChild = None
        self.assertFalse(self.tree.IsBalanced(root_node_50))
        self.assertTrue(self.tree.IsBST(root_node_50))



unittest.main()
