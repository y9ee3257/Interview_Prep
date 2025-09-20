# Understanding Greedy Algorithm

A **Greedy algorithm** is used to solve problems in which the best choice is made at each step, and it finds a solution in a minimal step. This approach assumes that choosing a local optimum at each stage will lead to the determination of a global optimum. It's like making the most beneficial decision at every crossroad, hoping it leads to the ultimate destination efficiently.

---

## Purpose of Greedy Algorithm

The main goal of a greedy algorithm is to solve complex problems by breaking them down into simpler subproblems, solving each one optimally to find a solution that is as close as possible to the overall optimum. It's particularly useful in scenarios where the problem exhibits the properties of **greedy choice** and **optimal substructure**.

---

## Properties for Greedy Algorithm Suitability

- **Greedy Choice Property**:  
  The local optimal choices lead to a global optimum, meaning the best solution in each small step leads to the best overall solution.

- **Optimal Substructure**:  
  A problem has an optimal substructure if an optimal solution to the entire problem contains the optimal solutions to its subproblems.

---

## Characteristics of Greedy Method

- **Local Optimization**:  
  At every step, the algorithm makes a choice that seems the best at that moment, aiming for local optimality.

- **Irrevocability**:  
  Once a choice is made, it cannot be undone or revisited. This is a key characteristic that differentiates greedy methods from dynamic programming, where decisions can be re-evaluated.

---

## Components of Greedy Algorithm

- **Candidate Set**:  
  The set of choices available at each step.

- **Selection Function**:  
  Helps in choosing the most promising candidate to be added to the current solution.

- **Feasibility Function**:  
  Checks if a candidate can be used to contribute to a solution without violating problem constraints.

- **Objective Function**:  
  Evaluates the value or quality of the solution at each step.

- **Solution Function**:  
  Determines if a complete solution has been reached.

---

## Simplified Greedy Algorithm Process

1. **Start with an Empty Solution Set**:  
   The algorithm begins with no items in the solution set.

2. **Iterative Item Selection**:  
   In each step, choose the most suitable item based on the current goal.

3. **Add Item to Solution Set**:  
   The selected item is added to the solution set.

4. **Feasibility Check**:  
   Determine if the solution set with the new item still meets the problem's constraints.

5. **Accept or Reject the Item**:
    - If **Feasible**: Keep the item in the solution set.
    - If **Not Feasible**: Remove and permanently discard the item.

6. **Repeat Until Complete**:  
   Continue this process until a full solution is formed or no feasible solution can be found.

7. **Assess Final Solution**:  
   Evaluate the completed solution set against the problem's objectives.

---

## Let's Understand the Greedy Algorithm via the Example Below

### Problem Statement (Boats to Save People)

We are given an array `people` where each element `people[i]` represents the weight of the i-th person. There is also a weight limit for each boat. Each boat can carry at most two people at a time, but the combined weight of these two people must not exceed `limit`. The objective is to determine the minimum number of boats required to carry all the people.

---

### Example

```text
Input: people = [10, 55, 70, 20, 90, 85], limit = 100  
Output: 4

Explanation: One way to transport all people using 4 boats is as follows:
- Boat 1: Carry people with weights 10 and 90 (total weight = 100).
- Boat 2: Carry a person with weight 85 (total weight = 85).
- Boat 3: Carry people with weights 20 and 70 (total weight = 90).
- Boat 4: Carry a person with weight 55 (total weight = 55).
```

# Pros of Greedy Approach

- **Efficiency in Time and Space**:  
  Greedy algorithms often have lower time and space complexities, making them fast and memory-efficient.

- **Ease of Implementation**:  
  They are generally simpler and more straightforward to code than other complex algorithms.

- **Optimal for Certain Problems**:  
  In problems with certain structures, like those with greedy-choice property and optimal substructure, greedy algorithms guarantee an optimal solution.

- **Useful for Approximations**:  
  When an exact solution is not feasible, greedy algorithms can provide a close approximation quickly.

---

# Cons of Greedy Approach with Example

- **Not Always Optimal**:  
  Greedy algorithms do not always yield the global optimum solution, especially in problems lacking a greedy-choice property.

- **Shortsighted Approach**:  
  They make decisions based only on current information, without considering the overall problem.


# Standard Greedy Algorithms

- **Kruskal’s Minimum Spanning Tree Algorithm**  
  Builds a minimum spanning tree by adding the shortest edge that doesn’t form a cycle.

- **Prim’s Minimum Spanning Tree Algorithm**  
  Grows a minimum spanning tree from a starting vertex by adding the nearest vertex.

- **Dijkstra’s Shortest Path Algorithm**  
  Finds the shortest path from a single source to all other vertices in a weighted graph.

- **Huffman Coding**  
  Used for data compression, it builds a binary tree with minimum weighted path lengths for given characters.

- **Fractional Knapsack Problem**  
  Maximizes the total value of items in a knapsack without exceeding its capacity.

- **Activity Selection Problem**  
  Selects the maximum number of activities that don't overlap in time.

- **Greedy Best-First Search**  
  Used in AI for pathfinding and graph traversal, prioritizing paths that seem closest to the goal.


