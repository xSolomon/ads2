''' Tests for lesson 1 Simple Tree methods. '''

import unittest
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

    def test_constructing_tree_with_root(self) -> None:
        ''' Expected node and leaf count = 1. '''
        first_node = SimpleTreeNode(5, None)
        test_tree = SimpleTree(first_node)
        self.assertEqual(test_tree.Root, first_node)
        self.assertEqual(test_tree.Count(), 1)
        self.assertEqual(test_tree.LeafCount(), 1)

    def test_move(self) -> None:
        ''' Expected nothing changed in each of situations:
            1) Moving None node.
            2) Moving node to itself as parent.
            3) Moving node to same parent. '''
        first_node = SimpleTreeNode(5, None)
        second_node = SimpleTreeNode(7, None)
        test_tree = SimpleTree(first_node)
        test_tree.AddChild(first_node, second_node)
        self.tree.MoveNode(None, test_tree.Root)
        self.tree.MoveNode(second_node, second_node)
        self.tree.MoveNode(second_node, first_node)
        self.assertEqual(test_tree.Root, first_node)
        self.assertEqual(test_tree.Count(), 2)
        self.assertEqual(test_tree.LeafCount(), 1)
        self.assertEqual(test_tree.GetAllNodes(), [first_node, second_node])


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
        ''' Expected node count = 9, leaves count = 4,
            tree structure must be exactly as in test list.
            All values must be found.
            Move mustn't change nodes count, but change tree structure. 
            Tree structure after all deletions must be exactly as in the test lists. '''
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
        test_get : list[SimpleTreeNode] = [first_node, second_node, fourth_node, fifth_node,
        seventh_node, eighth_node, third_node, sixth_node, ninth_node]
        test_search : list[SimpleTreeNode] = [first_node, second_node, third_node, fourth_node,
        fifth_node, sixth_node, seventh_node, eighth_node, ninth_node]
        self.assertEqual(self.tree.GetAllNodes(), test_get)
        for i in range(9):
            with self.subTest(i = i, value = 111 + i * 111):
                self.assertEqual(self.tree.FindNodesByValue(111 + i * 111), [test_search[i]])
        self.tree.MoveNode(fifth_node, third_node)
        test_move : list[SimpleTreeNode] = [first_node, second_node, fourth_node, third_node,
        sixth_node, ninth_node, fifth_node, seventh_node, eighth_node]
        self.assertEqual(self.tree.GetAllNodes(), test_move)
        self.tree.DeleteNode(second_node)
        test_first_delete : list[SimpleTreeNode] = [first_node, third_node,
        sixth_node, ninth_node, fifth_node, seventh_node, eighth_node]
        self.assertEqual(self.tree.GetAllNodes(), test_first_delete)
        self.tree.DeleteNode(sixth_node)
        test_second_delete : list[SimpleTreeNode] = [first_node, third_node,
            fifth_node, seventh_node, eighth_node]
        self.assertEqual(self.tree.GetAllNodes(), test_second_delete)

    def test_search_on_predefined_sameval_tree(self) -> None:
        ''' Expected list with all nodes in exactly same position they are in the test list. '''
        first_node : SimpleTreeNode = SimpleTreeNode(111, None)
        second_node : SimpleTreeNode = SimpleTreeNode(111, None)
        third_node : SimpleTreeNode = SimpleTreeNode(111, None)
        fourth_node : SimpleTreeNode = SimpleTreeNode(111, None)
        fifth_node : SimpleTreeNode = SimpleTreeNode(111, None)
        sixth_node : SimpleTreeNode = SimpleTreeNode(111, None)
        seventh_node : SimpleTreeNode = SimpleTreeNode(111, None)
        eighth_node : SimpleTreeNode = SimpleTreeNode(111, None)
        ninth_node : SimpleTreeNode = SimpleTreeNode(111, None)
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
        test_search : list[SimpleTreeNode] = [first_node, second_node, fourth_node, fifth_node,
        seventh_node, eighth_node, third_node, sixth_node, ninth_node]
        self.assertEqual(self.tree.FindNodesByValue(111), test_search)

    def test_symmetry_on_empty_tree(self) -> None:
        ''' Empty tree is symmetric. '''
        self.assertTrue(self.tree.is_symmetric())

    def test_symmetry_on_one_node_tree(self) -> None:
        ''' Tree with only root node is symmetric. '''
        self.tree.AddChild(None, SimpleTreeNode(111, None))
        self.assertTrue(self.tree.is_symmetric())

    def test_symmetry_on_three_node_trees(self) -> None:
        ''' Only the tree with non-equal keys on root children is not symmetric. '''
        trees : list[SimpleTree] = [SimpleTree(None) for _ in range(3)]
        for tree in trees:
            tree.AddChild(None, SimpleTreeNode(123, None))
            tree.AddChild(tree.Root, SimpleTreeNode(456, tree.Root))
        trees[0].AddChild(trees[0].Root.Children[0], SimpleTreeNode(789, trees[0].Root.Children[0])) # List-like variant.
        trees[1].AddChild(trees[1].Root, SimpleTreeNode(789, trees[1].Root)) # Second root child with different key.
        trees[2].AddChild(trees[2].Root, SimpleTreeNode(456, trees[2].Root)) # Second root child with equal key.
        results : list[bool] = [True, False, True]
        for i, tree in enumerate(trees):
            with self.subTest(i = i):
                self.assertEqual(results[i], tree.is_symmetric())

unittest.main()
