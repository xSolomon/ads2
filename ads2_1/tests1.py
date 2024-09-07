''' Tests for lesson 1 Simple Tree methods. '''

import unittest
from random import randint, sample
from parametrize import parametrize
from solution1 import SimpleTreeNode, SimpleTree

class SimpleTreeTests(unittest.TestCase):
    ''' Tests for SimpleTree AddChild(), DeleteNode(), GetAllNodes(),
        FindNodesByValue(), MoveNode(), Count(), LeafCount(), WriteLevelInNodeVal() functions. '''
    def setUp(self) -> None:
        ''' Test preparations. '''
        self.tree : SimpleTree = SimpleTree(None)

    def tearDown(self) -> None:
        ''' Aftertest cleanup. '''
        self.tree.DeleteNode(self.tree.Root)
        self.assertEqual(self.tree.Count(), 0)
        self.assertIsNone(self.tree.Root)

    def test_count_on_empty_tree(self) -> None:
        ''' Expected 0. '''
        self.assertEqual(self.tree.Count(), 0)

    def test_leaf_count_on_empty_tree(self) -> None:
        ''' Expected 0. '''
        self.assertEqual(self.tree.LeafCount(), 0)

    def test_find_on_empty_tree(self) -> None:
        ''' Expected empty list for each of the subtests. '''
        test_on : list = [1, 3, -1521541141, 0, 'qwerty', True, None]
        for _, item in enumerate(test_on):
            with self.subTest():
                self.assertEqual(self.tree.FindNodesByValue(item), [])

    def test_get_nodes_on_empty_tree(self) -> None:
        ''' Expected empty list. '''
        self.assertEqual(self.tree.GetAllNodes(), [])

    def test_inserting_none_node(self) -> None:
        ''' Expected nothing to be changed. '''
        self.tree.AddChild(None, None)
        self.assertEqual(self.tree.Count(), 0)
        self.assertIsNone(self.tree.Root)

    def test_inserting_in_empty_tree(self) -> None:
        ''' Expected nodes count = 1 and inserted node to be new root. '''
        test_node : SimpleTreeNode = SimpleTreeNode(123, None)
        self.tree.AddChild(None, test_node)
        self.assertEqual(self.tree.Count(), 1)
        self.assertEqual(self.tree.Root, test_node)

    def test_leaf_count_on_single_node_tree(self) -> None:
        ''' Expected leaf count = 1. '''
        test_node : SimpleTreeNode = SimpleTreeNode(123, None)
        self.tree.AddChild(None, test_node)
        self.assertEqual(self.tree.LeafCount(), 1)

    def test_get_nodes_on_single_node_tree(self) -> None:
        ''' Expected list with exactly one node (root) '''
        test_node : SimpleTreeNode = SimpleTreeNode(123, None)
        self.tree.AddChild(None, test_node)
        self.assertEqual(self.tree.GetAllNodes()[0], test_node)

    def test_find_nodes_on_single_node_tree(self) -> None:
        ''' Expected empty list for each of wrong values.
            Expected exactly root node on right value. '''
        test_node : SimpleTreeNode = SimpleTreeNode(123, None)
        self.tree.AddChild(None, test_node)
        test_on : list = [1, 3, -1521541141, 0, 'qwerty', True, None]
        for _, item in enumerate(test_on):
            with self.subTest():
                self.assertEqual(self.tree.FindNodesByValue(item), [])
        self.assertEqual(self.tree.FindNodesByValue(123), [test_node])

    def test_insert_in_root_two_times(self) -> None:
        ''' Expected node count = 2, leaf count = 1, root to be second inserted node. '''
        first_node : SimpleTreeNode = SimpleTreeNode(123, None)
        second_node : SimpleTreeNode = SimpleTreeNode(456, None)
        self.tree.AddChild(None, first_node)
        self.tree.AddChild(None, second_node)
        self.assertEqual(self.tree.Count(), 2)
        self.assertEqual(self.tree.LeafCount(), 1)
        self.assertEqual(self.tree.Root, second_node)

    def test_insert_in_root_then_under_root(self) -> None:
        ''' Expected node count = 2, leaf count = 1, root to be first inserted node. '''
        first_node : SimpleTreeNode = SimpleTreeNode(123, None)
        second_node : SimpleTreeNode = SimpleTreeNode(456, None)
        self.tree.AddChild(None, first_node)
        self.tree.AddChild(first_node, second_node)
        self.assertEqual(self.tree.Count(), 2)
        self.assertEqual(self.tree.LeafCount(), 1)
        self.assertEqual(self.tree.Root, first_node)

    def test_on_predefined_tree(self) -> None:
        ''' Expected node count = 9, leaves count = 4. '''
        first_node : SimpleTreeNode = SimpleTreeNode(111, None)
        second_node : SimpleTreeNode = SimpleTreeNode(222, None)
        third_node : SimpleTreeNode = SimpleTreeNode(333, None)
        fourth_node : SimpleTreeNode = SimpleTreeNode(444, None)
        fifth_node : SimpleTreeNode = SimpleTreeNode(555, None)
        sixth_node : SimpleTreeNode = SimpleTreeNode(666, None)
        seventh_node : SimpleTreeNode = SimpleTreeNode(777, None)
        eighth_node : SimpleTreeNode = SimpleTreeNode(888, None)
        ninth_node : SimpleTreeNode = SimpleTreeNode(999, None)
        self.tree.AddChild(None, first_node)
        self.tree.AddChild(first_node, second_node)
        self.tree.AddChild(first_node, third_node)
        self.tree.AddChild(second_node, fourth_node)
        self.tree.AddChild(second_node, fifth_node)
        self.tree.AddChild(third_node, sixth_node)
        self.tree.AddChild(fifth_node, seventh_node)
        self.tree.AddChild(fifth_node, eighth_node)
        self.tree.AddChild(sixth_node, ninth_node)
        self.assertEqual(self.tree.Count(), 9)
        self.assertEqual(self.tree.LeafCount(), 4)


unittest.main()
