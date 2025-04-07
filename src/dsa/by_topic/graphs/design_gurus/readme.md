### Common Graph Terminologies

| Concept                      | Description                                                                                       |
|:-----------------------------|:--------------------------------------------------------------------------------------------------|
| **Graph**                    | A structure consisting of a set of vertices (nodes) and a set of edges connecting these vertices. |
| **Vertex (Node)**            | A fundamental unit in a graph.                                                                    |
| **Edge**                     | A connection between two vertices.                                                                |
| **Directed Graph (Digraph)** | A graph where edges have a direction.                                                             |
| **Undirected Graph**         | A graph where edges have no direction.                                                            |
| **Weighted Graph**           | A graph where edges have associated values (weights).                                             |
| **Path**                     | A sequence of vertices connected by edges.                                                        |
| **Cycle**                    | A path that starts and ends at the same vertex.                                                   |
| **Connected Graph**          | A graph where there is a path between every pair of vertices.                                     |
| **Disconnected Graph**       | A graph with at least two vertices that are not connected by a path.                              |
| **Tree**                     | A connected graph with no cycles.                                                                 |
| **Degree (of a Vertex)**     | The number of edges connected to a vertex.                                                        |
| **Adjacent Vertices**        | Vertices that are connected by an edge.                                                           |
| **Loop**                     | An edge that connects a vertex to itself.                                                         |
| **In-Degree (of a Vertex)**  | The number of edges pointing *to* a vertex (in a directed graph).                                 |
| **Out-Degree (of a Vertex)** | The number of edges pointing *from* a vertex (in a directed graph).                               |
| **Cyclic Graph**             | A graph that contains at least one cycle.                                                         |
| **Acyclic Graph**            | A graph that contains no cycles.                                                                  |

# Graph Representation: Adjacency Matrix vs. Adjacency List

## Graph Visualization

Let’s consider both an **undirected** and a **directed** graph with 5 vertices: **A, B, C, D, E**.

### **Undirected Graph**

Edges:

- A — B
- A — C
- B — C
- B — D
- C — E
- D — E

```
    A
   / \
  B---C
  |   |
  D---E
```

### **Directed Graph**

Edges (direction matters):

- A → B
- A → C
- B → E
- B → D
- C → E

```
    A → B → D
    ↓   ↓
    C → E
```

---

## 1. Adjacency Matrix Representation

### **Undirected Graph Matrix**

|   | A | B | C | D | E |
|---|---|---|---|---|---|
| A | 0 | 1 | 1 | 0 | 0 |
| B | 1 | 0 | 1 | 1 | 0 |
| C | 1 | 1 | 0 | 0 | 1 |
| D | 0 | 1 | 0 | 0 | 1 |
| E | 0 | 0 | 1 | 1 | 0 |

### **Directed Graph Matrix**

|   | A | B | C | D | E |
|---|---|---|---|---|---|
| A | 0 | 1 | 1 | 0 | 0 |
| B | 0 | 0 | 0 | 1 | 1 |
| C | 0 | 0 | 0 | 0 | 1 |
| D | 0 | 0 | 0 | 0 | 0 |
| E | 0 | 0 | 0 | 0 | 0 |

### Explanation

- **0** means no edge between the vertices.
- **1** means an edge exists between the vertices.
- The **undirected graph matrix** is symmetric.
- The **directed graph matrix** is asymmetric (edges have direction).

---

## 2. Adjacency List Representation

For the same examples

### **Undirected Graph List**
```
    A
   / \
  B---C
  |   |
  D---E
```

```
A → B, C  
B → A, C, D  
C → A, B, E  
D → B, E  
E → C, D  
```


### **Directed Graph List**
```
    A → B → D
    ↓   ↓
    C → E
```

```
A → B, C  
B → E, D  
C → E  
D → (none) 
E → (none)  
```

Each vertex maintains a list of its adjacent vertices.

---

## Comparison of Representations

| Representation       | Space Complexity | Best Use Case               |
|----------------------|------------------|-----------------------------|
| **Adjacency Matrix** | O(V²)            | Dense graphs (many edges)   |
| **Adjacency List**   | O(V + E)         | Sparse graphs (fewer edges) |

### Key Differences

- **Adjacency Matrix** is faster for edge lookups (O(1)) but consumes more space for sparse graphs.
- **Adjacency List** is space-efficient and better for graphs with fewer edges.


