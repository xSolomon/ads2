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

unittest.main()
