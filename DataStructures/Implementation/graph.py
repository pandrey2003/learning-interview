class Graph:
    def __init__(self):
        self.number_of_nodes = 0
        self.adjacent_list = {}
    
    def add_vertex(self, node):
        self.adjacent_list[node] = []
        self.number_of_nodes += 1

    def add_edge(self, f_node, s_node):
        if self.adjacent_list.get(f_node) is None or self.adjacent_list.get(s_node) is None:
            return "Not added vertex"
        self.adjacent_list[f_node].append(s_node)
        self.adjacent_list[s_node].append(f_node)

    def show_connections(self):
        for vertex, connections in self.adjacent_list.items():
            print(vertex, "-->", connections)


if __name__ == "__main__":
    my_graph = Graph()
    # Adding vertexes
    my_graph.add_vertex(8)
    my_graph.add_vertex(1)
    my_graph.add_vertex(5)
    my_graph.add_vertex(3)
    my_graph.add_vertex(2)
    my_graph.add_vertex(7)
    my_graph.add_vertex(4)
    # Adding edges
    my_graph.add_edge(8, 5)
    my_graph.add_edge(1, 5)
    my_graph.add_edge(1, 8)
    my_graph.add_edge(2, 3)
    my_graph.add_edge(1, 3)
    my_graph.add_edge(7, 3)
    my_graph.add_edge(4, 7)
    # Checking the result
    my_graph.show_connections()
