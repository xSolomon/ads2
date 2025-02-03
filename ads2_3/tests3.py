''' Tests for lesson 3 Binary Search Tree traversal methods. '''

import unittest
from solution3 import BSTNode, BST

class BSTTests(unittest.TestCase):
    ''' Tests for BST depth and breadth traversals. '''
    def setUp(self) -> None:
        ''' Test preparations. '''
        self.tree = BST(None)

    def tearDown(self) -> None:
        ''' Aftertest cleanup. '''
        while self.tree.Count() > 0:
            self.assertTrue(self.tree.DeleteNodeByKey(self.tree.Root.NodeKey))
        self.assertEqual(self.tree.Count(), 0)
        self.assertIsNone(self.tree.Root)
        del self.tree

    def insert_values(self, values : list[int]) -> None:
        ''' Adds values to the tree one-by-one. Assumes key is the same as value. '''
        for value in values:
            self.tree.AddKeyValue(value, value)

    def test_traversals_on_empty_tree(self) -> None:
        ''' Expected each traversal to return empty tuple. '''
        self.assertEqual(self.tree.DeepAllNodes(0), ())
        self.assertEqual(self.tree.DeepAllNodes(1), ())
        self.assertEqual(self.tree.DeepAllNodes(2), ())
        self.assertEqual(self.tree.WideAllNodes(), ())

    def test_traversals_on_three_node_tree(self) -> None:
        ''' Test functions on tree with three nodes (root with two childs).
            Root = 8, left child = 4, right child = 12. '''
        self.insert_values([8, 4, 12])
        self.assertEqual(self.tree.DeepAllNodes(0),
            (self.tree.Root.LeftChild, self.tree.Root, self.tree.Root.RightChild))
        self.assertEqual(self.tree.DeepAllNodes(1),
            (self.tree.Root.LeftChild, self.tree.Root.RightChild, self.tree.Root))
        self.assertEqual(self.tree.DeepAllNodes(2),
            (self.tree.Root, self.tree.Root.LeftChild, self.tree.Root.RightChild))
        self.assertEqual(self.tree.WideAllNodes(),
            (self.tree.Root, self.tree.Root.LeftChild, self.tree.Root.RightChild))

    def test_traversals_on_fifteen_node_tree(self) -> None:
        ''' Test on tree with 15 nodes total.
            Values from 1 to 15, root value = 8. '''
        self.insert_values([8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15])
        root = self.tree.Root
        breadth_traversal : tuple[BSTNode] = (root, root.LeftChild, root.RightChild,
        root.LeftChild.LeftChild, root.LeftChild.RightChild, root.RightChild.LeftChild,
        root.RightChild.RightChild, root.LeftChild.LeftChild.LeftChild,
        root.LeftChild.LeftChild.RightChild, root.LeftChild.RightChild.LeftChild,
        root.LeftChild.RightChild.RightChild, root.RightChild.LeftChild.LeftChild,
        root.RightChild.LeftChild.RightChild, root.RightChild.RightChild.LeftChild,
        root.RightChild.RightChild.RightChild)
        self.assertEqual(self.tree.WideAllNodes(), breadth_traversal)

    def test_inverse_on_empty_tree(self) -> None:
        ''' Expected nothing changes. '''
        tree_root : BSTNode = self.tree.inverse_tree()
        self.assertEqual(self.tree.Count(), 0)
        self.assertIsNone(tree_root)

    def test_inverse_on_three_node_tree(self) -> None:
        ''' Root = 8, left child = 4, right child = 12.
            Expected swap of left and right children. '''
        self.insert_values([8, 4, 12])
        tree_before_inverse : tuple[BSTNode] = self.tree.DeepAllNodes(0)
        self.tree.inverse_tree()
        self.assertEqual(self.tree.Count(), 3)
        self.assertEqual([node.NodeValue for node in self.tree.DeepAllNodes(0)],
            [node.NodeValue for node in tree_before_inverse[::-1]])

    def test_inverse_on_fifteen_node_tree(self) -> None:
        ''' Test on tree with 15 nodes total.
            Values from 1 to 15, root value = 8. '''
        self.insert_values([8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15])
        tree_before_inverse : tuple[BSTNode] = self.tree.DeepAllNodes(0)
        self.tree.inverse_tree()
        self.assertEqual(self.tree.Count(), 15)
        self.assertEqual([node.NodeValue for node in self.tree.DeepAllNodes(0)],
            [node.NodeValue for node in tree_before_inverse[::-1]])

    def test_max_level_sum_on_empty_tree(self) -> None:
        ''' Expected 'None' as return value. '''
        self.assertIsNone(self.tree.level_with_max_sum())

    def test_max_level_sum_on_three_node_tree(self) -> None:
        ''' Root = 8, left child = 4, right child = 12.
            Expected level = 2. '''
        self.insert_values([8, 4, 12])
        self.assertEqual(self.tree.level_with_max_sum(), 2)

    def test_max_level_sum_on_fifteen_node_tree(self) -> None:
        ''' Test on tree with 15 nodes in total.
            Values from 1 to 15, root value = 8. Expected level = 4. '''
        self.insert_values([8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15])
        self.assertEqual(self.tree.level_with_max_sum(), 4)

    def test_recover_on_empty_tree(self) -> None:
        ''' Test on empty lists. Must form an empty tree. '''
        self.assertEqual(self.tree.recover_binary_tree([], []).WideAllNodes(), ())

    def test_recover_on_three_node_tree(self) -> None:
        ''' Root = 8, left child = 4, right child = 12. '''
        self.assertEqual([node.NodeValue for node in \
            self.tree.recover_binary_tree([4, 8, 12], [8, 4, 12]).WideAllNodes()],
            [8, 4, 12])

    def test_recover_on_seven_node_tree(self) -> None:
        ''' Tree in BFS: [1, 2, 3, 4, 5, 6, 7]. '''
        self.assertEqual([node.NodeValue for node in \
            self.tree.recover_binary_tree(
                [4, 2, 5, 1, 6, 3, 7], [1, 2, 4, 5, 3, 6, 7])
                .WideAllNodes()],
            [1, 2, 3, 4, 5, 6, 7])

    def test_recover_on_fifteen_node_tree(self) -> None:
        ''' Tree in BFS: [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]. '''
        self.assertEqual([node.NodeValue for node in \
            self.tree.recover_binary_tree(
                [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
                [8, 4, 2, 1, 3, 6, 5, 7, 12, 10, 9, 11, 14, 13, 15])
                .WideAllNodes()],
            [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15])

unittest.main()
