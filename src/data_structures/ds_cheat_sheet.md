# Heaps
1. All heaps are complete binary trees
2. The array representation of heap starts with index 1, so leave the 0th index empty.
   1. ex: [ , 10, 30, 20, 35, 40, 32, 25]
   2. This is to accommodate the below formulas. For any node at index "i" the below formulas work
   3. left child = 2i
   4. right child = 2i+1
   5. parent = i/2 (floor value)
3. Two types of heaps
   1. Max Heap 
   2. Min Heap

### Max Heap & Min Heap
1. Highest number will always be on top.
2. All child elements are less than or equal to the parent.
3. It is not a binary search tree, so the left child can be greater than right.
4. Same goes with Min Heap but just the opposite.

### Heapify
1. Converting a regular list into a heap list is called heapify. It rearranges them to follow the min/max heap rules.
2. Procedure to heapify
   1. Start with the end of array.
   2. For every element, compare with its child elements and swap accordingly and do this recursively.
   3. Do the above until you reach the start of the array.

### Sorting
1. You get sorted list by popping the parent continuously. 
2. The heap will auto reorganize itself to bring the next highest element to the top.

### heapq in python
Push (heappush): Adds an element to the heap while maintaining the heap property.
Pop (heappop): Removes and returns the smallest element in the heap, again maintaining the heap property.


| Strings     | value            |
|-------------|------------------|
| Peak        | heapq.peak()    |
| Push        | heapq.heappush()     |
| Pop         | heapq.heappop()      | 
| Pop         | heapq.heappop()      | 
| Heapify     | heapq.heapify(listForTree) |
| Heapify Max | heapq._heapify_max(listForTree) |



heapq.peak() View the smallest element without removing it.
heapq.heapify(listForTree)             # for a min heap
heapq._heapify_max(listForTree)
heapq.heappop(minheap)      # pop from minheap
heapq._heappop_max(maxheap) # pop from maxheap