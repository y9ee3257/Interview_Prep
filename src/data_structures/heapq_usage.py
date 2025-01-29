import heapq

# Heaps
# sort the elements in the below array using heap. Sort both ascending and descending
array = [4, 3, 5, 2, 6]

# ascending order
heapq.heapify(array)
output = []
while len(array) > 0:
    output.append(heapq.heappop(array))
print(output)

# descending order
# add - when adding and removing the element
array = [4, 3, 5, 2, 6]
heap = []
output = []
for num in array:
    heapq.heappush(heap, -num)
while len(heap) > 0:
    output.append(-heapq.heappop(heap))
print(output)

# given a list of tasks with priority, add the elements to a priority queue,
# where you should be able to pop the highest priority element always.
tasks = [(6, "abc"), (2, "xyz"), (3, "def"), (10, "uvw")]
heapq.heapify(tasks)
output = []
while tasks:
    output.append(heapq.heappop(tasks))
print(output)

# get n largest and n smallest elements from the below array using heap
arr = [10, 3, 5, 4, 6, 2, 11, 20, 14, 15]
heapq.heapify(arr)
print(heapq.nlargest(3, arr))
print(heapq.nsmallest(3, arr))
