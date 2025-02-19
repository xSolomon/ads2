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
        tree : SimpleTree = SimpleTree(None)
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

    def test_count_even_subtrees_on_empty_tree(self) -> None:
        ''' Must return 0. '''
        tree : SimpleTree = SimpleTree(None)
        self.assertEqual(tree.total_even_subtrees(None), 0)

    def test_count_even_subtrees_on_one_node_tree(self) -> None:
        ''' Must return 0. '''
        root_node : SimpleTreeNode = SimpleTreeNode(1, None)
        tree : SimpleTree = SimpleTree(None)
        self.assertEqual(tree.total_even_subtrees(root_node), 0)

    def test_count_even_subtrees_on_three_node_trees(self) -> None:
        ''' Must return 0 for case with balanced tree and 1 otherwise. '''
        # Balanced tree.
        root_node : SimpleTreeNode = SimpleTreeNode(1, None)
        second_node : SimpleTreeNode = SimpleTreeNode(2, None)
        third_node : SimpleTreeNode = SimpleTreeNode(3, None)
        tree : SimpleTree = SimpleTree(None)
        tree.AddChild(None, root_node)
        tree.AddChild(root_node, second_node)
        tree.AddChild(root_node, third_node)
        with self.subTest():
            self.assertEqual(tree.total_even_subtrees(root_node), 0)
        # List-like tree.
        tree : SimpleTree = SimpleTree(None)
        root_node : SimpleTreeNode = SimpleTreeNode(1, None)
        second_node : SimpleTreeNode = SimpleTreeNode(2, None)
        third_node : SimpleTreeNode = SimpleTreeNode(3, None)
        tree.AddChild(None, root_node)
        tree.AddChild(root_node, second_node)
        tree.AddChild(second_node, third_node)
        with self.subTest():
            self.assertEqual(tree.total_even_subtrees(root_node), 1)

    def test_count_even_subtrees_on_predefined_tree(self) -> None:
        ''' Tree root has 4 even trees, and node 2 has 1 even tree. '''
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
        eleventh_node : SimpleTreeNode = SimpleTreeNode(11, seventh_node)
        tree : SimpleTree = SimpleTree(None)
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
        tree.AddChild(seventh_node, eleventh_node)
        self.assertEqual(tree.total_even_subtrees(root_node), 4)
        self.assertEqual(tree.total_even_subtrees(second_node), 1)
        self.assertEqual(tree.total_even_subtrees(sixth_node), 0)
        self.assertEqual(tree.total_even_subtrees(eighth_node), 0)
        self.assertEqual(tree.total_even_subtrees(seventh_node), 0)
        self.assertEqual(tree.total_even_subtrees(third_node), 0)

    def test_count_even_subtrees_on_nine_node_tree(self) -> None:
        ''' Tree structure: root -> left
                                        -> left
                                               -> left
                                               -> right
                                        -> right
                                 -> right
                                        -> left
                                        -> right '''
        root_node : SimpleTreeNode = SimpleTreeNode(0, None)
        one_node : SimpleTreeNode = SimpleTreeNode(1, root_node)
        two_node : SimpleTreeNode = SimpleTreeNode(2, one_node)
        three_node : SimpleTreeNode = SimpleTreeNode(3, two_node)
        four_node : SimpleTreeNode = SimpleTreeNode(4, two_node)
        five_node : SimpleTreeNode = SimpleTreeNode(5, one_node)
        six_node : SimpleTreeNode = SimpleTreeNode(6, root_node)
        seven_node : SimpleTreeNode = SimpleTreeNode(7, six_node)
        eight_node : SimpleTreeNode = SimpleTreeNode(8, six_node)
        tree : SimpleTree = SimpleTree(None)
        tree.AddChild(None, root_node)
        tree.AddChild(root_node, one_node)
        tree.AddChild(one_node, two_node)
        tree.AddChild(two_node, three_node)
        tree.AddChild(two_node, four_node)
        tree.AddChild(one_node, five_node)
        tree.AddChild(root_node, six_node)
        tree.AddChild(six_node, seven_node)
        tree.AddChild(six_node, eight_node)
        self.assertEqual(tree.total_even_subtrees(root_node), 0)

unittest.main()
