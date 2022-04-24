from data_structures.linked_list import SinglyLinkedListNode


class Queue:
    def __init__(self, items=[]):
        self._head = None
        self._tail = None
        self._size = 0

        for item in items:
            self.enqueue(item)

    def __len__(self):
        return self._size

    def enqueue(self, value):
        new_node = SinglyLinkedListNode(value)

        if self.is_empty():
            self._head = new_node
            self._tail = new_node
            self._size += 1
            return

        self._tail.set_next(new_node)
        self._tail = new_node
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            return None

        node_to_remove = self._head

        if len(self) == 1:
            self._head = None
            self._tail = None
        else:
            self._head = self._head.get_next()

        self._size -= 1

        return node_to_remove

    def peek(self):
        return self._head

    def is_empty(self):
        return self._size == 0
