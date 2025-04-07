def stack_push(stack, element):
    """Adds an element to the top of the stack (right end of deque)."""
    pass

def stack_pop(stack):
    """Removes and returns the top element from the stack."""
    pass

def queue_enqueue_left(queue, element):
    """Adds an element to the left end of the queue."""
    pass

def queue_enqueue_right(queue, element):
    """Adds an element to the right end of the queue."""
    pass

def queue_dequeue_left(queue):
    """Removes and returns the element from the left end of the queue."""
    pass

def queue_dequeue_right(queue):
    """Removes and returns the element from the right end of the queue."""
    pass

# Test Cases
def test_stack_queue_functions():
    # Test Stack
    stack = deque()
    stack_push(stack, 1)
    stack_push(stack, 2)
    stack_push(stack, 3)
    assert list(stack) == [1, 2, 3]
    assert stack_pop(stack) == 3
    assert list(stack) == [1, 2]
    assert stack_pop(stack) == 2
    assert stack_pop(stack) == 1
    assert stack_pop(stack) == None

    # Test Queue (Left Enqueue/Dequeue)
    queue1 = deque()
    queue_enqueue_left(queue1, 1)
    queue_enqueue_left(queue1, 2)
    queue_enqueue_left(queue1, 3)
    assert list(queue1) == [3, 2, 1]
    assert queue_dequeue_left(queue1) == 3
    assert list(queue1) == [2, 1]
    assert queue_dequeue_left(queue1) == 2
    assert queue_dequeue_left(queue1) == 1
    assert queue_dequeue_left(queue1) == None

    # Test Queue (Right Enqueue/Dequeue)
    queue2 = deque()
    queue_enqueue_right(queue2, 1)
    queue_enqueue_right(queue2, 2)
    queue_enqueue_right(queue2, 3)
    assert list(queue2) == [1, 2, 3]
    assert queue_dequeue_right(queue2) == 3
    assert list(queue2) == [1, 2]
    assert queue_dequeue_right(queue2) == 2
    assert queue_dequeue_right(queue2) == 1
    assert queue_dequeue_right(queue2) == None

    # Test Queue (Left Enqueue/Right Dequeue)
    queue3 = deque()
    queue_enqueue_left(queue3, 1)
    queue_enqueue_left(queue3, 2)
    queue_enqueue_left(queue3, 3)
    assert queue_dequeue_right(queue3) == 1
    assert list(queue3) == [3, 2]

test_stack_queue_functions()