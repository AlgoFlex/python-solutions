class SinglyLinkedListNode:
    def __init__(self, value, next=None):
        self._value = value
        self._next = next

    def get_value(self):
        return self._value

    def get_next(self):
        return self._next

    def set_next(self, next_node):
        self._next = next_node
