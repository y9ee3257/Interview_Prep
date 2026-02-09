"""
https://www.designgurus.io/course-play/grokking-dynamic-programming/doc/unbounded-knapsack
"""

class UnboundedKnapsackRecursion:
    def solveKnapsack(self, profits, weights, capacity):
        self.profits, self.weights = profits, weights
        return self.helper(capacity, 0)

    def helper(self, cap, profit):
        if cap == 0:
            return profit

        max_profit = profit
        for i, wt in enumerate(self.weights):
            if cap - wt >= 0:
                res = self.helper(cap - wt, profit + self.profits[i])
                max_profit = max(res, max_profit)

        return max_profit


class UnboundedKnapsackTabulation:
    def solveKnapsack(self, profits, weights, capacity):
        output = [0 for _ in range(capacity + 1)]

        for cap in range(1, capacity + 1):
            max_profit = output[cap]
            for i, wt in enumerate(weights):
                if cap - wt >= 0:
                    res = profits[i] + output[cap - wt]
                    max_profit = max(res, max_profit)
            output[cap] = max_profit

        return output[capacity]
