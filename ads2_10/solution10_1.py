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
        for vertex in self.vertex:
            if vertex:
                vertex.Hit = False
        result_path : list[int] = self.DFS(VFrom, VTo, [])
        return [self.vertex[vertex_index] for vertex_index in result_path]





