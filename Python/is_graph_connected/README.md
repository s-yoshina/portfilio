
# Checking whether a Graph has Continuous Connection

A function that allows the user to check whether all the nodes in a graph are
accessible from each other. A Boolean value is returned by the function: True if all
nodes are connected, False if all nodes are not connected. The algorithm used to
solve this problem is breadth-first search. The graph object used in this function
represents a graph using an adjacency list.

## Examples  

### Example 1   

![Example 1 Graph](https://i.imgur.com/E2Up1Pk.png "Example 1")

#### Graph object inputs  

- n_nodes = 5  
- edges = [(0,1),(1,2),(2,3),(3,4),(4,0),(1,4),(1,3)]

#### Input   

- graph = Graph(n_nodes, edges)  

#### Output

- True  

### Example 2

![Example 2 Graph](http://www.martinbroadhurst.com/images/connected_components.png "Example 2")  

#### Graph object input

- n_nodes = 9  
- edges = [(0, 1), (0, 3), (1, 2), (2, 3), (4, 5), (4, 6), (5, 6), (7, 8)]  

#### Input

- graph = Graph(n_nodes, edges)  

#### Output

- False  

#### Example 3

![Example 3 Graph](https://tutorialspoint.dev/image/cycleGraph.png "Example 3")  

#### Graph object input

- n_nodes = 5  
- edges = [(1,2),(2,0),(1,0),(0,3),(3,4)]  

####  Input

- graph = Graph(n_nodes, edges)  

#### Output

- True  
