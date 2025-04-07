"""
All the below questions are actual Meta Interview Questions

https://codebunk.com/b/3501100707405/

Given a binary tree, imagine yourself standing on the top side of it,
return the values of the nodes you can see ordered from left to right.

If multiple nodes are in the same column, only record the lowest level. (or higher node)

Example 1:

 | | | |
 | | | |
 V V V V
   3
  /\
 /  \
 9  20
    /\
   /  \
  15   7

Output: [9, 3, 20, 7]

"""

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right =right


from collections import deque

def top_view(tree: TreeNode):
    if not tree:
        return []

    q = deque([(tree, 0)])
    col_map = {} # {1:5, -1:3, -2:2...}
    min_col, max_col = float("inf"), float("-inf")

    while q:
        node, level = q.popleft()
        min_col = min(level,min_col)
        max_col = max(level,max_col)

        if level not in col_map:
            col_map[level] = node.val

        if node.left:
            q.append((node.left, level-1))

        if node.right:
            q.append((node.right, level+1))


    output = []
    for i in range(min_col, max_col+1):
        output.append(col_map[i])


    return output




"""
Given a binary tree, determine if it is a complete binary tree.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

        1
       / \
      2   3
     / \  /
    4   5 6     [1,2,3,4,5,6]

        1
       /       [1, 2 ,null ,5]
      2   
     /   
    5           [1,2,3,5,null,7,8,null,null]

        1
       / \
      2   3   [1,2,3,5]
     /   
    5  

"""
from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def complete_binary_tree(root: TreeNode):
    if not root:
        return True

    q = deque([root])

    output = []
    while q:
        node = q.popleft()

        output.append(node.val if node else None)

        if node:
            q.append(node.left)
            q.append(node.right)

    # [1,2,3,4,5]

    while output[-1] == None:
        output.pop()

    for node in output:
        if not node:
            return False

    return True

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)

## print(complete_binary_tree(root))





"""
Given a sorted array of integers with duplicates, count the number of unique values.

Input:
{4,5,8}

444588

444444444444444444555555555555555555555555555557778888888888888888888888888888999999999999999

klog(n)

Output:
3

(Explanation: there are 3 distinct values: 4, 5, 8)

Assume that the number of unique elements, K, is much less than the size of the array, N
e.g. K = O(log N)
     K = O(sqrt (sqrt(N)))
"""

def find_unique(arr):
    if not arr:
        return 0

    def binary_search(num, start, end):
        mid = start + (end - start) // 2

        # 44444444444444444 4 5 5555555555555555555555555557778888888888888888888888888888999999999999999
        if start == end:
            return len(arr)

        if arr[mid] == num and arr[mid + 1] > num:
            return mid + 1
        if arr[mid] > num and arr[mid - 1] == num:
            return mid

        if arr[mid] == num:
            return binary_search(num, mid + 1, end)
        else:
            return binary_search(num, start, mid - 1)

    current_index = 0
    output = 0
    while current_index < len(arr):
        output += 1
        current_index = binary_search(arr[current_index], current_index, len(arr))

    return output

print(find_unique([4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6]))
