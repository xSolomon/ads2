''' Solution for lesson 2. '''

class BSTNode:
    ''' Value can be distinct with key if needed. '''
    def __init__(self, key, val, parent) -> None:
        self.NodeKey = key # Node key.
        self.NodeValue = val # Node value.
        self.Parent : BSTNode = parent # Parent (None for root).
        self.LeftChild : BSTNode = None # Left child.
        self.RightChild : BSTNode = None # Right child.


class BSTFind: # промежуточный результат поиска
    ''' Holds results of BST FindNodeByKey function. '''    
    def __init__(self) -> None:
        self.Node : BSTNode = None # None if tree is empty
        self.NodeHasKey : bool = False # True if node found.
        self.ToLeft : bool = False # True if new node must be left child.

class BST:
    ''' Binary sorted tree. '''
    def __init__(self, node : BSTNode) -> None:
        self.Root = node # Tree root, can be None.
        self.NodesCount : int = 0 if self.Root is None else 1

    def FindNodeByKey(self, key) -> BSTFind:
        # ищем в дереве узел и сопутствующую информацию по ключу
        return None # возвращает BSTFind

    def AddKeyValue(self, key, val) -> bool:
        # добавляем ключ-значение в дерево
        return False # если ключ уже есть
  
    def FinMinMax(self, FromNode, FindMax) -> BSTNode:
        # ищем максимальный/минимальный ключ в поддереве
        # возвращается объект типа BSTNode
        return None
	
    def DeleteNodeByKey(self, key) -> bool:
        # удаляем узел по ключу
        return False # если узел не найден

    def Count(self) -> int:
        return 0 # количество узлов в дереве