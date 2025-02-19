''' Lesson 11 task 1 solution. '''

from typing import Tuple

class NodeBase:
    ''' Base Node, contains no data. '''
    def __init__(self):
        self.next : NodeBase = None
        self.prev : NodeBase = None

class Node(NodeBase):
    ''' Node with data. '''
    def __init__(self, v):
        super().__init__()
        self.value = v

class LinkedListIterator:
    ''' Implements iterator protocol for LinkedList. '''
    def __init__(self, linked_list : 'LinkedList'):
        self.head : NodeBase = linked_list._head
        self.current : NodeBase = self.head.next

    def __iter__(self) -> 'LinkedListIterator':
        return self

    def __next__(self):
        ''' Returns next value in the list. '''
        if self.current is self.head:
            raise StopIteration
        self.current = self.current.next
        return self.current.prev

class LinkedList:
    ''' Represents circular doubly linked list with dummy node. '''
    def __init__(self):
        self._head : NodeBase = NodeBase()
        self._head.next = self._head
        self._head.prev = self._head
        self._len : int = 0

    def __iter__(self) -> LinkedListIterator:
        ''' Returns iterator, allowing to traverse list. '''
        return LinkedListIterator(self)

    def __len__(self) -> int:
        ''' Get current length of the list. '''
        list_len : int = self._len
        return list_len

    def get_head(self) -> Node | None:
        ''' Returns current head. '''
        return self._head.next if self._head.next is not self._head else None

    def get_tail(self) -> Node | None:
        ''' Returns current head. '''
        return self._head.prev if self._head.prev is not self._head else None

    def insert(self, new_node : Node,  insertion_node : NodeBase = None,
        after : bool = False) -> bool:
        ''' Inserts new node in list.
            If after = false, insert node before given one.
            If after = true, insert node after given one.
            If insertion node is None and after = false, insert in head.
            If insertion node is None and after = true, insert in tail. '''
        if new_node is None: # Nothing to insert.
            return False
        if insertion_node is None and after: # Insert in tail.
            new_node.next = self._head
            new_node.prev = self._head.prev
            self._head.prev.next = new_node
            self._head.prev = new_node
            self._len += 1
            return True
        if insertion_node is None and not after: # Insert in head.
            new_node.prev = self._head
            new_node.next = self._head.next
            self._head.next.prev = new_node
            self._head.next = new_node
            self._len += 1
            return True
        if not after: # Insert before given node.
            new_node.next = insertion_node
            new_node.prev = insertion_node.prev
            insertion_node.prev.next = new_node
            insertion_node.prev = new_node
        else: # Insert after given node.
            new_node.prev = insertion_node
            new_node.next = insertion_node.next
            insertion_node.next.prev = new_node
            insertion_node.next = new_node
        self._len += 1
        return True

    def delete(self, val, delete_all : bool = False) -> None:
        ''' If delete_all = false, deletes first occurence of val in list.
            If delete_all = true, deletes all occurences of val in list. '''
        current : NodeBase = self._head
        while current.next is not self._head:
            if current.next.value == val: # Found first occurence, delete it.
                current.next = current.next.next
                del current.next.prev
                current.next.prev = current
                self._len -= 1
                break
            current = current.next
        if not delete_all:  # One node with val was deleted or no value was found
            return
        while current.next is not self._head:
            if current.next.value == val: # Found another occurence, delete it.
                current.next = current.next.next
                del current.next.prev
                current.next.prev = current
                self._len -= 1
                continue # Cause node was deleted, we don't advance.
            current = current.next

    def find(self, val) -> Node | None:
        ''' Finds first occurence of val in list and returns its node.
            If no node with this key, returns None. '''
        current : NodeBase = self._head
        while (current := current.next) is not self._head:
            if current.value == val: # Found key, return node.
                return current
        return None

    def find_all(self, val) -> list[Node]:
        ''' Finds all occurence of key in LinkedList.
            Returns python list of nodes with value = val. '''
        result : list[Node] = []
        current : NodeBase = self._head
        while (current := current.next) is not self._head:
            if current.value == val: # Found key, add node to the resulting list.
                result.append(current)
        return result

    def clean(self) -> None:
        ''' Delete every node in the list. '''
        current : NodeBase = self._head
        while current.next is not self._head:
            current.next = current.next.next
            del current.next.prev
            current.next.prev = current
            self._len -= 1

    def print_all_nodes(self) -> None:
        ''' Print list to the console. '''
        for node in self:
            print(node.value, end = ' <-> ')
        print('End of list.')

class Queue:
    ''' Represents FIFO queue. '''
    def __init__(self):
        self.queue : LinkedList = LinkedList()

    def enqueue(self, item) -> None:
        ''' Insert item in the tail of queue. '''
        self.queue.insert(Node(item), None, True)

    def dequeue(self):
        ''' Removes and returns item from queue head. '''
        if len(self.queue) == 0:
            return None
        item = self.queue.get_head().value
        self.queue.delete(self.queue.get_head().value)
        return item

    def peek(self):
        ''' Return queue head without removing it. '''
        return None if len(self.queue) == 0 else self.queue.get_head().value

    def size(self) -> int:
        ''' Returns current queue size. '''
        return len(self.queue)

class Vertex:
    ''' Wrapper for raw value. '''
    def __init__(self, val : int):
        self.Value : int = val # Vertex value/weight.
        self.Hit : bool = False # True if we visited Vertex during DFS algorithm.

class SimpleGraph:
    ''' Represented via adjacency matrix and vertex list. '''
    def __init__(self, size : int):
        self.max_vertex : int = size # Max vertex number graph can hold.
        self.m_adjacency = [[0] * size for _ in range(size)] # Adjacency matrix.
        self.vertex = [None] * size # List of verteces.

    def AddVertex(self, v : int) -> None:
        ''' Adds new vertex with given value in the first free place. '''
        for i, vertex in enumerate(self.vertex):
            if vertex is None:
                self.vertex[i] = Vertex(v)
                break

    def RemoveVertex(self, v : int) -> None:
        ''' Removes vertex and all its edges. '''
        if self.vertex[v] is None:
            return
        self.vertex[v] = None
        for v2 in range(len(self.vertex)):
            self.m_adjacency[v][v2] = 0
            self.m_adjacency[v2][v] = 0

    def IsEdge(self, v1 : int, v2 : int) -> bool:
        ''' Checks whether verteces with given indexes are connected. '''
        return self.m_adjacency[v1][v2] == 1

    def AddEdge(self, v1 : int, v2 : int) -> None:
        ''' Adds edge between given verteces. '''
        if self.vertex[v1] is None or self.vertex[v2] is None:
            return
        self.m_adjacency[v1][v2] = 1
        self.m_adjacency[v2][v1] = 1

    def RemoveEdge(self, v1 : int, v2 : int) -> None:
        ''' Removes edge between given verteces. '''
        self.m_adjacency[v1][v2] = 0
        self.m_adjacency[v2][v1] = 0

    def _mark_verteces_unvisited(self) -> None:
        ''' Resets visited status for DFS. '''
        for vertex in self.vertex:
            if vertex:
                vertex.Hit = False

    def DFS(self, VFrom : int, VTo : int, current_path : list[int]) -> list[int]:
        ''' Uses stack representing path between verteces. '''
        self.vertex[VFrom].Hit = True
        current_path.append(VFrom)
        while current_path:
            VFrom = current_path[-1]
            if self.IsEdge(VFrom, VTo):
                current_path.append(VTo)
                return current_path
            for vertex_index, vertex in enumerate(self.vertex):
                if self.IsEdge(VFrom, vertex_index) and not vertex.Hit:
                    return self.DFS(vertex_index, VTo, current_path)
            del current_path[-1]
        return current_path

    def DepthFirstSearch(self, VFrom : int, VTo : int) -> list[Vertex]:
        ''' Finds path between verteces in graph using depth-first method. '''
        self._mark_verteces_unvisited()
        result_path : list[int] = self.DFS(VFrom, VTo, [])
        return [self.vertex[vertex_index] for vertex_index in result_path]

    def BreadthFirstSearch(self, VFrom : int, VTo : int) -> list[Vertex]:
        ''' Finds path between vertex in graph using breadth-first method. '''
        self._mark_verteces_unvisited()
        not_visited_vertex : Queue = Queue()
        not_visited_vertex.enqueue((VFrom, [VFrom])) # Store path along with each vertex.
        while not_visited_vertex.size() > 0:
            path_to_node : list[int] = []
            VFrom, path_to_node = not_visited_vertex.dequeue()
            for vertex_index, vertex in enumerate(self.vertex):
                if not self.IsEdge(VFrom, vertex_index): # Not adjacent vertex, skip it.
                    continue
                if vertex_index == VTo: # Found path, return it.
                    return [self.vertex[vertex_index] for vertex_index in path_to_node + [VTo]]
                if not vertex.Hit: # Not visited vertex, mark it and enqueue.
                    vertex.Hit = True
                    not_visited_vertex.enqueue((vertex_index, path_to_node + [vertex_index]))
        return [] # No path found.

    def _all_cycles_bfs(self, from_vertex_index : int) -> list[list[Tuple[int, int]]]:
        ''' Performs bfs to detect cycles. '''
        cycles : list[list[Tuple[int,int]]] = []
        not_visited_vertex : Queue = Queue()
        vertex_parent : list[int] = [None * len(self.vertex)]
        not_visited_vertex.enqueue(from_vertex_index)
        self.vertex[from_vertex_index].Hit = True
        while not_visited_vertex.size() > 0:
            current_vertex_index : int = not_visited_vertex.dequeue()
            for to_vertex_index, vertex in enumerate(self.vertex):
                # Filter non adjacent vertex.
                if not self.IsEdge(current_vertex_index, to_vertex_index):
                    continue
                # Mark as visited and to queue.
                if not vertex.Hit:
                    vertex.Hit = True
                    vertex_parent[to_vertex_index] = current_vertex_index
                    not_visited_vertex.enqueue(to_vertex_index)
                    continue
                # Found cycle, add it to the result.
                cycle_edges : list[Tuple(int, int)] = [(current_vertex_index, to_vertex_index)]

        

    def find_all_cycles(self) -> list[list[Tuple[int, int]]]:
        ''' Find all cycles in graph and return it as a list of edges indices. '''
        self._mark_verteces_unvisited()
        result : list[list[Tuple[int, int]]] = []
        # Scan each vertex in case of not connected graph.
        for from_vertex_index, vertex in enumerate(self.vertex):
            if vertex and not vertex.Hit:
                result.extend(self._all_cycles_bfs(from_vertex_index))
        return result



