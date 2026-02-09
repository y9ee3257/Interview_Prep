class Tabulation:
    def countSubsets(self, num, sum1):
        n = len(num)
        output = [[0 for _ in range(sum1 + 1)] for _ in range(n)]

        for index in range(n):
            for capacity in range(sum1 + 1):
                if capacity == 0:
                    output[index][0] = 1
                elif index == 0:
                    output[0][capacity] = 1 if num[index] == capacity else 0
                else:
                    include = 0
                    if capacity - num[index] >= 0:
                        include = output[index - 1][capacity - num[index]]
                    exclude = output[index - 1][capacity]
                    output[index][capacity] = include + exclude

        print(output)
        return output[n - 1][sum1]
