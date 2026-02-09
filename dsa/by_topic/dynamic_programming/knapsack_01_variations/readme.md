### Easy Explanation:
https://youtu.be/xCbYmUPvc2Q?si=3iYRL9DcnGkY4uwb


### Knapsack 0-1 pattern

Given two arrays, profit[] and weight[], where each element represents the profit and weight of an item respectively,
also given an integer W representing the maximum capacity of the knapsack (the total weight it can hold).
Task is to put the items into the knapsack such that the sum of profits associated with them is the maximum possible,
without exceeding the capacity W.

Note: We can either include an item completely or exclude it entirely — we cannot include a fraction of an item.

Examples:

Input:  W = 4, profit[] = [1, 2, 3], weight[] = [4, 5, 1]  
Output: 3  
Explanation: There are two items which have weight less than or equal to 4. If we select the item with weight 4, the
possible profit is 1. And if we select the item with weight 1, the possible profit is 3. So the maximum possible profit
is 3. Note that we cannot put both the items with weight 4 and 1 together as the capacity of the bag is 4.

Input: W = 3, profit[] = [1, 2, 3], weight[] = [4, 5, 6]  
Output: 0  
Explanation: All the item weights are greater than the knapsack capacity.

#### Recursion

```python 
    def solution(self, weight, profit, W):
    self.weight, self.profit = weight, profit
    return self.helper(len(weight) - 1, W, 0)


def helper(self, index, capacity, profit_so_far):
    if index < 0 or capacity == 0:
        return profit_so_far

    include = 0
    if capacity - self.weight[index] >= 0:
        include = self.helper(index + 1, capacity - self.weight[index], profit_so_far + self.profit[index])
    exclude = self.helper(index + 1, capacity, profit_so_far)
    return max(include, exclude)
```

#### Memoization

```

```

#### Tabulation

```python
    def solution(self, wt, val, cap):
    n = len(wt)
    output = [[0 for _ in range(cap + 1)] for _ in range(n)]

    for index in range(n):
        for capacity in range(cap + 1):
            if capacity == 0:
                output[index][capacity] = 0
            elif index == 0:
                output[index][capacity] = wt[index] if capacity >= wt[index] else 0
            else:
                include = 0
                if capacity - wt[index] >= 0:
                    include = val[index] + output[index - 1][capacity - wt[index]]
                exclude = output[index - 1][capacity]

                output[index][capacity] = max(include, exclude)

    return output[n - 1][cap]
```

#### Similar problems with minor changes

1. Subset Sum:  
   https://www.geeksforgeeks.org/dsa/subset-sum-problem-dp-25/
    ```python
        def isSubsetSum(self, arr, sum):
            n = len(arr)
            output = [[False for _ in range(sum + 1)] for _ in range(n)]
    
            for index in range(n):
                for target in range(sum + 1):
                    if target == 0:
                        output[index][target] = True
                    elif index == 0:
                        output[index][target] = arr[index] == target
                    else:
                        include = False
                        if target-arr[index] >=0 :
                            include = output[index - 1][target - arr[index]]
                        exclude = output[index - 1][target]
                        output[index][target] = include or exclude
            return output[n - 1][sum]
    ```
2. Equal Subset Sum:   
   https://leetcode.com/problems/partition-equal-subset-sum/description/
    ```python
    def solution(self, nums):
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2

        output = [[-1 for _ in range(target + 1)] for _ in range(len(nums))]

        for index in range(len(nums)):
            for target_sum in range(target + 1):
                if target_sum == 0:
                    output[index][target_sum] = False
                elif index == 0:
                    output[index][target_sum] = target_sum == nums[index]
                else:
                    include = False
                    if target_sum - nums[index] >=0 :
                        include = output[index - 1][target_sum - nums[index]]
                    exclude = output[index - 1][target_sum]
                    output[index][target_sum] = include or exclude

        return output[len(nums) - 1][target]
    ```
3. Minimum Subset sum diff:  
   https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference/
   ```python 
    def minimumDifference(self, nums: List[int]) -> int:
        total = sum(nums)
        target = total // 2
        size = len(nums)

        output = [[False for _ in range(target + 1)] for _ in range(size)]

        for index in range(size):
            for capacity in range(target + 1):
                if capacity == 0:
                    output[index][0] = True
                elif index == 0:
                    output[0][capacity] = nums[index] == capacity
                else:
                    include = False
                    if capacity - nums[index] >= 0:
                        include = output[index - 1][capacity - nums[index]]
                    exclude = output[index - 1][capacity]
                    output[index][capacity] = include or exclude

        for i in range(target, -1, -1):
            if output[size - 1][i]:
                return total - (2 * i)

        return 0
   ```
4. Count of Subset Sum:  
   https://www.geeksforgeeks.org/dsa/count-of-subsets-with-sum-equal-to-x/
   ```python
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

        return output[n - 1][sum1]

   ```