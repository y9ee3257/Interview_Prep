# implement heap with push/pull/min_heap/max_heap and heapify functionality


class Heap:
    __heap = []
    __is_min_heap = False

    def __init__(self, is_min_heap=False):
        self.__is_min_heap = is_min_heap

    def push(self, element):
        self.__heap.append(element)
        self.__propagate_up(len(self.__heap) - 1)

    def pull(self):
        if len(self.__heap) == 0:
            return None
        top = self.__heap[0]
        self.__heap[0] = self.__heap.pop()
        self.__propagate_down(0)
        return top

    def heapify(self, array):
        if len(array) == 0:
            return []
        self.__heap = array
        for idx in range(len(array) - 1, 0, -1):
            self.__propagate_down(idx)
        return self.__heap

    def __propagate_down(self, index):
        # if not 0 < index < len(self.__heap):
        #     return
        cur = self.__heap[index]
        left = self.__left(index)
        right = self.__right(index)
        if left is not None and right is not None:
            swap_index = None
            if cur < left and cur < right:
                if self.__is_min_heap:
                    swap_index = 2 * index + 1 if left < right else 2 * index + 2
                else:
                    swap_index = 2 * index + 1 if left > right else 2 * index + 2
            elif cur < left:
                swap_index = 2 * index + 1
            elif cur < right:
                swap_index = 2 * index + 2

            if swap_index is not None:
                self.__swap(index, swap_index)
                self.__propagate_down(swap_index)
        # elif left is not None:




    def __propagate_up(self, index):
        if not 0 < index < len(self.__heap):
            return
        cur = self.__heap[index]
        parent = self.__heap[(index - 1) // 2]
        if parent is not None and (self.__is_min_heap and cur < parent or not self.__is_min_heap and cur > parent):
            self.__swap(index, (index - 1) // 2)
            self.__propagate_up((index - 1) // 2)

    def __left(self, index):
        if 2 * index + 1 < len(self.__heap):
            return self.__heap[2 * index + 1]
        return None

    def __right(self, index):
        if 2 * index + 2 < len(self.__heap):
            return self.__heap[2 * index + 2]
        return None

    def __swap(self, p1, p2):
        self.__heap[p1], self.__heap[p2] = self.__heap[p2], self.__heap[p1]

    def heap_array(self):
        return self.__heap

    def sort(self):
        output = []
        for idx in range(len(self.__heap) - 1):
            output.append(self.pull())
        return output


heap = Heap()

print(heap.heapify([7, 6, 3, 2, 5, 4]))
heap.push(10)
heap.push(12)
heap.push(1)
print(heap.heap_array())
print(heap.sort())
