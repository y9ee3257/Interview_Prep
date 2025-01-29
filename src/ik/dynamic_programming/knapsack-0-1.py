# https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/

# Recursive solution:

def knapsack_helper(weight_arr, value_arr, target_weight, index):
    # include last element
    profit1 = knapsack_helper(weight_arr, value_arr, target_weight - weight_arr[index], index - 1)
    profit2 = knapsack_helper(weight_arr, value_arr, target_weight, index - 1)

    return max(profit1, profit2) + value_arr[index]


def knapsack_recursion(weight_arr, value_arr, target_weight):
    return knapsack_helper(weight_arr, value_arr, target_weight, len(weight_arr) - 1)
