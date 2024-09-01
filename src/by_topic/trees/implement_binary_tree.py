class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value

    def leftI(self, left):
        self.left = left

    def rightI(self, right):
        self.right = right

    def value(self, value):
        self.value = value

    def print(self):
        print(self.value)
        if self.left is not None:
            self.left.print()
        if self.right is not None:
            self.right.print()




root = BinaryTree(20)
root.leftI(BinaryTree(10))
root.rightI(BinaryTree(30))

root.left.leftI(BinaryTree(5))
root.left.rightI(BinaryTree(8))

root.right.leftI(BinaryTree(25))
root.right.rightI(BinaryTree(35))

root.print()
