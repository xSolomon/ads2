''' Solution for lesson 2. '''

class BSTNode:
    ''' Value can be distinct with key if needed. '''
    def __init__(self, key, val, parent) -> None:
        self.NodeKey = key # node key
        self.NodeValue = val # node value
        self.Parent = parent # Parent (None for root)
        self.LeftChild = None # левый потомок
        self.RightChild = None # правый потомок


class BSTFind: # промежуточный результат поиска
    ''' Holds results of BST FindNodeByKey function. '''    
    def __init__(self) -> None:
        self.Node = None # None if tree is empty
        self.NodeHasKey = False # True if node found.
        self.ToLeft = False # True if new node must be left child.

class BST:
    ''' Binary sorted tree. '''
    def __init__(self, node):
        self.Root = node # корень дерева, или None

    def FindNodeByKey(self, key):
        # ищем в дереве узел и сопутствующую информацию по ключу
        return None # возвращает BSTFind

    def AddKeyValue(self, key, val):
        # добавляем ключ-значение в дерево
        return False # если ключ уже есть
  
    def FinMinMax(self, FromNode, FindMax):
        # ищем максимальный/минимальный ключ в поддереве
        # возвращается объект типа BSTNode
        return None
	
    def DeleteNodeByKey(self, key):
        # удаляем узел по ключу
        return False # если узел не найден

    def Count(self):
        return 0 # количество узлов в дереве