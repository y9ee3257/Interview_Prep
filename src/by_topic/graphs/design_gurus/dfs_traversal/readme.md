## Graph Traversal - Depth First Search(DFS)

Graphs are made up of nodes (vertices) connected by edges. Traversing a graph means visiting all its nodes in a structured way. This helps solve problems like finding paths, detecting cycles, and searching for specific values.

Two widely used traversal techniques are:

Depth-First Search (DFS): Explores as far as possible along each branch before backtracking.
Breadth-First Search (BFS): Explores all neighbors of a node before moving deeper.

### Depth First Search(DFS) Using a Recursive Approach
In the recursive approach, the function calls itself to traverse adjacent nodes, mimicking the natural depth-first behavior of the algorithm. This approach leverages the function call stack to manage backtracking, simplifying the implementation.

In recursive DFS, each node is visited once, and its unvisited neighbors are recursively explored. The recursion ends when all reachable nodes have been visited. A visited array is used to ensure nodes are not revisited, preventing infinite loops in cyclic graphs.

```python

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices  # Number of vertices
        self.adjacencyList = [[] for _ in range(vertices)]  # Adjacency list

    # Method to add an edge to the graph
    def addEdge(self, source, destination):
        self.adjacencyList[source].append(destination)
        self.adjacencyList[destination].append(source)  # For an undirected graph

    # Method to perform DFS using recursion
    def DFS(self, startVertex):
        visited = [False] * self.vertices  # Track visited nodes
        print("DFS Traversal: ", end="")
        self.DFSRecursive(startVertex, visited)  # Start DFS from the given vertex

    def DFSRecursive(self, currentVertex, visited):
        visited[currentVertex] = True  # Mark the current node as visited
        print(currentVertex, end=" ")  # Process the current node

        # Recur for all unvisited neighbors
        for neighbor in self.adjacencyList[currentVertex]:
            if not visited[neighbor]:
                self.DFSRecursive(neighbor, visited)


class Solution:
    @staticmethod
    def main():
        g = Graph(5)

        g.addEdge(0, 3)
        g.addEdge(0, 2)
        g.addEdge(0, 1)
        g.addEdge(1, 2)
        g.addEdge(2, 4)

        print("DFS Traversal starting from vertex 0: ", end="")
        g.DFS(0)


Solution.main()

```

### Problems
1. 