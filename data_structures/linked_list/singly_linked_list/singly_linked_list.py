from data_structures.node.singly_linked_list_node import SinglyLinkedListNode


class SinglyLinkedList:
    def __init__(self, items=[]):
        self._head = None
        self._size = 0

        for item in items:
            self.append(item)

    def __len__(self):
        return self._size

    def __str__(self):
        formatted = ""
        current_node = self._head
        while current_node:
            suffix = "->" if current_node.get_next() else ""
            formatted += f"{current_node.get_value()}{suffix}"
            current_node = current_node.get_next()

        return formatted

    def get_head(self):
        return self._head

    def is_empty(self):
        return self.size == 0

    def append(self, value):
        new_node = SinglyLinkedListNode(value)

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
        self._head = SinglyLinkedListNode(value, self._head)
        self._size += 1

    def find(self, target):
        current_node = self._head

        if current_node is None:
            return -1

        index = 0
        while current_node:
            if current_node.get_value() == target:
                return index
            current_node = current_node.get_next()
            index += 1

        return -1

    def insert(self, value, index):
        if index < 0 or index > self._size:
            raise IndexError("Index out of range")

        if index == 0:
            self.prepend(value)
            return

        if index == self._size:
            self.append(value)
            return

        new_node = SinglyLinkedListNode(value)
        current_node = self._head
        prev_node = None
        while index >= 0:
            prev_node = current_node
            current_node = current_node.get_next()
            index -= 1

        prev_node.set_next(new_node)
        new_node.set_next(current_node)
        self._size += 1

    def delete(self, target):
        if self._head is None:
            return

        if self._head.get_value() == target:
            self._head = self._head.get_next()
            self._size -= 1
            return

        prev_node = self._head
        current_node = self._head.get_next()
        while current_node:
            if current_node.get_value() == target:
                prev_node.set_next(current_node.get_next())
                self._size -= 1
                return
            prev_node = current_node
            current_node = current_node.get_next()
