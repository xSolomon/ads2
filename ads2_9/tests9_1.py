''' Tests for lesson 9 task 1 solution. '''

import unittest
from solution9_1 import SimpleTreeNode, SimpleTree

class HeapTests(unittest.TestCase):
    ''' Tests for MakeHeap, Add, GetMax functions. '''
    def setUp(self) -> None:
        ''' Test preparations. '''
        self.tree : SimpleTree = SimpleTree(None)

    def tearDown(self) -> None:
        ''' Aftertest cleanup. '''
        self.tree.DeleteNode(self.tree.Root)
        self.tree = None

    def form_tree(self, key_pairs : list[tuple]) -> None:
        ''' Forms tree from tuple of pairs of unique keys. '''
        for key_pair in key_pairs:
            found_nodes : list[SimpleTreeNode] = self.tree.FindNodesByValue(key_pair[0])
            parent_node : SimpleTreeNode = None if not found_nodes else found_nodes[0]
            self.tree.AddChild(parent_node, SimpleTreeNode(key_pair[1], parent_node))

    def test_on_empty_tree(self) -> None:
        ''' Must return an empty list. '''
        self.assertEqual(self.tree.EvenTrees(), [])

    def test_on_singlenode_tree(self) -> None:
        ''' Must return an empty list. '''
        self.form_tree([(None, 1)])
        self.assertEqual(self.tree.EvenTrees(), [])

    def test_on_two_node_tree(self) -> None:
        ''' Must return an empty list. '''
        self.form_tree([(None, 1), (1, 2)])
        self.assertEqual(self.tree.EvenTrees(), [])

    def test_on_three_nodes_trees(self) -> None:
        ''' In case where root has one child, must return vertex between that nodes. '''
        self.form_tree([(None, 1), (1, 2), (2, 3)])
        self.assertEqual(self.tree.EvenTrees(), [1, 2])
        self.tree.DeleteNode(self.tree.Root)
        self.form_tree([(None, 1), (1, 2), (1, 3)])
        self.assertEqual(self.tree.EvenTrees(), [])

    def test_on_predefined_trees(self) -> None:
        ''' For each tree, result must be the same as in the result list. '''
        trees : list[list[tuple]] = [
            [(None, 1), (1, 2), (2, 5), (2, 7)],
            [(None, 1), (1, 6), (6, 8), (8, 9), (8, 10)],
            [(None, 1), (1, 2), (1, 3), (1, 6), (2, 5), (2, 7), (3, 4), (6, 8), (8, 9), (8, 10)],
            [(None, 1), (1, 2), (1, 3), (1, 6), (2, 5), (2, 7), (3, 4), (6, 8), (8, 9), (8, 10), (5, 11), (11, 12), (12, 13), (13, 14)],
        ]
        results : list[list[int]] = [
            [],
            [1, 6],
            [1, 3, 1, 6],
            [12, 13, 5, 11, 1, 3, 1, 6]
        ]
        for i, tree in enumerate(trees):
            self.form_tree(tree)
            with self.subTest():
                self.assertEqual(self.tree.EvenTrees(), results[i])
            self.tree.DeleteNode(self.tree.Root)

unittest.main()
