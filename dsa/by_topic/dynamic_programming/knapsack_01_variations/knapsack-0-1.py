# https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/

# Recursive Approach
class KnapsackRecursive:
    def solution(self, wt, val, cap):
        self.wt, self.val = wt, val
        return self.helper(cap, 0, len(wt) - 1)

    def helper(self, wt_left, total_val, index):
        if wt_left == 0 or index < 0:
            return total_val
        include = 0
        if wt_left >= self.wt[index]:
            include = self.helper(wt_left - self.wt[index], total_val + self.val[index], index - 1)
        exclude = self.helper(wt_left - self.wt[index], total_val + self.val[index], index - 1)
        return max(include, exclude)


class KnapsackIterative:
    def solution(self, wt, val, cap):
        length = len(wt)
        output = [[0 for _ in range(cap+1)] for _ in range(length)]

        for r in range(length):
            for c in range(cap+1):
                if c == 0:
                    output[r][c] = 0
                if r == 0:
                    output[r][c] = wt[r] if c >= wt[r] else 0

                # max(include,exclude)
                include = 0
                if c >= wt[r]:
                    include = val[r] + output[r - 1][c - wt[r]]
                exclude = output[r - 1][c]

                output[r][c] = max(include, exclude)

        return output


class Knapsack1:
    """
    Initial Approach 1
    """

    def solution(self, wt, val, capacity):
        self.wt = wt
        self.val = val
        self.capacity = capacity
        self.max = 0
        self.knapsack_hlpr(0, 0, 0, [])
        return self.max

    def knapsack_hlpr(self, wt, val, i, slate):
        if wt > self.capacity:
            return
        self.max = max(self.max, val)
        # print(slate)
        if i >= len(self.wt):
            return
        self.knapsack_hlpr(wt, val, i + 1, slate)
        slate.append((self.wt[i], self.val[i]))
        self.knapsack_hlpr(wt + self.wt[i], val + self.val[i], i + 1, slate)
        slate.pop()


class Knapsack2:
    """
    Initial Approach 2
    """

    def solution(self, wt, val, capacity):
        self.wt = wt
        self.val = val
        self.capacity = capacity
        self.max = 0
        self.n = len(wt)
        self.knapsack_hlpr(0, 0, set(range(self.n)), [])
        return self.max

    def knapsack_hlpr(self, wt, val, remaining, slate):
        if wt > self.capacity:
            return
        self.max = max(self.max, val)
        # print(slate)

        if len(remaining) == 0:
            return

        remaining_copy = remaining.copy()

        for i in remaining_copy:
            remaining.remove(i)
            slate.append((self.wt[i], self.val[i]))
            self.knapsack_hlpr(wt + self.wt[i], val + self.val[i], remaining, slate)
            slate.pop()
            remaining.add(i)


instance = KnapsackRecursive()
print("recursive", instance.solution([1, 4, 6], [1, 2, 3], 10))

instance = KnapsackIterative()
print("iterative", instance.solution([1, 4, 6], [1, 2, 3], 10))

# instance = Knapsack1()
# print(instance.solution([1, 4, 6], [1, 2, 3], 10))
#
# instance = Knapsack2()
# print(instance.solution([1, 4, 6], [1, 2, 3], 10))
