## Introduction to Tree Depth Pattern

The Tree Depth Pattern is crucial in binary tree problems where understanding the depth of the tree is key. Depth refers to the number of nodes along the path from the root to the deepest or shallowest leaf. Problems involving depth often require finding the minimum or maximum depth of the tree, which can be important for understanding the tree’s structure, balance, and overall health. Mastering this pattern will help you solve various problems efficiently by focusing on how deep or shallow different parts of the tree are.

To approach these problems, the general strategy involves traversing the tree while keeping track of the depth at each level. There are two common methods:

Breadth-First Search (BFS): This method processes nodes level by level, making it easier to calculate the depth of each level. It's particularly useful for finding the minimum depth of the tree.

Depth-First Search (DFS): This method explores as far as possible along each branch before backtracking. It's often used for calculating the maximum depth and is ideal for a more recursive approach.

By understanding and applying these techniques, you'll be able to handle problems related to tree depth effectively, ensuring that you can identify the key characteristics of the tree structure quickly.

Given a root of the binary tree and node value n, return the depth of the node having value n in the tree. If the node does not exist in the tree, return -1.

Examples
Example 1:
Input: root = [3, 9, 20, null, null, 15, 7], n = 15 <br/>
             3 
            / \
           9  20
              / \
             15  7

Expected Output: 3
Explanation: The node with value 15 is at depth 2.
Example 2:
Input: root = [1, 2, 3, 4, 5, null, null, 8], n = 8 <br/>
            1
           / \
          2   3
         / \
        4   5
       /
      8
Expected Output: 4
Explanation: The node with value 8 is at depth 4.


### Finding a Tree Depth Using the DFS
Here, the goal is to find the depth of a specific node by exploring the tree's structure, starting from the root and moving down each branch. DFS is effective here because it allows us to explore each possible path to the node, ensuring we find the exact depth. By keeping track of the current depth at each level, we can determine the node's position in the tree. This approach is efficient as it only traverses paths that are necessary to find the target node, making it optimal for solving this problem.

```python
# class TreeNode:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None

class Solution:
    def findDepth(self, root, target):
        return self.dfs(root, target, 1)  # Start DFS from root at depth 1

    def dfs(self, node, target, depth):
        # Base case: if node is null, return -1 (target not found)
        if node is None:
            return -1

        # If current node is the target, return current depth
        if node.val == target:
            return depth

        # Recur for the left subtree
        leftDepth = self.dfs(node.left, target, depth + 1)
        if leftDepth != -1:
            return leftDepth  # Target found in left subtree

        # Recur for the right subtree if not found in left
        return self.dfs(node.right, target, depth + 1)  # Check right subtree
```
### Complexity Analysis
Time Complexity: The time complexity of the DFS approach in this problem is , where N is the number of nodes in the binary tree. This is because, in the worst case, we may need to explore all nodes to find the target node, especially if the node is located deep in the tree.

Space Complexity: The space complexity is , where H is the height of the binary tree. This space is required for the call stack due to the recursive nature of DFS. In the worst case, the height of the tree could be equal to the number of nodes (in a skewed tree), making the space complexity .


### Finding a Tree Depth Using the BFS
The BFS also is ideal for this type of problem because it explores the tree level by level, making it well-suited for finding the shortest path or depth in a binary tree. By processing all nodes at one depth level before moving to the next, BFS ensures that we find the target node at the shallowest possible depth, if it exists. This approach is effective because it avoids unnecessary deep exploration and directly focuses on the level where the target node resides. Additionally, BFS naturally handles the traversal in a way that keeps track of the depth, making it easy to return the correct depth as soon as the target node is found.

```python
from collections import deque

# TreeNode class in Python
# class TreeNode:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None

class Solution:
    
    # BFS method to find the depth of a given node value
    def findDepth(self, root, target):
        # If the tree is empty, return -1
        if root is None:
            return -1

        # Initialize a queue to store nodes along with their depth
        queue = deque([root])
        depth = 1  # Start from depth 1

        # Perform BFS traversal
        while queue:
            levelSize = len(queue)  # Number of nodes at the current depth level

            # Process all nodes at the current level
            for i in range(levelSize):
                currentNode = queue.popleft()

                # If the current node matches the target, return the current depth
                if currentNode.val == target:
                    return depth

                # Add left and right children to the queue, if they exist
                if currentNode.left is not None:
                    queue.append(currentNode.left)
                if currentNode.right is not None:
                    queue.append(currentNode.right)

            # Increment depth as we move to the next level
            depth += 1

        # If the target node is not found, return -1
        return -1

```


### Complexity Analysis:
Time Complexity: The time complexity of the BFS approach in this problem is O(N), where N is the number of nodes in the binary tree. In the worst case, we might need to traverse all nodes to find the target node, particularly if the target is located at the last level of the tree.

Space Complexity: The space complexity is O(W), where W is the maximum width of the tree. This is because BFS requires storing nodes in a queue, and the maximum space needed occurs when the largest number of nodes are at a single level. In a balanced binary tree, this would be around O(N/2) == O(N), but generally, we refer to it as O(N).


### Problems
1. https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
2. https://leetcode.com/problems/minimum-depth-of-binary-tree/
3. https://www.geeksforgeeks.org/how-to-determine-if-a-binary-tree-is-balanced/
4. https://leetcode.com/problems/diameter-of-binary-tree/description/
5. https://leetcode.com/problems/maximum-depth-of-n-ary-tree/description/
