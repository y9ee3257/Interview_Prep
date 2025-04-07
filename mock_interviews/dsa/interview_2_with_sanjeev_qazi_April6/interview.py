'''
/* Given: a binary tree, return a circular doubly linked list ( make the  change in place, ie, reuse existing nodes of the tree )
Assume you are given a Node class that has left, right, and value fields.
class Node {
    Node  left;
    Node  right;
    int   value;
}
		     A
		   /
		  B
		    \
		     C
Output:  B <-> C <-> A  ( A is pointing to B and B is pointing to A ...circular doubly linked list)

            A
		   /
		  B
	     / \
        D   C

Output:  D <-> B <-> C <-> A  ( A is pointing to D and D is pointing to A ...circular doubly linked list)


        A
       /  \
      B    X
     / \
    D   C

       D <-> B <-> C      <-> A <->      X

Output:  D <-> B <-> C      <-> A <->      X  ( X is pointing to D and D is pointing to X ...circular doubly linked list)



A
 helper(Parent(A),currentNode(B), dir(left)):

    current_node.right= parent
    left_node = helper(left, parent)
    right_node = helper(right, parent)

    # pointing to the nodes

    return right_node



    def helper(node, head):
        if not node:
            return


        helper( node.left)

        print(node.val)   first time here is fpr node D, second time here is for node B

        if head is null:
          head = node   head will be B

        node.left = prevNode  # D is the prev node I had visited

        if prevNode:
            prevNode.right = node #  prevNode.right = node

        prevNode = node

        D.right = B   cant really do this
        B.left = D

        helper( node.right)


   head.left = prevNode
   prevNode.right = head

'''


def to_linked_list(root):


    def helper(node, parent, isLeft):
        if not node:
            return

        if isLeft:
            node.right= parent
        else:
            node.left = parent

        left = helper(node.left, node)  # D
        right = helper(node.right,node)  # C



        return node # -D-


    helper(root)



# Did not attempt the second question but asked the interviewer to provide the question, for later practice

# You are given a sorted array consisting of only integers where every element appears exactly twice,
# except for one element which appears exactly once. Find this single element that appears only once.
#  Input: nums = [1,1,2,3,3,4,4,8,8]
#   Output: 2

