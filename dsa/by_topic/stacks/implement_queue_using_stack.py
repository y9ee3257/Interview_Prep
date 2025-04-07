class CustomQueue:
    def __init__(self, elements=None):
        if elements is None:
            elements = []
        if elements:
            self.queue = elements
        else:
            self.queue = []

    def push(self, element):
        self.queue.append(element)

    def pop(self):
        if self.queue:
            top = self.queue[0]
            self.queue = self.queue[1:]
            return top
        else:
            raise Exception("Queue is empty")

    def start(self):
        if self.queue:
            return self.queue[0]
        else:
            return None

    def end(self):
        if self.queue:
            return self.queue[-1]
        else:
            return None

    def print(self):
        print(self.queue)


queue = CustomQueue()
queue.push(2)
queue.push(3)
queue.push(4)
queue.push(5)
queue.pop()
queue.push(6)
queue.pop()
queue.pop()
queue.pop()
queue.print()
