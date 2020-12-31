class Vertex:

    def __init__(self, name):
        self.name = name
        self.neighbours = set()

    def add_neighbour(self, vertex_name):
        self.neighbours.add(vertex_name)


class Graph:

    vertices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            self.vertices[u].add_neighbour(v)
            self.vertices[v].add_neighbour(u)
            return True
        else:
            return False

    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key, sorted(list(self.vertices[key].neighbours)))


if __name__ == '__main__':
    graph = Graph()
    a = Vertex('A')
    graph.add_vertex(a)
    graph.add_vertex(Vertex('B'))

    for i in range(ord('A'), ord('L')):
        graph.add_vertex(Vertex(chr(i)))

    edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'EH', 'FB', 'FK', 'GA', 'GB', 'HI', 'JK', 'KA']
    for edge in edges:
        graph.add_edge(edge[0], edge[1])

    graph.print_graph()
