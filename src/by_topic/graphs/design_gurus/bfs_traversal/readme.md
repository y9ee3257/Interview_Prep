## Graph Traversal - Breadth First Search (BFS)

Breadth-First Search (BFS) is a graph traversal algorithm that explores a graph's vertices (nodes) level by level. It starts from a selected source node and moves outward to visit all the nodes at the same distance from the source before moving on to nodes at the following distance level.

BFS is particularly useful for finding the shortest path in unweighted graphs and for systematically exploring graphs.

```python
from collections import defaultdict, deque

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adjList = defaultdict(list)

    def addEdge(self, u, v):
        self.adjList[u].append(v)
        self.adjList[v].append(u)  # For undirected graph

    def BFS(self, startVertex):
        visited = [False] * self.V  # To keep track of visited vertices
        q = deque()

        visited[startVertex] = True
        q.append(startVertex)

        while q:
            currentVertex = q.popleft()
            print(currentVertex, end=" ")

            # Explore adjacent vertices
            for neighbor in self.adjList[currentVertex]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    q.append(neighbor)

if __name__ == "__main__":
    graph = Graph(5)  # Create a graph with 6 vertices

    graph.addEdge(0, 1)
    graph.addEdge(0, 2)
    graph.addEdge(0, 3)
    graph.addEdge(1, 2)
    graph.addEdge(2, 4)

    print("Breadth-First Traversal starting from vertex 0:")
    graph.BFS(0)

```

### Problems
1. https://leetcode.com/problems/shortest-path-with-alternating-colors/description/
2. https://leetcode.com/problems/jump-game-iii/description/
3. https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
4. https://leetcode.com/problems/shortest-path-in-binary-matrix/description/
5. https://leetcode.com/problems/word-ladder/description/
6. https://leetcode.com/problems/bus-routes/description/

### Practice Again
1. https://leetcode.com/problems/shortest-path-with-alternating-colors/description/
2. https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
3. https://leetcode.com/problems/bus-routes/description/
