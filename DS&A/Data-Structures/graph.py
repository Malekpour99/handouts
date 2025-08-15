# Graph (G) consists of Vertices (V : Vertex) & Edges (E)
# Degree = Number of edges connected to a vertex
# Number of edges = total degrees / 2
# Complete Graph = An undirected graph including all edges (Kn)
# Degree of a vertex in a full graph (K) = n - 1
# Total degree of a Kn = n * (n - 1)
# Number of edges in Kn = n * (n - 1) / 2

# A vertex without input: source
# A vertex without output: well


class GraphMatrix:
    def __init__(self, n: int):
        """
        Creating an undirected graph with n vertices
        and adjacency matrix
        """
        self.size = n
        self.M = []
        for _ in range(n):
            self.M.append([0 for _2 in range(n)])
            # self.M.append([0] * n for i in range(n))

    def add_edge(self, v1, v2):
        "Adding edges to the undirected graph matrix"
        self.M[v1][v2] = 1
        self.M[v2][v1] = 1

    def remove_edge(self, v1, v2):
        "Removing edges from the undirected graph matrix"
        self.M[v1][v2] = 0
        self.M[v2][v1] = 0

    def print_matrix(self):
        "printing graph adjacency matrix in a structured and readable way"
        for row in self.M:
            for edge in row:
                print(edge, end=" ")
            print()


g = GraphMatrix(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.print_matrix()
print("--------------------------------------")


class Node:
    def __init__(self, data):
        "Creating an adjacency list node"
        self.vertex = data
        self.next = None


class GraphNode:
    def __init__(self, n):
        "Creating a graph using adjacency list"
        self.V = n
        self.graph = [None] * self.V

    def add_edge(self, source, data):
        "Adding edge to the graph"
        n = Node(data)
        n.next = self.graph[source]
        self.graph[source] = n
        m = Node(source)
        m.next = self.graph[data]
        self.graph[data] = m

    def print_list(self):
        "printing graph adjacency list in a structured and readable way"
        for i in range(self.V):
            print(i, ": head", end=" ")
            t = self.graph[i]
            while t:
                print("->  {}".format(t.vertex), end=" ")
                t = t.next
            print()


g2 = GraphNode(5)
g2.add_edge(0, 1)
g2.add_edge(0, 4)
g2.add_edge(1, 2)
g2.add_edge(1, 3)
g2.add_edge(1, 4)
g2.add_edge(2, 3)
g2.add_edge(3, 4)
g2.print_list()
