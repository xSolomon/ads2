''' Tests for BST via array methods. '''

import unittest
from solution4 import aBST

class aBSTTests(unittest.TestCase):
    ''' Tests for aBST FindKeyIndex and Addkey methods. '''
    def test_on_empty_tree(self) -> None:
        ''' Expected find to give root key (0).
            Also add must be root. '''
        tree : aBST = aBST(0)
        self.assertEqual(tree.FindKeyIndex(123), 0)
        self.assertEqual(tree.AddKey(123), 0)
        self.assertIsNotNone(tree.Tree[0])
        self.assertEqual(tree.FindKeyIndex(123), 0)

    def test_on_predefined_tree(self) -> None:
        ''' Node values (in insert order) are:
            50, 25, 75, 37, 62, 84, 31, 43, 55, 92
            Expected correct BST form. '''
        tree : aBST = aBST(3)
        values : list[int] = [50, 25, 75, 37, 62, 84, 31, 43, 55, 92]
        indexes : list[int] = [0, 1, 2, 4, 5, 6, 9, 10, 11, 14]
        for i, key in enumerate(values):
            with self.subTest(i = i, key = key, index = indexes[i]):
                self.assertEqual(tree.AddKey(key), indexes[i])
        for i, key in enumerate(values):
            with self.subTest(i = i, key = key, index = indexes[i]):
                self.assertEqual(tree.FindKeyIndex(key), indexes[i])
                self.assertEqual(tree.AddKey(key), indexes[i])



unittest.main()
