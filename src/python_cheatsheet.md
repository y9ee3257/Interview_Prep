**If Conditions**
1. Syntax for multiple conditions in an if statement
   1. ```
      if ((cond1 and/or cond2) and/or (cond3 and/or cond4)):
      ```
   2. the outer brackets "()" are mandatory 
2. Alternative for ternary operator (single line if statement)
   1. ```
      result = value1 if cond else value2
      ```

**Math Functions**
1. abs(-2)
2. max(2, 3)
3. min(3, 5)
4. float("inf")  # infinite value
5. pow(2, 3)  # 2^3

**Arrays**
1. string_to_int_array = [int(x) for x in string_array]
2. array_to_string = " ".join(map(str, output))
3. Joining two arrays
   1. arr1 + arr2
   2. [*arr1, *arr2]

**Set**

                1
              /   \
            2       3
             \    /   \
              4  5     6
             /     \   / \
            7       8 9  10
                       \
                        11
                          \
                           12

**Strings**
1. s = s[:2] + "h" + s[3:]  # to change char at index 2, String are immutable in python
2. ord("c")  # get ascii value of a char and vice versa
3. chr(97)  # get char from ascii
4. string.lower()
5. string.upper()
6. char.isdigit()

**Dictionaries**
1. del dict["a"]  # delete key if you know it exists
2. dict.pop("a")  # delete key if you don't know it exists
3. dict.get('a', 0)  # get key with default value
4. dict.keys()  # iterable list of keys
5. dict.values()  # iterable list of values
6. Counter("aabbccc")  # {a:2,b:2,c:3} count of frequencies as dict
7. list(dict)  # ["a","b","c"]

**Stacks/Queues/Deque**
1. from collections import deque
2. deque = deque()
3. deque.append(2)
4. deque.appendleft(3)
5. deque.pop()
6. deque.popleft()

**General**
1. isinstance(object, type)
   1. ex: isinstance(2,int)
   2. ex: isinstance("string", str)
   3. ex: isinstance("Hello", (float, int, str, list, dict, tuple)) # check multiple
2. Exception
   1. ```
      raise Exception("Queue is empty")
      ```

**Classes**
1. constructor with optional arguments
   1. ```
      def __init__(self, elements=None)
             self.queue = elements
      ```
2. 


