class DoublyLinkedListNode:
    def __init__(self, value, next=None, prev=None):
        self._value = value
        self._next = next
        self._prev = prev

    def get_value(self):
        return self._value

    def get_next(self):
        return self._next

    def get_prev(self):
        return self._prev

    def set_next(self, next_node):
        self._next = next_node

    def set_prev(self, prev_node):
        self._prev = prev_node
