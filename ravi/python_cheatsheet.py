from collections import Counter

array = [1, 2, 3, 4, 5]
output = [3, 2, 4]
string_array = ["1", "2", "3", "4"]

# Math functions
# absolute value
abs(-2)
max(2, 3)
min(3, 5)
float("inf")  # infinite value
pow(2, 3)  # 2^3

# Loops
string_to_int_array = [int(x) for x in string_array]

#
print(" ".join(map(str, output)))

#Strings
s = "aabbccd"
s = s[:2]+"h"+s[3:] # to change char at index 2, String are immutable in python
ord("c") # get ascii value of a char and vice versa
chr(97) # get char from ascii


# Dictionaries
dict = {"a": 1, "b": 2}
del dict["a"]  # delete key if you know it exists
dict.pop("a")  # delete key if you don't know it exists
dict.get('a', 0)  # get key with default value
dict.keys()  # iterable list of keys
dict.values()  # iterable list of values
Counter("aabbccc")  # {a:2,b:2,c:3} count of frequencies as dict
list(dict)  # ["a","b","c"]
