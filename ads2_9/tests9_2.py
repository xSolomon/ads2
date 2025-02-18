''' Tests for lesson 9 task 2 solution. '''

import unittest
from bst import BST
from solution9_2 import BSTNode, BalancedBST

class BalancedBSTTests(unittest.TestCase):
    ''' Tests for make_balanced function. '''
    def setUp(self) -> None:
        ''' Test preparations. '''
        self.tree : BalancedBST = BalancedBST()

    def tearDown(self) -> None:
        ''' Aftertest cleanup. '''
        self.tree = None

    def insert_values(self, tree : BST, values : list[int]) -> None:
        ''' Adds values to the tree one-by-one. Assumes key is the same as value. '''
        for value in values:
            tree.AddKeyValue(value, value)

    def test_make_balanced_on_empty_tree(self) -> None:
        ''' Expected empty tree as the result. '''
        tree_to_balance : BST = BST(None)
        balanced_tree : BalancedBST = self.tree.make_balanced(tree_to_balance)
        self.assertTrue(balanced_tree.IsBalanced(balanced_tree.Root))

    def test_make_balanced_on_predefined_trees(self) -> None:
        ''' Each tree should be balanced after executing function. '''
        tree_to_balance : BalancedBST = BST(None)
        self.insert_values(tree_to_balance,
            [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15])
        balanced_tree : BalancedBST = self.tree.make_balanced(tree_to_balance)
        self.assertTrue(balanced_tree.IsBalanced(balanced_tree.Root))
        self.insert_values(tree_to_balance,
            [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])
        balanced_tree : BalancedBST = self.tree.make_balanced(tree_to_balance)
        self.assertTrue(balanced_tree.IsBalanced(balanced_tree.Root))
        tree_to_balance : BalancedBST = BST(None)
        self.insert_values(tree_to_balance, 
            [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
        balanced_tree : BalancedBST = self.tree.make_balanced(tree_to_balance)
        self.assertTrue(balanced_tree.IsBalanced(balanced_tree.Root))


unittest.main()
