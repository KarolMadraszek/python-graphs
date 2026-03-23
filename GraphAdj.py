# required dep
import numpy as np

class GraphAdj:
    """
    Directed Multigraph class. Uses adjacency matrix.
     
    CC Franciszek Moszczuk
    """

    
    def __init__(self, vertex: set, edges: list, name = "Unnamed", directed = True):
        """
        Uses tuples by default because the graph isn't the same after it's modified,
        therefore it makes sense to make edges a list of tuples
        1. Sort because 
        2. Append numbers to vertex 
        # {a, c, 1, c, ...} --> {0: a, 1: c, } etc 
        # IndexToVertex === ITV
        # VertexToIndex === VTI
        
        """
        # set basic params
        self.directed = directed
        self.name = name

        # sort set
        # assumes only strings for now
        templist = sorted(vertex)
         
        # technically those two should be linked somehow but they arent
        # THIS SHOULD BE A SEPARATE CLASS!!! CAN AND WILL GET DESYNCED
        self.IndexToVertex = dict(enumerate(templist))
        self.VertexToIndex = {v: k for k, v in self.IndexToVertex.items()}
        # create a numpy array of the size dict
        a = len(self.VertexToIndex)
        self.adjMatrix = np.zeros((a, a), dtype=np.int_)
        # convert each edge to adjacency matrix
        for u, v in edges:
            try:
                self.adjMatrix[self.VertexToIndex[u], self.VertexToIndex[v]] += 1
                if not self.directed and (u != v):
                    # avoids loop duplication 
                    self.adjMatrix[self.VertexToIndex[v], self.VertexToIndex[u]] += 1
            except KeyError:
                print(f"Vertex {u} or {v} is missing from set, skipping")
 
    def __str__(self):
        # Todo: 
        return f"Matrix Multigraph {self.name} with the following params:\n \
               Vertex: {self.IndexToVertex}\n, Matrix: \n {self.adjMatrix}"

    def add_vertex(self, vertex: str):
        """
        Adds a vertex to the graph. Assumed a UTF-8 character (Python default).
           Resizes the numpy array.
           Question: should I sort the array first? Or leave it be?
        """
        # add two vertexes in both dicts, resize numpy
        if (vertex) in self.VertexToIndex:
           print(f"Vertex {vertex} already in set")
           return false
        # probably should insert at last pos and then sort
        self.adjMatrix = np.insert(self.adjMatrix, insert_pos, 0, axis=0)
        self.adjMatrix = np.insert(self.adjMatrix, insert_pos, 0, axis=1) 
        # entries are sorted
        
        # (add in lexical order)
        #self.adjMatrix =
        np.c_[] 

    def remove_vertex(self, vertex: str):
        """
        Deletes a vertex. Drops col and row containing the vertex, 
           then updates the dicts by dropping the i -> v key first, then the i -> v()
        """

    def add_edge(self, edge: tuple):
        """
        Adds an edge. Checks whether the edge is valid, then inserts.
        """
        # Check whether this is a tuple
        if type(edge) is tuple:
           a, b = edge
           # rewrite
           if a not in self.VertexToIndex or b not in self.VertexToIndex:
              raise KeyError(f"Not in the list of verticies")
           self.adjMatrix[a, b] += 1
        else:
           raise TypeError(f"Bad Type: Edge is a {edge}")


    def remove_edge(self, edge: tuple):
        """
        Removes an edge. Throws an error if there is no such edge or 
            there are no such edges (0).
        """
        #try:
        if (self.adjMatrix[edge[0], edge[1]] > 0):
           self.adjMatrix[edge[0], edge[1]] -= 1
           if not self.directed:
              self.adjMatrix[edge[1], edge[0]] -= 1
        
       

    def to_list(self):
        """
        Construct a list based on edges list. O(V^2). 
        """
        raise NotImplemented
        



newGraph = GraphAdj({'a', 'b'}, [('a', 'b',), ('a', 'b')], name = "Example")        
print(newGraph)

newGraph = GraphAdj({'a', 'b', 'c', 'd'}, [('a', 'b',), ('a', 'b'), ('a', 'c'), ('a', 'd')], name = "Example")        
print(newGraph)

# should error out
newGraph = GraphAdj({'a', 'b', 'c'}, [('a', 'b',), ('a', 'b'), ('a', 'c'), ('a', 'd')], name = "Example")        
print(newGraph)

#newGraph.add_vertex("z")
# print(newGraph)
#newGraph.add_edge(("b", "z"))
#print(newGraph)
#newGraph.add_edge(("z", "y")) #errors out on purpose
#newGraph.remove_edge(("a", "b"))
#print(newGraph)
#newGraph.remove_vertex("b")
# newGraph.remove_vertex("p") # key not in set
# print(newGraph)
