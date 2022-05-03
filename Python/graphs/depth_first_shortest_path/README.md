# Finding Shortest Path using Depth First Search

A function that finds the shortest path between two nodes in a graph using depth
first search. If the end node is found, the function returns the length of the
shortest path as an integer and the path to the end node from the starting node
as a list. If the end node is not found, the function returns None.  

## Examples  

### Example 1

![Example 1](https://i.imgur.com/E2Up1Pk.png "Example 1")  

#### Graph Object Input  

- n_nodes = 5  
- edges = [(0,1),(1,2),(2,3),(3,4),(4,0),(1,4),(1,3)]  

#### Input

- graph = Graph(n_nodes, edges)  
- root = 3  
- target = 0  

#### Output

- (2, [3, 1, 0])  

### Example 2

![Example 2](http://www.martinbroadhurst.com/images/connected_components.png "Example 2")  

#### Graph Object Input

- n_nodes = 9  
- edges = [(0, 1), (0, 3), (1, 2), (2, 3), (4, 5), (4, 6), (5, 6), (7, 8)]  

#### Input

- graph = Graph(n_nodes, edges)  
- root = 8  
- target = 2  

#### Output

- None
