# Math
# max in an array
# min in an array
# sum of an array
# represent Infinity
# absolute value of a num
# power of number

arr = [15, 4, 6, 2, 0]
print("min element", min(arr))
print("sum of elements", sum(arr))
print("Infinity", float("inf"))
print("Negative Infinity", -float("inf"))
print("Absolute value of a number", abs(-12.8))
print("power of number", pow(2, 3))
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

dict = {}
dict[1] = 25
dict[2] = 33
dict["abc"] = "xyz"
print("after adding elements", dict)
del dict["abc"]
print("after deleting an element", dict)
print("get key", dict.get(2))
print("default value", dict.get("abc", "default"))
print("all values", dict.values())
print("all keys", dict.keys())
print("all entries", dict.items())
for key, value in dict.items():
    print(key, ":", value)
from collections import Counter

print("frequency counter", Counter([1, 2, 2, 3, 3, 4]))
print("---------------------------------------")

# Arrays:
# add element
# remove element
# remove element at index
# length
# copy list
# initialize with elements
# initialize 2D array with elements
# string to int array
# int array to string
# list to string
# join 2 arrays
# sort ascending
# sort descending
# sort by 2nd index
# sort ascending
# sort descending

arr = [5, 2, 3, 6, 2, 3]
arr.append(25)
print("after adding element", arr)
arr.pop()
print("after deleting last element", arr)
arr.pop(2)
print("after deleting element at index ", arr)
print("length of array", len(arr))
new_list = arr[:]
print("copied to a new list", new_list)
print("initialize with elements", [i for i in range(10)])
print("initialize with elements", [[i for i in range(10)] for j in range(100)])
print("string to int arr", [int(char) for char in "123456"])
print("list to string", "".join(str(i) for i in arr))
print("string to list", "abcdef"[::-1])
arr.sort()
print("after sorting the array", arr)
arr.sort(reverse=True)
print("after sorting in reverse order", arr)
arr = [("def", 6, "abc"), ("xyz", 2, "xyz"), ("abc", 3, "def"), ("uvw", 10, "uvw")]
arr.sort(key=lambda x: x[1])
print("after sorting by 2nd index asc", arr)
arr.sort(key=lambda x: x[1], reverse=True)
print("after sorting by 2nd index desc", arr)
print("---------------------------------------")

# Strings (String are immutable)
# substring from index 3,5
# substring alternate chars
# substring last 3 chars
# replace character at index
# split the string by char
# reverse the string
# convert to list
# sort
# char to ascii
# ascii to char
# check if the given char is int
# convert the list back to string
# to upper case
# to lower case

str = "hello this IS Ravi"
print("substring from index 2-3", str[2:4])
print("substring alternative chars", str[::2])
print("split the string on char", str.split("i"))
print("last 3 chars", str[-3:])
print("replace char at index 3", str[:3] + "r" + str[4:])
print("reverse the string", str[::-1])
print("convert to list", list(str))
print("sort using ascii", sorted(str))
print("ascii value of a, A", ord('a'), ord('A'))
print("char from ascii", chr(ord('a')), chr(ord('A')))
print("check if char is integer", "1".isnumeric())
print("list to string", "".join(list(str)))
print("to upper", 'a'.upper())
print("to lower", 'A'.lower())
print("---------------------------------------")

# Stack & Queues
# using dequeue (array can also be used for stack)
# add element to left
# add element to right
# remove element from left
# remove element from right

from collections import deque

q = deque()
q.append(2)
q.append(3)
print("after adding element to right", q)
q.appendleft(1)
print("after adding element to left", q)
q.pop()
print("after removing element from right", q)
q.popleft()
print("after removing element from left", q)
print("---------------------------------------")

# Heaps
# sort ascending using heap
# sort descending using heap
# print top k elements, heap space is O(k)
# print bottom k elements, heap space is O(k)
# sort tuples using priority queue
# when same priority, tie break it

lst = [5, 4, 6, 3, 9]
from queue import PriorityQueue

pq = PriorityQueue()
for num in lst:
    pq.put(num)
output = []
while not pq.empty():
    output.append(pq.get())
print("sort ascending", output)

pq = PriorityQueue()
for num in lst:
    pq.put(-num)
output = []
while not pq.empty():
    output.append(-pq.get())
print("sort descending", output)

pq = PriorityQueue()
for num in lst:
    pq.put(num)
    while pq.qsize() > 3:
        pq.get()
output = []
while not pq.empty():
    output.append(pq.get())
print("top k elements", output)

pq = PriorityQueue()
for num in lst:
    pq.put(-num)
    while pq.qsize() > 3:
        pq.get()
output = []
while not pq.empty():
    output.append(-pq.get())
print("bottom k elements", output)

tasks = [(6, "abc"), (2, "xyz"), (2, "def"), (10, "uvw")]
for idx, task in enumerate(tasks):
    pq.put((task[0], idx, task[1]))
output = []
while not pq.empty():
    output.append(pq.get()[2])
print("tasks by priority", output)
print("---------------------------------------")

# Set
# add to set
# remove from set
# remove last added value
# len of set
st = set()
st.add(3)
st.add(4)
st.add(3)
print("after adding duplicate valuse to set", st)
st.remove(3)
print("after removing a number from set", st)
st.add(1)
st.pop()
print("after removing recently added value", st)
print("length of set ", len(st))
print("---------------------------------------")

# Misc
# ternary if
# for loop using range
# for loop using enumerate
# check if value is string/boolean/int

print("ternary if", 2 if 2==2 else 3)
print("is integer", isinstance(2,int))
print("is boolean", isinstance("abc",str))
print("is boolean", isinstance(True,bool))