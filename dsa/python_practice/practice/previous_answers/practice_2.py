# Math
import math
arr = [15, 4, 6, 2, 0]
print("max element", max(arr))
print("min element", min(arr))
print("sum of elements", sum(arr))
print("average of an array", sum(arr)/len(arr))
print("Infinity", math.inf)
print("Negative Infinity", -math.inf)
print("Absolute value of a number", abs(-9.3))
print("power of number", pow(2,3))
print("floor value ", math.floor(2.3))
print("ceil value ", math.ceil(2.4))
print("---------------------------------------")


# Numbers
print("binary string to integer", int("11101",2) )
print("integer to binary string", bin(23))
print("---------------------------------------")

# Strings (String are immutable)
string = "hello this IS Ravi"
print("substring from index 3-5", string[3:6])
print("substring alternate chars", string[::2])
print("substring last 3 chars", string[-3:])
print("replace character at index", string[:1] + "z" + string[2:])
print("replace first occurrence of a char", string.replace("l", "z", 1))
print("replace all occurrences of a char", string.replace("l", "z"))
print("convert to list", list(string))
print("convert to int", int("12343"))
print("sort using ascii values", sorted(string))
print("char to ascii", ord("a"))
print("ascii to char", chr(98))
print("check if the given string is a valid integer", )
print("check if the given char is number", "2".isdigit())
print("check if the given char is a letter", "a".isalpha() )
print("check if the given char is alphanumeric", "23a".isalnum())
print("check if the given char is a space", " ".isspace())
print("convert the list back to string", "".join(["a","b","c"]))
print("to upper case", string.upper())
print("to lower case", string.lower())
print("split using char", string.split("a"))
print("sort the string", sorted(string))
print("---------------------------------------")

# Arrays:
arr = [5, 2, 3, 6, 2, 3]
arr2 = [("def", 6, "abc"), ("xyz", 2, "xyz"), ("abc", 3, "def"), ("uvw", 10, "uvw")]
arr.append(5)
print("add element",arr)
arr.pop()
print("remove an element from the end", arr)
arr[3]=9
print("replace an element at index", arr)
del arr[3]
print("remove an element by index", arr)
arr.insert(1,35)
print("insert element at index",arr)
print("length", len(arr))
print("reverse the array", arr[::-1])
print("copy list", arr.copy())
print("initialize with elements", [5]*10)
print("initialize 2D array with elements",[[4]*10 for _ in range(5)] )
print("convert string array to int array", [int(x) for x in ["1","2","3"]])
print("list to string", "".join([str(x) for x in arr]))
print("join 2 arrays", [1,2,3]+arr)
arr.sort()
print("sort ascending --> ", arr)
arr.sort(reverse=True)
print("sort descending --> ", arr)
arr2.sort(key = lambda x: x[1])
print("sort by 2nd index --> ", arr2)
print("remove duplicates from list --> ", list(set(arr)) )
print("---------------------------------------")


# Dict
# add key/value pair
# delete key
# get key
# get or default
# get all values
# get key set
# iterate through entries
# list to freq dict
# iterate through entries in freq dic
# using default dict


dict = {}
print("add key/value pair", )
print("delete key", )
print("get key", )
print("get or default", )
print("get all values", )
print("get key set", )
print("iterate through entries", )
print("list to freq dict", )
print("iterate through entries in freq dict", )
print("using default dict", )

print("---------------------------------------")


# Stack & Queues
# using dequeue (array can also be used for stack)
# add element to left
# add element to right
# remove element from left
# remove element from right

print("after adding element to right", )
print("after adding element to left", )
print("after removing element from right", )
print("after removing element from left", )
print("---------------------------------------")

# Heaps
# sort array using heap
# sort ascending
# sort descending
# print top k elements
# print last k elements
# sort tuples using priority queue
# when same priority, tie break it
# get top k priority elements
# get last k priority elements

lst = [5,4,6,3,9]
print("sort ascending",)
print("sort descending",)
print("add elements")
print("remove elements")
print("top k elements",)
print("bottom k elements",)
tasks = [(6, "abc"), (2, "xyz"), (2, "def"), (10, "uvw")]
print("tasks by priority",)
print("get top k priority elements", )
print("get last k priority elements", )
print("---------------------------------------")


# Set
# add to set
# remove from set
# remove last added value
# len of set
print("after adding duplicate valuse to set", )
print("after removing a number from set", )
print("after removing recently added value", )
print("length of set ", )
print("---------------------------------------")


# bisect
# find element using binary search
# find the 1st occurrence of a number in a sorted list
# find the last occurrence of a number in a sorted list

print("find element using binary search", )
print("find the 1st occurrence of a number in a sorted list", )
print("find the last occurrence of a number in a sorted list", )


# Misc
# ternary if
# for loop using range
# for loop using enumerate
# check if value is string/boolean/int
# evaluate expression from a string (like "2+3-5")
# try catch (try to convert invalid string to int)

print("ternary if", )
print("for loop using range", )
print("for loop using enumerate", )
print("check if value is string/boolean/int", )
print("evaluate expression from a string (like '2+3-5')", )
print("try catch (try to convert invalid string to int)", )

