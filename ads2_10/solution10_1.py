''' Lesson 10 task 1 solution. '''

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

    def get_max_vertex(self) -> int:
        ''' Returns max_vertex graph can hold. '''
        return self.max_vertex

    def AddVertex(self, v : int) -> bool:
        ''' Adds new vertex with given value in the first free place. '''
        for i, vertex in enumerate(self.vertex):
            if vertex is None:
                self.vertex[i] = Vertex(v)
                return True
        return False

    def RemoveVertex(self, v : int) -> bool:
        ''' Removes vertex and all its edges. '''
        if self.vertex[v] is None:
            return False
        self.vertex[v] = None
        for v2 in range(len(self.vertex)):
            self.m_adjacency[v][v2] = 0
            self.m_adjacency[v2][v] = 0
        return True

    def IsEdge(self, v1 : int, v2 : int) -> bool:
        ''' Checks whether verteces with given indexes are connected. '''
        return self.m_adjacency[v1][v2] == 1

    def AddEdge(self, v1 : int, v2 : int) -> bool:
        ''' Adds edge between given verteces. '''
        if self.vertex[v1] is None or self.vertex[v2] is None:
            return False
        if self.m_adjacency[v1][v2] == 1:
            return False
        self.m_adjacency[v1][v2] = 1
        self.m_adjacency[v2][v1] = 1
        return True

    def RemoveEdge(self, v1 : int, v2 : int) -> bool:
        ''' Removes edge between given verteces. '''
        if self.vertex[v1] is None or self.vertex[v2] is None:
            return False
        if self.m_adjacency[v1][v2] == 0:
            return False
        self.m_adjacency[v1][v2] = 0
        self.m_adjacency[v2][v1] = 0
        return True

    def DepthFirstSearch(self, VFrom : int, VTo : int) -> list[Vertex]:
        ''' Finds path between verteces in graph using depth-first method. '''
        for vertex in self.vertex:
            if vertex:
                vertex.Hit = False
        if VFrom < 0 or VFrom >= len(self.vertex):
            return []
        if not self.vertex[VFrom]:
            return []
        current_path : list[int] = [VFrom]
        while current_path:
            current_vertex_index : int = current_path[-1]
            self.vertex[current_vertex_index].Hit = True
            first_not_visited_index : int = -1
            for vertex_index, vertex in enumerate(self.vertex):
                if vertex and not vertex.Hit and self.IsEdge(current_vertex_index, vertex_index):
                    first_not_visited_index = vertex_index
                    break
            if first_not_visited_index != -1 and first_not_visited_index == VTo:
                current_path.append(VTo)
                return current_path
            if first_not_visited_index != -1:
                current_path.append(first_not_visited_index)
                continue
            current_path.pop()
        return [self.vertex[vertex_index] for vertex_index in current_path]

    def is_connected(self) -> bool:
        ''' Tries to find path from one vertex to all other.
            If DFS reaches all vertexes - graph is connected. '''
        self.DepthFirstSearch(0, -1)
        for vertex in self.vertex:
            if vertex and not vertex.Hit:
                return False
        return True
