from data_structures.queues import Queue


def test_enqueue():
    items = [1, 2, 3]
    queue = Queue(items)

    assert len(queue) == len(items)

    current_node = queue.peek()
    for item in items:
        assert current_node.get_value() == item
        current_node = current_node.get_next()


def test_dequeue():
    queue = Queue()

    assert queue.dequeue() is None

    items = [1, 2, 3]
    queue = Queue(items)

    for i, item in enumerate(items):
        assert queue.dequeue().get_value() == item
        assert len(queue) == len(items) - (i + 1)

    assert queue.peek() is None


def test_peek():
    queue = Queue()

    assert queue.peek() is None

    queue.enqueue(1)
    assert queue.peek().get_value() == 1

    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.peek().get_value() == 1

    queue.dequeue()
    assert queue.peek().get_value() == 2

    queue.dequeue()
    assert queue.peek().get_value() == 3


def test_len():
    items = [1, 2, 3]
    queue = Queue()

    for i, item in enumerate(items):
        queue.enqueue(item)
        assert len(queue) == i + 1


def test_is_empty():
    queue = Queue()

    assert queue.is_empty() is True

    queue.enqueue(1)
    assert queue.is_empty() is False
