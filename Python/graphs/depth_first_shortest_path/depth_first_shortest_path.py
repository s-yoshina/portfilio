class Graph:
    def __init__(self, n_nodes:int, edges:list, directed=False):
        self.check_n_nodes_validity(n_nodes)
        self.check_edges_validity(edges)
        self.n_nodes = n_nodes
        self.directed = directed
        self.weighted = True if len(edges[0]) == 3 else False
        self.initialize_weights(edges)
        self.adj_list = [[] for _ in range(n_nodes)]
        self.add_edges(edges)

    def check_n_nodes_validity(self, n_nodes:int):
        if not isinstance(n_nodes, int):
            raise TypeError("n_nodes is not an integer value.")
        if n_nodes <= 0:
            raise ValueError("n_nodes is not a value greater than 0")

    def check_edges_validity(self, edges:list):
        if not isinstance(edges, list):
            raise TypeError("edges is not a list.")
        if len(edges) == 0:
            raise ValueError("edges is a list with no elements")

    def initialize_weights(self, edges:list):
        if self.weighted:
            self.weights = [[] for _ in range(n_nodes)]
        else:
            self.weights = None

    def check_edge_validity(self, edge:list):
        if not (isinstance(edge, tuple) or isinstance(edge,list)):
            raise TypeError("Edges contains an elements that is not a tuple nor a list")
        # Checking the number of elements in an edge
        if ((self.weighted and len(edge) != 3) or
            (not self.weighted and len(edge) != 2)):
            raise ValueError("An edge has too many or too few elements")

        # Checking the nodes of an edge
        if not (isinstance(edge[0], int) and isinstance(edge[1], int)):
            raise TypeError("A node(s) in an edge are not integer values")
        if edge[0] < 0 or edge[1] < 0:
            raise ValueError("A node has to be a value greater than or equal to 0")

        # Checking the weight if the graph is weighted
        if self.weighted:
            if not (isinstance(edge[2], int) or isinstance(edge[2], float)):
                raise TypeError("The weight of an edge needs to be a float or an integer value.")
            if edge[2] < 0:
                raise ValueError("The weight of an edge cannot be a negative value.")

    def add_edges(self, edges:list):
        for edge in edges:
            self.check_edge_validity(edge)
            node1, node2 = edge[0], edge[1]
            if self.weighted:
                weight = edge[2]

            self.adj_list[node1].append(node2)
            if not self.directed:
                self.adj_list[node2].append(node1)
            if self.weighted:
                self.weights[node1].append(weight)
                if not self.directed:
                    self.weights[node2].append(weight)

    def __repr__(self):
        result = ""
        if self.weighted:
            for i, (nodes, weights) in enumerate(zip(self.adj_list, self.weights)):
                result += f"{i}:{list(zip(nodes,weights))}"
                if i != len(self.adj_list)-1:
                    result += "\n"
        else:
            result = "\n".join([f"{i}:{l}" for i, l in enumerate(self.adj_list)])
        return result

    def __str__(self):
        return self.__repr__()

def check_args_validity(graph:Graph, root:int, target:int):
    if (not isinstance(graph, Graph) or
        not isinstance(root, int) or
        not isinstance(target, int)):
        raise TypeError
    if root < 0 or target < 0:
        raise ValueError("The root node or the target node is a value less than 0")
    if root > graph.n_nodes or target >= graph.n_nodes:
        raise ValueError("The target node or the root node cannot be a value greater than or equal to the number of nodes.")

def return_shortest_path(parents:list, root:int, target:int) -> list:
    current_node = target
    path = [current_node]
    while current_node is not root:
        if current_node is None:
            return None
        current_node = parents[current_node]
        path.append(current_node)
    return path[::-1]

def find_shortest_path(graph:Graph, root:int, target:int) -> (int, list):
    check_args_validity(graph, root, target)
    stack = []
    visited = [False]*len(graph.adj_list)
    parents = [None]*len(graph.adj_list)
    stack.append(root)
    while stack != []:
        current_node = stack.pop()
        if current_node == target:
            shortest_path = return_shortest_path(parents, root, target)
            return len(shortest_path)-1, shortest_path
        if not visited[current_node]:
            visited[current_node] = True
            for node in graph.adj_list[current_node]:
                if parents[node] is None:
                    parents[node] = current_node
                stack.append(node)
    return None
