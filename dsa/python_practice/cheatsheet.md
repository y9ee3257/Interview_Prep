**Math Functions**

1. `abs(-2)`  # absolute value
2. `max(2, 3)`  # maximum of two numbers
3. `min(3, 5)`  # minimum of two numbers
4. `float("inf")`  # infinite value
5. `pow(2, 3)`  # 2^3

**Arrays**

1. `string_to_int_array = [int(x) for x in string_array]`
2. `array_to_string = " ".join(map(str, output))`
3. Joining two arrays:
    1. `arr1 + arr2`
    2. `[*arr1, *arr2]`

**Strings**

1. `s = s[:2] + "h" + s[3:]`  # change char at index 2 (strings are immutable in Python)
2. `ord("c")`  # get ASCII value of a character
3. `chr(97)`  # get character from ASCII value
4. `string.lower()`  # convert to lowercase
5. `string.upper()`  # convert to uppercase
6. `char.isdigit()`  # check if a character is a digit

**Dictionaries**

1. `del dict["a"]`  # delete key if you know it exists
2. `dict.pop("a")`  # delete key if unsure of existence
3. `dict.get('a', 0)`  # get key with default value
4. `dict.keys()`  # iterable list of keys
5. `dict.values()`  # iterable list of values
6. `Counter("aabbccc")`  # count character frequencies as dictionary
7. `list(dict)`  # list of dictionary keys

**Stacks/Queues/Deque**

1. `from collections import deque`
2. `dq = deque()`
3. `dq.append(2)`
4. `dq.appendleft(3)`
5. `dq.pop()`
6. `dq.popleft()`

**General**

1. `isinstance(object, type)`
    1. `isinstance(2, int)`
    2. `isinstance("string", str)`
    3. `isinstance("Hello", (float, int, str, list, dict, tuple))`  # check multiple types
2. Exception handling:
    1. ```python
       raise Exception("Queue is empty")
       ```

**Classes**

1. Constructor with optional arguments:
   ```python
   def __init__(self, elements=None):
       self.queue = elements
   ```

### Arrays

| Operation                  | Code Example                                  |
|----------------------------|-----------------------------------------------|
| Add element                | `list.append(value)`                          |
| Delete element             | `list.pop()`                                  |
| Length                     | `len(list)`                                   |
| Slice                      | `list[start:end:step]`                        |
| Get last element           | `list[-1]`                                    |
| Reverse                    | `list.reverse()`                              |
| Copy                       | `list.copy()` / `[*list]`/ `list[:]`          |
| Initialize with elements   | `[1 for x in range(10)]` *(avoid `[1]*n`)*    |
| Initialize 2D array        | `[[1] for x in range(10)] for y in range(10)` |
| Convert list to string     | `"".join(list)`                               |
| Convert string list to int | `[int(x) for x in list]`                      |
| Join two arrays            | `list1 + list2`                               |

### Strings

| Operation             | Code Example       |
|-----------------------|--------------------|
| ASCII value of char   | `ord(char)`        |
| Char from ASCII value | `chr(ascii)`       |
| Convert to lowercase  | `string.lower()`   |
| Convert to uppercase  | `string.upper()`   |
| Check if numeric      | `string.isdigit()` |

### Sorting

| Operation              | Code Example                                       |
|------------------------|----------------------------------------------------|
| Sort                   | `sorted(list)`                                     |
| Sort with key function | `intervals.sort(key=lambda x: x.foo)`              |
| Sort in reverse        | `intervals.sort(key=lambda x: x[0], reverse=True)` |

### Mathematical Functions

| Operation             | Code Example     |
|-----------------------|------------------|
| Maximum of 2 elements | `max(2, 3)`      |
| Minimum of 2 elements | `min(2, 3)`      |
| Sum of array          | `sum(list)`      |
| Absolute value        | `abs(x)`         |
| Power                 | `pow(base, exp)` |
| Positive Infinity     | `float("inf")`   |
| Negative Infinity     | `float("-inf")`  |

### Dictionary Operations

| Operation                         | Code Example          |
|-----------------------------------|-----------------------|
| Add key-value pair                | `dict["key"] = value` |
| Delete a key-value pair           | `del dict["key"]`     |
| Get keys from dict                | `dict.keys()`         |
| Get values from dict              | `dict.values()`       |
| Create dict from frequency counts | `Counter("aabbcc")`   |

### Stacks and Queues

| Operation  | Code Example      |
|------------|-------------------|
| Initialize | `queue = deque()` |
| Enqueue    | `queue.append(x)` |
| Dequeue    | `queue.popleft()` |
| Push       | `stack.append(x)` |
| Pop        | `stack.pop()`     |

### Type Checking

| Operation                     | Code Example                |
|-------------------------------|-----------------------------|
| Check if int                  | `isinstance(x, int)`        |
| Check if boolean              | `isinstance(x, bool)`       |
| Check if string               | `isinstance(x, str)`        |
| Check multiple instance types | `isinstance(x, (int, str))` |

### Heaps (heapq module)

| Function                  | Description                                  |
|---------------------------|----------------------------------------------|
| `heapq.heapify(x)`        | Converts list into a heap                    |
| `heapq.heappush(h, x)`    | Pushes x onto the heap                       |
| `heapq.heappop(h)`        | Pops the smallest item                       |
| `heapq.heappushpop(h, x)` | Pushes x then pops the smallest item         |
| `heapq.heapreplace(h, x)` | Pops then pushes x, always removing smallest |

### Bisect (Binary Search)

| Function                       | Purpose                                                                         | Returns                                                                         | Handles Duplicates                                 | Accepts Start & End Index?                            |
|--------------------------------|---------------------------------------------------------------------------------|---------------------------------------------------------------------------------|----------------------------------------------------|-------------------------------------------------------|
| `bisect_left(lst, x, lo, hi)`  | Finds the leftmost (first) index where `x` should be inserted to maintain order | Index of the first occurrence of `x` or the insertion point if `x` is not found | Returns the first occurrence of `x`                | ✅ Yes (search can be restricted within `lo` and `hi`) |
| `bisect_right(lst, x, lo, hi)` | Finds the rightmost (last + 1) index where `x` should be inserted               | Index just after the last occurrence of `x` or the insertion point              | Returns the index after the last occurrence of `x` | ✅ Yes (search can be restricted within `lo` and `hi`) |

```python
import bisect

lst = [1, 2, 4, 4, 5]
index = bisect.bisect_left(lst, 4)
print(index)  # 2
```
