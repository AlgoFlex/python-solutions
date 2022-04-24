from data_structures.linked_list import SinglyLinkedListNode


class Stack:
    def __init__(self, max_size=1000):
        self._top = None
        self._max_size = max_size
        self._size = 0

    def __len__(self):
        return self._size

    def peek(self):
        return self._top

    def push(self, value):
        if self.has_space() is False:
            raise ValueError("Stack overflow")

        new_node = SinglyLinkedListNode(value)
        new_node.set_next(self._top)
        self._top = new_node
        self._size += 1

    def pop(self):
        if self.is_empty():
            return None

        current_top = self._top
        self._top = self._top.get_next()
        self._size -= 1

        return current_top

    def is_empty(self):
        return self._size == 0

    def has_space(self):
        return self._max_size > self._size
