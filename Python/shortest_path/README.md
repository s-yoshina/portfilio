# Shortest Path in a Graph
A program where the user can find the shortest path between a start point (root)
and an end point (target) in a graph. The program returns the total weight (distance) and
the path of the shortest path as an integer and a list, respectively, in a tuple.
If there is no path connecting the starting point and the end point, the program
returns None. The algorithms used to find the shortest path is breadth-first search
and Dijkstra's algorithm for an unweighted and weighted path, respectively.
** The function to find the shortest path will not accept a graph with a node that
has a value greater than or equal to the number of nodes in the graph or less than 0.

## Examples
### Example 1
<Graph Object Input>
num_nodes = 9
edges = [(0, 1, 3), (0, 3, 2), (0, 8, 4), (1, 7, 4), (2, 7, 2), (2, 3, 6),
          (2, 5, 1), (3, 4, 1), (4, 8, 8), (5, 6, 8)]

Graph Image: https://i.imgur.com/wy7ZHRW.png
<input>
graph = Graph(n_nodes, edges)
root = 8
target = 7
<output>
(11, [8, 7, 1, 0])

### Example 2
<Graph Object Input>
n_nodes = 5
edges = [(0,1),(1,2),(2,3),(3,4),(4,0),(1,4),(1,3)]

Graph Image: https://i.imgur.com/E2Up1Pk.png
<input>
graph = Graph(n_nodes, edges)
root = 0
target = 2
<output>
(2, [0, 1, 2])

### Example 3
<Graph Object Input>
n_nodes = 9
edges = [(0, 1), (0, 3), (1, 2), (2, 3), (4, 5), (4, 6), (5, 6), (7, 8)]

Graph image: http://www.martinbroadhurst.com/images/connected_components.png
<input>
graph = Graph(n_nodes, edges)
root = 3
target = 5
<output>
None
