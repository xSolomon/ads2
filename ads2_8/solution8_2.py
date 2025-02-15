''' Lesson 8 task 2 solution. '''

from enum import Enum


class SearchStatus(Enum):
    ''' Stages of processing while searching for any cycles. '''
    WAITING = 1
    PROCESSING = 2
    FINISHED = 3

class Vertex:
    ''' Wrapper for raw value. '''
    def __init__(self, val : int):
        self.value : int = val # Vertex value/weight.

class DirectedGraph:
    ''' Represented via adjacency matrix and vertex list.
        Row represents node and pathes to another node. '''
    def __init__(self, size : int):
        self.max_vertex : int = size # Max vertex number graph can hold.
        self.m_adjacency : list[list[int]] = [[0] * size for _ in range(size)] # Adjacency matrix.
        self.vertex : list[int] = [None] * size # List of verteces.
        self.first_free_index : int = 0

    def max_verteces(self) -> int:
        ''' Returns max_verteces graph can hold. '''
        return self.max_vertex

    def add_vertex(self, value : int) -> bool:
        ''' Adds new vertex with given value in the first free place.
            Returns whether vertex was added. '''
        if self.first_free_index >= self.max_vertex: # Graph is full
            return False
        self.vertex[self.first_free_index] = Vertex(value)
        self.first_free_index += 1
        return True

    def remove_vertex(self, vertex_index : int) -> bool:
        ''' Removes vertex and all its edges.
            Returns whether vertex was removed. '''
        if self.vertex[vertex_index] is None:
            return False
        self.vertex[vertex_index] = None
        for v2 in range(len(self.vertex)):
            self.m_adjacency[vertex_index][v2] = 0
            self.m_adjacency[v2][vertex_index] = 0
        self.first_free_index -= 1
        return True

    def is_edge(self, from_vertex_index : int, to_vertex_index : int) -> bool:
        ''' Checks whether there is an edge from one vertex to another. '''
        return self.m_adjacency[from_vertex_index][to_vertex_index] == 1

    def add_edge(self, from_vertex_index : int, to_vertex_index : int) -> bool:
        ''' Adds edge from one vertex to another. 
            Returns whether edge was added.'''
        if self.vertex[from_vertex_index] is None or \
           self.vertex[to_vertex_index] is None or \
           self.m_adjacency[from_vertex_index][to_vertex_index] == 1:
            return False
        self.m_adjacency[from_vertex_index][to_vertex_index] = 1
        return True

    def remove_edge(self, from_vertex_index : int, to_vertex_index : int) -> bool:
        ''' Removes edge between given verteces.
            Returns whether edge was removed. '''
        if self.vertex[from_vertex_index] is None or \
           self.vertex[to_vertex_index] is None or \
           self.m_adjacency[from_vertex_index][to_vertex_index] == 0:
            return False
        self.m_adjacency[from_vertex_index][to_vertex_index] = 0
        return True

    def _has_cycles(self, from_vertex_index : int, search_statuses : list[SearchStatus]) -> bool:
        ''' Searches if any path from that node leads to cycle. '''
        # Reached subgraph that has no cycles.
        if search_statuses[from_vertex_index] == SearchStatus.FINISHED:
            return False
        # Returned to not finished not, a cycle.
        if search_statuses[from_vertex_index] == SearchStatus.PROCESSING:
            return True
        search_statuses[from_vertex_index] = SearchStatus.PROCESSING
        for to_vertex_index, _ in enumerate(self.m_adjacency[from_vertex_index]):
            if self.is_edge(from_vertex_index, to_vertex_index) and \
               self._has_cycles(to_vertex_index, search_statuses): # Path leading to cycle
                return True
        search_statuses[from_vertex_index] = SearchStatus.FINISHED
        return False

    def is_cyclic(self) -> bool:
        ''' Checks whether graph has at least one cycle. '''
        search_statuses : list[SearchStatus] = \
            [SearchStatus.WAITING for _ in range(self.first_free_index)]
        for vertex_index, _ in enumerate(search_statuses):
            if self._has_cycles(vertex_index, search_statuses):
                return True
        return False
