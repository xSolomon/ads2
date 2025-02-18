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
        self.search_status : SearchStatus = SearchStatus.WAITING

class DirectedGraph:
    ''' Represented via adjacency matrix and vertex list.
        Row represents node and pathes to another node. '''
    def __init__(self, size : int):
        self.max_vertex : int = size # Max vertex number graph can hold.
        self.m_adjacency : list[list[int]] = [[0] * size for _ in range(size)] # Adjacency matrix.
        self.vertex : list[Vertex] = [None] * size # List of verteces.
        self.first_free_index : int = 0

    def get_max_vertex(self) -> int:
        ''' Returns max_vertex graph can hold. '''
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

    def _has_cycles(self, from_vertex_index : int, current_path : list[int]) -> bool:
        ''' Searches cycles using DFS. '''
        self.vertex[from_vertex_index].search_status = SearchStatus.PROCESSING
        to_vertex_index : int = -1
        for vertex_index, _ in enumerate(self.m_adjacency[from_vertex_index]):
            # Filter vertex not having edges.
            if not self.is_edge(from_vertex_index, vertex_index):
                continue
            # Filter vertex already completed.
            if self.vertex[vertex_index].search_status == SearchStatus.FINISHED:
                continue
            # Found cycle.
            if self.vertex[vertex_index].search_status == SearchStatus.PROCESSING:
                return True
            to_vertex_index = vertex_index
            break
        # Found not visited vertex.
        if to_vertex_index != -1:
            current_path.append(to_vertex_index)
            return self._has_cycles(to_vertex_index, current_path)
        self.vertex[from_vertex_index].search_status = SearchStatus.FINISHED
        current_path.pop()
        if len(current_path) == 0:
            return False
        return self._has_cycles(current_path[-1], current_path)

    def is_cyclic(self) -> bool:
        ''' Checks whether graph has at least one cycle. '''
        for vertex in self.vertex: # Make all vertex unvisited.
            if vertex:
                vertex.search_status = SearchStatus.WAITING
        # We must search all graph in case we can't reach all vertex from one.
        for vertex_index, _ in enumerate(self.vertex):
            if self.vertex[vertex_index] and self._has_cycles(vertex_index, [vertex_index]):
                return True
        return False
