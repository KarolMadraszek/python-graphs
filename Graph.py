class Graph:
    """
    (Un) Directed Multigraph class. Uses adjacency lists by default.
     
    CC Franciszek Moszczuk & Karol Madraszek
    """

    
    def __init__(self, vertex: set, edges: list, name = "Unnamed", directed = True):
        """
        Uses tuples by default because the graph isn't the same after it's modified,
        therefore it makes sense to make edges a list of tuples
        """
        # adjacency 
        self.directed = directed
        self.name = name
        # sort set
        # assumes only strings for now
        templist = sorted(vertex)
        
        # as it is the case in the adjacency matrix I need a 
        # f(X): int -> vertex 
        #self.IndexToVertex = dict(enumerate(templist))
        self.vertex = vertex
        
        # self.adjList: 
        # f(X): dict<int> -> list<tuple>
        # maybe change this to str? no need to vti
        self.adjList = {}
        for i in range(len(templist)):
            self.adjList[templist[i]] = []
        print(self.adjList)
            
        for u, v in edges:
            if u not in self.vertex or v not in self.vertex:
               print(f"{u} or {v} not in set, skipping...")
            else:
               self.adjList[u].append((u, v))
        #self.edges = edges
        print(self.adjList)
 
    def __str__(self):
        return f"Multigraph {self.name} with the following params:\n \
               Vertex: {self.vertex}, Adjacency list: {self.adjList}"

    def add_vertex(self, vertex: str):
        """
        Adds a vertex to the graph. Assumed a UTF-8 character (Python default)
        """
        # make sure it's really a string? 
        if vertex not in self.vertex:
           self.adjList[vertex] = []
           self.vertex.add(vertex)
        else:
           print(f"Vertex {vertex} already in graph!")
              

    def remove_vertex(self, vertex: str):
        """
        Deletes a vertex. Deletes all edges O(V)
        """
        if vertex not in self.vertex:
           raise KeyError("Vertex not in set")
        else:
           del self.adjList[vertex]
           self.vertex.remove(vertex)

    def add_edge(self, edge: tuple):
        """
        Adds an edge. Checks whether there are vertexes in a graph, then inserts an additional edge.
        """
        # Check whether this is a tuple
        if type(edge) is tuple:
           a, b = edge
           if a not in self.vertex or b not in self.vertex:
              raise KeyError(f"{a} or {b} not in the list of verticies")
           self.adjList[a].append((a, b))
        else:
           raise TypeError(f"Bad Type: {edge} is", edge)


    def remove_edge(self, edge: tuple):
        """
        Removes an edge. Throws an error if there is no such edge.
        """
        self.adjList[edge[0]].remove(edge)

    def to_adj(self):
        """
        Either print out an adjecency matrix or create a new graph. 
        """
        raise NotImplemented
        



newGraph = Graph({'a', 'b'}, [('a', 'b',), ('a', 'b')], name = "Example")        
print(newGraph)
newGraph.add_vertex("z")
print(newGraph)
newGraph.add_edge(("b", "z"))
print(newGraph)
#newGraph.add_edge(("z", "y")) #errors out on purpose
newGraph.remove_edge(("a", "b"))
print(newGraph)
newGraph.remove_vertex("b")
# newGraph.remove_vertex("p") # key not in set
print(newGraph)
