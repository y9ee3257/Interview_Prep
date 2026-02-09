"""
https://www.designgurus.io/course-play/grokking-dynamic-programming/doc/rod-cutting
https://www.geeksforgeeks.org/dsa/cutting-a-rod-dp-13/
"""

class RodCuttingIterative:
    def solveRodCutting(self, lengths, prices, n):

        output = [0 for _ in range(n + 1)]

        for max_len in range(1, n + 1):
            max_profit = 0
            for i, length in enumerate(lengths):
                if max_len - length > 0:
                    profit = prices[i] + output[max_len - length]
                    max_profit = max(profit, max_profit)

            output[max_len] = max_profit
        print(output)
        return output[n]
