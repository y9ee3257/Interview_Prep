# https://leetcode.com/problems/insert-delete-getrandom-o1
import random
class RandomizedSet:

    def __init__(self):
        self.random_arr = []
        self.random_map = {}

    def insert(self, val: int) -> bool:
        if val in self.random_map:
            return False
        self.random_arr.append(val)
        self.random_map[val] = len(self.random_arr) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.random_map:
            return False

        index = self.random_map[val]
        self.random_arr[index], self.random_arr[-1] = self.random_arr[-1], self.random_arr[index]
        self.random_map[self.random_arr[index]] = index
        self.random_arr.pop()
        del self.random_map[val]
        return True

    def getRandom(self) -> int:
        random_index = random.randrange(0, len(self.random_arr))
        return self.random_arr[random_index]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()