## Introduction to Comparison of Two Trees Pattern

In binary tree coding, the Comparison of Two Trees Pattern involves determining if two trees have the same structure and values at corresponding positions. This pattern is crucial in problems where we need to verify if two binary trees are identical or symmetrical. Understanding how to compare each node in both trees helps in solving a wide range of problems, especially those that deal with equality checks between tree structures.

To solve problems based on this pattern, the approach generally involves traversing both trees simultaneously. At each step, the algorithm compares the nodes from both trees. If the nodes are equal, the process continues to their respective child nodes. Recursive methods are commonly used for this traversal. If any mismatch occurs between nodes or tree structures, the trees are considered different. This method is efficient and straightforward, making it a solid approach to tackle tree comparison problems.


Problem Statement
Given the roots of two binary trees, root1 and root2, check if these two binary trees are exactly the same.

Two binary trees are considered the same if they have the same structure and the corresponding nodes hold the same values. If both trees are identical, return true, otherwise, return false.

Examples
Example 1
Input: root1 = [4, 5, 6, null, 7, 8], root2 = [4, 5, 6, null, 7, 8]
Expected Output: true
Justification: Both arrays represent trees with the same structure, and all corresponding values are equal, so the trees are identical.

Example 2:
Input: root1 = [3, null, 7], root2 = [3, null, 8]
Expected Output: false
Justification: Even though the structure is the same, the value at the left child of the root is different (7 in root1, 8 in root2), so the trees are not identical.

We can compare two trees using DFS (Depth-first search) or BFS (Breadth-first search) traversal. Let's learn both approaches.

### Using the DFS Approach
The algorithm compares two binary trees using Depth First Search (DFS) by recursively checking if both trees are identical. The process starts at the root nodes of both trees and compares their values. If both nodes are null, the trees are identical at that point. If one node is null and the other is not, the trees are not the same. The algorithm then recursively compares the left and right subtrees. If all corresponding nodes in both trees have the same value and structure, the trees are considered identical; otherwise, they are not.

```python
# Definition for a binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # DFS function to compare two trees
    def isSameTree(self, root1, root2):
        # If both nodes are null, they are identical at this point
        if root1 is None and root2 is None:
            return True
        
        # If one of the nodes is null, they are not the same
        if root1 is None or root2 is None:
            return False

        # If values of the current nodes are different, trees are not identical
        if root1.val != root2.val:
            return False

        # Recursively check the left and right subtrees using DFS
        return self.isSameTree(root1.left, root2.left) and self.isSameTree(root1.right, root2.right)
```

Complexity Analysis
Time Complexity: The algorithm visits each node in both trees exactly once, performing constant-time operations (such as value comparison) at each node. Therefore, if n is the number of nodes in each tree, the time complexity is O(N) . This complexity applies because, in the worst case, all nodes must be compared.

Space Complexity: The space complexity depends on the depth of the recursion stack. In the worst case (when the trees are skewed), the depth of recursion can go up to n (the number of nodes), resulting in O(N) space complexity. In the best case (balanced trees), the space complexity is O(logN) due to the recursion stack being proportional to the height of the tree.


### Using the BFS Approach
The algorithm uses Breadth First Search (BFS) to check whether two binary trees are identical. It leverages two queues to store nodes from both trees. The algorithm starts by adding the root nodes of both trees to their respective queues. Then, it iteratively processes the nodes level by level. For each node pair, it checks if both nodes are null (skip comparison), if one is null and the other isn't (the trees are different), or if their values differ (the trees are different). If both node values are the same, their left and right children are added to the respective queues for further comparison. The algorithm continues this process until both queues are empty. If both queues are empty at the same time, the trees are identical; otherwise, they are not.

```python
from collections import deque

# Definition for a binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # BFS function to compare two trees
    def isSameTree(self, root1, root2):
        # Use a queue to store nodes for level-order traversal
        queue1 = deque()
        queue2 = deque()
        
        # Add root nodes of both trees to respective queues
        queue1.append(root1)
        queue2.append(root2)
        
        # Loop until both queues are empty
        while queue1 and queue2:
            node1 = queue1.popleft()
            node2 = queue2.popleft()
            
            # If both nodes are null, continue to next iteration
            if not node1 and not node2:
                continue
            
            # If one of the nodes is null, trees are not the same
            if not node1 or not node2:
                return False
            
            # If the node values are different, trees are not identical
            if node1.val != node2.val:
                return False
            
            # Add left and right children of both nodes to respective queues
            queue1.append(node1.left)
            queue1.append(node1.right)
            queue2.append(node2.left)
            queue2.append(node2.right)
        
        # If both queues are empty at the same time, trees are identical
        return len(queue1) == 0 and len(queue2) == 0
```

Complexity Analysis
Time Complexity: The algorithm traverses each node in both trees exactly once. For n nodes in each tree, the time complexity is O(N), as we need to compare every node in both trees.

Space Complexity: The space complexity depends on the width of the tree. In the worst case (a perfectly balanced tree), the space complexity is O(N) due to the queues storing nodes at the current level of the tree.


### Problems
1. https://leetcode.com/problems/symmetric-tree/description/
2. https://leetcode.com/problems/subtree-of-another-tree/description/
3. https://www.geeksforgeeks.org/tree-isomorphism-problem/

### Practice Again
1. https://leetcode.com/problems/subtree-of-another-tree/description/
2. https://www.geeksforgeeks.org/tree-isomorphism-problem/
