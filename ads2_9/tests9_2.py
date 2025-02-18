''' Tests for lesson 9 task 2 solution. '''

import unittest
from solution9_2 import BSTNode, BalancedBST

class BalancedBSTTests(unittest.TestCase):
    ''' Tests for make_balanced function. '''
    def setUp(self) -> None:
        ''' Test preparations. '''
        self.tree : BalancedBST = BalancedBST()

    def tearDown(self) -> None:
        ''' Aftertest cleanup. '''
        self.tree = None

    def test_make_balanced_on_empty_tree(self) -> None:
        ''' Expected empty tree as the result. '''
        tree_to_balance : BalancedBST = BalancedBST()
        balanced_tree : BalancedBST = self.tree.make_balanced(tree_to_balance)
        self.assertTrue(balanced_tree.IsBalanced(balanced_tree.Root))

    def test_make_balanced_on_predefined_trees(self) -> None:
        ''' For each tree, resulting tree must be balanced. '''
        # Stores all possible five-node tree variants.
        # Most inner list represents two childs being None or other node.
        # Second inner list represents one of tree variants.

        tree_to_balance : BalancedBST = BalancedBST()
        balanced_tree : BalancedBST = self.tree.make_balanced(tree_to_balance)


unittest.main()
