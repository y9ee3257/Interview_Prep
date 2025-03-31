"""
https://www.geeksforgeeks.org/serialize-deserialize-n-ary-tree/
"""

from collections import deque


# class NAryNode:
#     def __init__(self, val=0, children=None):
#         self.val = val
#         self.children = children if children is not None else []

class Solution:
    """
    for tree
          1
      /  |  |  \
     2   3   4   5
    /|\   |   |\   \
   6 7 8  9  10 11  12
     |       |  |
     13      14 15


the serialization produces output like
1,#,2,3,4,5,#,6,7,8,#,9,#,10,11,#,12,#,#,13,#,#,#,#,#,14,#,15,#,#

# is used as both seperator and also indicate null nodes
    """
    def serialize(self, root):
        q = deque()
        output = []
        if not root: return output
        q.append(root)
        q.append(None)
        while q:
            node = q.popleft()
            if not node:
                output.append("#")
                continue
            output.append(str(node.val))

            for child in node.children:
                q.append(child)
            if not node.children:
                q.append(None)
            q.append(None)

        return ",".join(output)

    """
    deserializing the below string to tree 
    1,#,2,3,4,5,#,6,7,8,#,9,#,10,11,#,12,#,#,13,#,#,#,#,#,14,#,15,#,#
    
    1 -> 2,3,4
    2 -> 6,7,8
    3 -> 9
    4 -> 10,11
    5 -> 12
    6 -> # (empty)
    7 -> 13
    8 -> #
    9 -> #
    10 -> 14
    11 -> 15
    12 -> #
    """
    def deserialize(self, data):
        print(data)
        q = deque()
        arr = data.split(",")
        if len(arr) == 0: return None
        root = NAryNode(arr[0], [])
        if len(arr) <= 2: return root

        q.append(root)
        index = 2

        while q:
            node = q.popleft()
            while index < len(arr) and arr[index] != "#":
                child_node = NAryNode(int(arr[index]), [])
                node.children.append(child_node)
                q.append(child_node)
                index += 1
            index += 1

        return root