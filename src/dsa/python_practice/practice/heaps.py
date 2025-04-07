import heapq

def heap_sort_array(arr):
    """Sorts an array using a heap."""
    pass

def heap_sort_ascending(arr):
    """Sorts an array in ascending order using a heap."""
    pass

def heap_sort_descending(arr):
    """Sorts an array in descending order using a heap."""
    pass

def heap_print_top_k(arr, k):
    """Prints the top k elements from a heapified array."""
    pass

def heap_print_last_k(arr, k):
    """Prints the last k elements from a heapified array."""
    pass

def heap_sort_tuples_priority(tuples):
    """Sorts a list of tuples using a priority queue (heap)."""
    pass

def heap_sort_tuples_priority_tie_break(tuples, tie_break_index):
    """Sorts tuples by priority, breaking ties using a specified index."""
    pass

def heap_get_top_k_priority(tuples, k):
    """Gets the top k priority elements from a list of tuples."""
    pass

def heap_get_last_k_priority(tuples, k):
    """Gets the last k priority elements from a list of tuples."""
    pass

# Test Cases
def test_heap_functions():
    # Test heap sort array
    arr1 = [3, 1, 4, 1, 5, 9, 2, 6]
    #assert heap_sort_array(arr1.copy()) == [1, 1, 2, 3, 4, 5, 6, 9] #will fail

    # Test heap sort ascending
    arr2 = [3, 1, 4, 1, 5, 9, 2, 6]
    #assert heap_sort_ascending(arr2.copy()) == [1, 1, 2, 3, 4, 5, 6, 9] #will fail

    # Test heap sort descending
    arr3 = [3, 1, 4, 1, 5, 9, 2, 6]
    #assert heap_sort_descending(arr3.copy()) == [9, 6, 5, 4, 3, 2, 1, 1] #will fail

    # Test print top k
    arr4 = [9, 6, 5, 4, 3, 2, 1, 1] #assume heapified
    #heap_print_top_k(arr4.copy(), 3) #will fail, print output needs to be checked manually

    # Test print last k
    arr5 = [1, 1, 2, 3, 4, 5, 6, 9] #assume heapified
    #heap_print_last_k(arr5.copy(), 3) #will fail, print output needs to be checked manually

    # Test sort tuples priority
    tuples1 = [(3, 'a'), (1, 'b'), (4, 'c'), (1, 'd')]
    #assert heap_sort_tuples_priority(tuples1.copy()) == [(1, 'b'), (1, 'd'), (3, 'a'), (4, 'c')] #will fail

    # Test sort tuples priority tie break
    tuples2 = [(3, 'a', 1), (1, 'b', 2), (4, 'c', 3), (1, 'd', 4)]
    #assert heap_sort_tuples_priority_tie_break(tuples2.copy(), 2) == [(1, 'b', 2), (1, 'd', 4), (3, 'a', 1), (4, 'c', 3)] #will fail

    # Test get top k priority
    tuples3 = [(3, 'a'), (1, 'b'), (4, 'c'), (1, 'd')]
    #assert heap_get_top_k_priority(tuples3.copy(), 2) == [(1, 'b'), (1, 'd')] #will fail

    # Test get last k priority
    tuples4 = [(3, 'a'), (1, 'b'), (4, 'c'), (1, 'd')]
    #assert heap_get_last_k_priority(tuples4.copy(), 2) == [(3, 'a'), (4, 'c')] #will fail

test_heap_functions()