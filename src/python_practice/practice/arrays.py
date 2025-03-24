"""
Arrays:
1. add element
2. remove element
3. length
4. reverse the array
5. copy list
7. initialize with elements
8. initialize 2D array with elements
9. convert string array to int array
10. sort ascending
11. sort descending
12. list to string
13. join 2 arrays
14. sort by 2nd index
15. remove duplicates from list of lists
"""

def array_add_element(arr, element):
    """Adds an element to the end of the array."""
    pass

def array_remove_element(arr, element):
    """Removes the first occurrence of an element from the array."""
    pass

def array_length(arr):
    """Returns the length of the array."""
    pass

def array_reverse(arr):
    """Reverses the array in place."""
    pass

def array_copy(arr):
    """Returns a copy of the array."""
    pass

def array_initialize(elements):
    """Initializes an array with the given elements."""
    pass

def array_initialize_2d(elements):
    """Initializes a 2D array with the given elements."""
    pass

def array_string_to_int(arr):
    """Converts a string array to an integer array."""
    pass

def array_sort_ascending(arr):
    """Sorts the array in ascending order."""
    pass

def array_sort_descending(arr):
    """Sorts the array in descending order."""
    pass

def array_list_to_string(arr, separator=""):
    """Converts a list to a string with the given separator."""
    pass

def array_join(arr1, arr2):
    """Joins two arrays into a new array."""
    pass

def array_sort_by_second_index(arr):
    """Sorts a list of lists by the second element of each inner list."""
    pass

def array_remove_duplicates_list_of_lists(arr):
    """Removes duplicate inner lists from a list of lists."""
    pass

# Test Cases
def test_array_functions():
    # Test add element
    arr1 = [1, 2, 3]
    array_add_element(arr1, 4)
    assert arr1 == [1, 2, 3, 4]

    # Test remove element
    arr2 = [1, 2, 3, 2]
    array_remove_element(arr2, 2)
    assert arr2 == [1, 3, 2]

    # Test length
    arr3 = [1, 2, 3]
    assert array_length(arr3) == 3

    # Test reverse
    arr4 = [1, 2, 3]
    array_reverse(arr4)
    assert arr4 == [3, 2, 1]

    # Test copy
    arr5 = [1, 2, 3]
    copied_arr = array_copy(arr5)
    assert copied_arr == [1, 2, 3]
    assert copied_arr is not arr5

    # Test initialize
    arr6 = array_initialize([1, 2, 3])
    assert arr6 == [1, 2, 3]

    # Test initialize 2D
    arr7 = array_initialize_2d([[1, 2], [3, 4]])
    assert arr7 == [[1, 2], [3, 4]]

    # Test string to int
    arr8 = ["1", "2", "3"]
    int_arr = array_string_to_int(arr8)
    assert int_arr == [1, 2, 3]

    # Test sort ascending
    arr9 = [3, 1, 2]
    array_sort_ascending(arr9)
    assert arr9 == [1, 2, 3]

    # Test sort descending
    arr10 = [1, 3, 2]
    array_sort_descending(arr10)
    assert arr10 == [3, 2, 1]

    # Test list to string
    arr11 = [1, 2, 3]
    string_arr = array_list_to_string(arr11, "-")
    assert string_arr == "1-2-3"

    # Test join
    arr12 = [1, 2]
    arr13 = [3, 4]
    joined_arr = array_join(arr12, arr13)
    assert joined_arr == [1, 2, 3, 4]

    # Test sort by second index
    arr14 = [[2, 1], [1, 3], [3, 2]]
    array_sort_by_second_index(arr14)
    assert arr14 == [[2, 1], [3, 2], [1, 3]]

    # Test remove duplicates from list of lists
    arr15 = [[1, 2], [3, 4], [1, 2], [5, 6], [3, 4]]
    deduped_arr = array_remove_duplicates_list_of_lists(arr15)
    assert deduped_arr == [[1, 2], [3, 4], [5, 6]]

test_array_functions()