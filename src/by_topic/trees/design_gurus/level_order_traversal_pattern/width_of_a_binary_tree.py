"""
https://leetcode.com/problems/maximum-width-of-binary-tree/description/

Given the root of a binary tree, find the maximum width of the tree.

The maximum width is the widest level in the tree.

The width of a level is the number of nodes between the leftmost and rightmost non-null nodes, where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.

You can assume that the result will fit within a 32-bit signed integer.

Input: root = [1, 2, 3, 4, null, null, 5]
       1
      / \
     2   3
    /     \
   4       5
Output: 4
Justification: The maximum width is at the last level between nodes 4 and 5. It counts four positions: [4, null, null, 5].


Input: root = [1, 2, 3, 4, null, 5, 6, null, 7]
       1
     / \
    2   3
   /   / \
  4   5   6
   \
    7
Output: 4
Justification: The maximum width is between nodes 4 and 6 at level 3, counting four positions: [4, null, 5, 6].

Input: root = [1, 2, null, 3, 4, null, null, 5]
      1
     /
    2
   / \
  3   4
     /
    5

Output: 2
Justification: The maximum width is at the third level, between nodes 3 and 4. It counts two positions: [3, 4].

"""