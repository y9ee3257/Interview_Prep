## Introduction to Root to Leaf Path Pattern

The Root to Leaf Path Pattern is fundamental when dealing with binary trees. This pattern focuses on problems that involve navigating from the root of the tree to its leaves, where each leaf represents a node without children. Understanding this pattern is crucial because many binary tree problems require operations that focus on these paths. For instance, tasks like finding the sum of all left leaves or determining specific paths that meet a given condition rely heavily on this approach. Mastering this pattern allows you to handle a wide variety of problems involving tree traversal and leaf node operations.

In this pattern, the general approach involves recursive traversal of the binary tree, where you explore each possible path from the root to the leaf nodes. During the traversal, you can perform specific operations, such as accumulating sums, validating path properties, or collecting nodes. The key is to ensure that you correctly identify and process each path leading to a leaf, as the operations often depend on the properties of these paths.

Problem Statement
Given a binary tree where each node contains an integer, return the maximum sum obtained by following any path from the root node to a leaf node.

The path must start at the root and end at a leaf.

```python
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.maxSum = float('-inf')

    def maxPathSum(self, root):
        # Initialize maxSum to the smallest possible value
        self.maxSum = float('-inf')

        # Start the recursive process to find the maximum sum
        self.findMaxSum(root, 0)
        return self.maxSum

    def findMaxSum(self, node, currentSum):
        # Base case: if the current node is null, return immediately
        if node is None:
            return

        # Add the current node's value to the current path sum
        currentSum += node.val

        # Check if the current node is a leaf
        if node.left is None and node.right is None:
            # Update maxSum if the current path sum is greater
            self.maxSum = max(self.maxSum, currentSum)

        # Recursively process the left and right subtrees
        self.findMaxSum(node.left, currentSum)
        self.findMaxSum(node.right, currentSum)

```

### Time Complexity
The time complexity of the algorithm is , where N is the number of nodes in the binary tree.

The algorithm uses a depth-first search (DFS) traversal to explore each node in the tree exactly once. In the worst case, every node from the root to the leaf must be visited, which results in linear time complexity relative to the number of nodes.
### Space Complexity
The space complexity of the algorithm is O(H), where H is the height of the binary tree.

The space complexity is primarily determined by the recursive call stack. In the worst-case scenario (e.g., a skewed tree), the height of the tree could be N (when the tree is a straight line). However, for a balanced tree, the height is log(N). Thus, in the worst case, the space complexity is O(N), but for a balanced tree, it is O(logN).


## Problems
1. https://leetcode.com/problems/sum-root-to-leaf-numbers/description/
2. https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/description/
3. https://leetcode.com/problems/insufficient-nodes-in-root-to-leaf-paths/description/
4. https://leetcode.com/problems/smallest-string-starting-from-leaf/description/
5. https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/description/
6. https://leetcode.com/problems/path-sum-ii/description/
7. https://leetcode.com/problems/sum-root-to-leaf-numbers/description/
8. https://www.geeksforgeeks.org/check-root-leaf-path-given-sequence/
9. https://leetcode.com/problems/path-sum-iii/description/
