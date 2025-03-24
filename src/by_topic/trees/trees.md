https://docs.google.com/document/d/1zO6GGD39gIx9a2Q32swY3NfCXHCWfFrOaX2i_lylz1c/edit


```python
"""
Standard Template for BFS 
Prefer iterative over recursive for BFS to avoid extra space for call stack
"""
# level order traversal of a tree 
from collections import deque

q = deque()
q.append(root)
output = []
while len(q) > 0:
   row_size = len(q)
   row = []
   for i in range(row_size):
      node = q.popleft()
      row.append(node.value)

      if node.left:
         q.append(node.left)
      if node.right:
         q.append(node.right)
   output.append(row)

return output
```

1. making minor mistakes not considering edge cases, below are examples
   1. is bst
   2. single value tree
   3. symmetric tree
   
2. do all the above problems without using a global variable, use recursion to return answer.


### Practice Again:
1. Symmetric Tree
2. Flip upside down 
3. vertical order traversal
4. 


