Two ways to solve a problem
1. Divide and conquer
2. Decrease and conquer


Stack Trace (each stack trace will contain all the below variables stored)
1. Function Address
2. Parameters
3. Local Variables
4. Return Address

***
When to use Recursion vs Iteration
1. If it's a divide and conquer, recursion is a best approach.  
2. If it's a decrease and conquer use iteration.

Example:

compare factorial with iteration vs recursion

Iteration:
```python
fact = 1
for num in range(1,n):
    fact*=num
```
Time Complexity = O(n)  
Space Complexity = O(1) 

Recursion:
```python
def fact(num):
    if num == 0:
        return 1
    fact(num-1)
```
Time Complexity = O(n)  
Space Complexity = O(n) (stack trace that takes up memory for every recursion call)

For any recursive function the time complexity is equal to the number of nodes (assuming each node takes constant time).  
The number of children in a complete binary tree = 2^n  
But in recursion we will never have a full binary tree, it will be full until the height n/2 and will be semi filled after that.  
So the number of nodes will be between 2^n/2 to 2^n (2^n/2 is the height until which the recursion tree will be full)

Golden Ratio for fibonacci series (google it)  
Time Complexity = (golden-ratio)^n

Key Takeaways
1. nothing is executed in parallel. Space is going to re-used.
2. space complexity is propotional to height.
3. Time complexity is propotional to number of nodes in the recursion tree.

***

***Permutations***
```python
def recursion_function(input):
    # define base case and return when hit the base case
    if input == 0:
        return 1
    # reduce the size of input by exclude the current num
    recursion_function(input-1)
```

