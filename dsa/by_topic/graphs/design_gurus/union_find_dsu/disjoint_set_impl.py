class DisjointSet:

    def __init__(self, n):
        self.parent = []
        for i in range(n):
            self.parent.append(i + 1)
        self.size = [1] * n

    def find_parent(self, node):
        index = node-1
        if self.parent[index] == node:
            return node

        parent = self.find_parent(self.parent[index])
        self.parent[index] = parent
        return parent

    def union(self, node1, node2):
        print("performing union for ", node1, " and ", node2)
        parent1 = self.find_parent(node1)
        parent2 = self.find_parent(node2)

        print(parent1)
        print(parent2)

        if parent1 == parent2:
            return
        parent1_index = parent1-1
        parent2_index = parent2-1

        if self.size[parent1_index] > self.size[parent2_index]:
            self.parent[parent2_index] = parent1
            self.size[parent1_index] = self.size[parent1_index] + self.size[parent2_index]
        else:
            self.parent[parent1_index] = parent2
            self.size[parent2_index] = self.size[parent2_index] + self.size[parent1_index]

    def log(self):
        print(self.parent)
        print(self.size)
        print("-----------------")


ds = DisjointSet(8)
ds.log()
ds.union(1, 2)
ds.log()
ds.union(8, 3)
ds.log()
ds.union(4, 5)
ds.log()
ds.union(6, 7)
ds.log()
# ds.union(5, 6)
# ds.log()
# ds.union(3, 7)
# ds.log()

for i in range(8):
    ds.find_parent(i+1)
ds.log()