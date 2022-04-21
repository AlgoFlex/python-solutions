class Node:
    def __init__(self, value, next=None):
        self._value = value
        self._next = next

    def get_value(self):
        return self._value

    def get_next(self):
        return self._next

    def set_next(self, next_node):
        self._next = next_node


class SinglyLinkedList:
    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def get_head(self):
        return self._head

    def append(self, value):
        new_node = Node(value)

        if self._head is None:
            self._head = new_node
            self._size += 1
            return

        current_node = self._head
        while current_node.get_next():
            current_node = current_node.get_next()

        current_node.set_next(new_node)
        self._size += 1

    def prepend(self, value):
        self._head = Node(value, self._head)
        self._size += 1
