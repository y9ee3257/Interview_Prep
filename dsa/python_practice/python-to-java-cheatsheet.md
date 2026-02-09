## List

| Operation   | Python `list` | Java `ArrayList<T>`              |
|-------------|---------------|----------------------------------|
| Create      | `a = []`      | `List<T> a = new ArrayList<>();` |
| Add         | `a.append(x)` | `a.add(x)`                       |
| Get         | `a[i]`        | `a.get(i)`                       |
| Set         | `a[i] = x`    | `a.set(i, x)`                    |
| Remove last | `a.pop()`     | `a.remove(a.size()-1)`           |
| Remove at i | `a.pop(i)`    | `a.remove(i)`                    |
| Length      | `len(a)`      | `a.size()`                       |
| Sort        | `a.sort()`    | `Collections.sort(a)`            |
| Reverse     | `a.reverse()` | `Collections.reverse(a)`         |

## Set

| Operation | Python `set`  | Java `HashSet<T>`             |
|-----------|---------------|-------------------------------|
| Create    | `s = set()`   | `Set<T> s = new HashSet<>();` |
| Add       | `s.add(x)`    | `s.add(x)`                    |
| Remove    | `s.remove(x)` | `s.remove(x)`                 |
| Contains  | `x in s`      | `s.contains(x)`               |
| Size      | `len(s)`      | `s.size()`                    |
| Iterate   | `for x in s:` | `for (T x : s)`               |

## Map

| Operation     | Python `dict`          | Java `HashMap<K,V>`             |
|---------------|------------------------|---------------------------------|
| Create        | `m = {}`               | `Map<K,V> m = new HashMap<>();` |
| Put           | `m[k] = v`             | `m.put(k, v)`                   |
| Get           | `m[k]`                 | `m.get(k)`                      |
| Get default   | `m.get(k,0)`           | `m.getOrDefault(k, 0)`          |
| Contains key  | `k in m`               | `m.containsKey(k)`              |
| Remove        | `del m[k]`             | `m.remove(k)`                   |
| Size          | `len(m)`               | `m.size()`                      |
| Iterate keys  | `for k in m:`          | `for (K k : m.keySet())`        |
| Iterate items | `for k,v in m.items()` | `for (var e : m.entrySet())`    |

## Stack

| Operation | Python (`list`) | Java (`ArrayDeque<T>`)              |
|-----------|-----------------|-------------------------------------|
| Create    | `st = []`       | `Deque<T> st = new ArrayDeque<>();` |
| Push      | `st.append(x)`  | `st.push(x)`                        |
| Pop       | `st.pop()`      | `st.pop()`                          |
| Peek      | `st[-1]`        | `st.peek()`                         |
| Empty     | `not st`        | `st.isEmpty()`                      |
| Size      | `len(st)`       | `st.size()`                         |

## Queue

| Operation | Python `deque` | Java `ArrayDeque<T>`               |
|-----------|----------------|------------------------------------|
| Create    | `q = deque()`  | `Deque<T> q = new ArrayDeque<>();` |
| Enqueue   | `q.append(x)`  | `q.offer(x)`                       |
| Dequeue   | `q.popleft()`  | `q.poll()`                         |
| Peek      | `q[0]`         | `q.peek()`                         |
| Empty     | `not q`        | `q.isEmpty()`                      |
| Size      | `len(q)`       | `q.size()`                         |

## Heap

| Operation       | Python `heapq`   | Java `PriorityQueue<T>`                        |
|-----------------|------------------|------------------------------------------------|
| Create min heap | `h = []`         | `PriorityQueue<T> pq = new PriorityQueue<>();` |
| Push            | `heappush(h, x)` | `pq.offer(x)`                                  |
| Pop             | `heappop(h)`     | `pq.poll()`                                    |
| Peek            | `h[0]`           | `pq.peek()`                                    |
| Size            | `len(h)`         | `pq.size()`                                    |

## Strings

| Operation    | Python `str`            | Java `String`                    |
|--------------|-------------------------|----------------------------------|
| Length       | `len(s)`                | `s.length()`                     |
| Char at i    | `s[i]`                  | `s.charAt(i)`                    |
| Substring    | `s[l:r]`                | `s.substring(l, r)`              |
| Contains     | `"ab" in s`             | `s.contains("ab")`               |
| Find index   | `s.find("a")`           | `s.indexOf("a")`                 |
| Starts/Ends  | `startswith / endswith` | `startsWith / endsWith`          |
| Split        | `s.split(",")`          | `s.split(",")`                   |
| Replace      | `s.replace("a","b")`    | `s.replace("a","b")`             |
| Reverse      | `s[::-1]`               | `new StringBuilder(s).reverse()` |
| Build string | `"".join()`             | `StringBuilder`                  |



1. Initialize array with values
2. Using Tuple (record in java) with different datatypes
3. 