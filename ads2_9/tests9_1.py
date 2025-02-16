''' Tests for lesson 9 solution. '''

import unittest
from solution9_1 import SimpleTree, SimpleTreeNode

class EvenTreesTests(unittest.TestCase):
    ''' Tests for EvenTrees, total_even_subtrees functions. '''
    def test_even_trees_on_empty_tree(self) -> None:
        ''' Must return empty list. '''
        tree : SimpleTree = SimpleTree(None)
        self.assertEqual(tree.EvenTrees(), [])

    def test_even_trees_on_one_node_tree(self) -> None:
        ''' Must return empty list. '''
        tree : SimpleTree = SimpleTree(SimpleTreeNode(252, None))
        self.assertEqual(tree.EvenTrees(), [])

    def test_even_trees_on_two_node_tree(self) -> None:
        ''' Must return empty list. '''
        root_node : SimpleTreeNode = SimpleTreeNode(456, None)
        tree : SimpleTree = SimpleTree(root_node)
        tree.AddChild(root_node, SimpleTreeNode(123, root_node))
        self.assertEqual(tree.EvenTrees(), [])

    def test_even_tree_on_four_node_tree(self) -> None:
        ''' Must return edge between second and third node. '''
        root_node : SimpleTreeNode = SimpleTreeNode(1, None)
        second_node : SimpleTreeNode = SimpleTreeNode(2, root_node)
        third_node : SimpleTreeNode = SimpleTreeNode(3, second_node)
        fourth_node : SimpleTreeNode = SimpleTreeNode(4, third_node)
        tree : SimpleTree = SimpleTree(root_node)
        tree.AddChild(root_node, second_node)
        tree.AddChild(second_node, third_node)
        tree.AddChild(third_node, fourth_node)
        self.assertEqual(tree.EvenTrees(), [second_node, third_node])

    def test_even_tree_on_ten_node_tree(self) ->  None:
        ''' Root node have 2 even and 1 odd subtree.
            Must return edges between root node and it's
            second and third childs. '''
        root_node : SimpleTreeNode = SimpleTreeNode(1, None)
        second_node : SimpleTreeNode = SimpleTreeNode(2, root_node)
        third_node : SimpleTreeNode = SimpleTreeNode(3, root_node)
        fourth_node : SimpleTreeNode = SimpleTreeNode(4, third_node)
        fifth_node : SimpleTreeNode = SimpleTreeNode(5, second_node)
        sixth_node : SimpleTreeNode = SimpleTreeNode(6, root_node)
        seventh_node : SimpleTreeNode = SimpleTreeNode(7, second_node)
        eighth_node : SimpleTreeNode = SimpleTreeNode(8, sixth_node)
        ninth_node : SimpleTreeNode = SimpleTreeNode(9, eighth_node)
        tenth_node : SimpleTreeNode = SimpleTreeNode(10, eighth_node)
        tree : SimpleTree = SimpleTree(root_node)
        tree.AddChild(None, root_node)
        tree.AddChild(root_node, second_node)
        tree.AddChild(root_node, third_node)
        tree.AddChild(third_node, fourth_node)
        tree.AddChild(second_node, fifth_node)
        tree.AddChild(root_node, sixth_node)
        tree.AddChild(second_node, seventh_node)
        tree.AddChild(sixth_node, eighth_node)
        tree.AddChild(eighth_node, ninth_node)
        tree.AddChild(eighth_node, tenth_node)
        self.assertEqual(tree.EvenTrees(), [root_node, third_node, root_node, sixth_node])

unittest.main()
