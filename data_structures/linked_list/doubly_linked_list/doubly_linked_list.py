from .doubly_linked_list_node import DoublyLinkedListNode


class DoublyLinkedList:
    def __init__(self, items=[]):
        self._head = None
        self._tail = None
        self._size = 0

        for item in items:
            self.append(item)

    def __len__(self):
        return self._size

    def __str__(self):
        formatted = "None<-"
        current_node = self._head
        while current_node:
            suffix = "<=>" if current_node.get_next() else "->None"
            formatted += f"{current_node.get_value()}{suffix}"
            current_node = current_node.get_next()
        return formatted

    def get_head(self):
        return self._head

    def get_tail(self):
        return self._tail

    """Adding to the Head
    
    First we check if there is a current head. If not, that means 
    the list is empty, and we can make the new node the head and
    the tail of the list.
    
    If there is a head to the list, we follow the following steps:
    First, set the new node's next pointer to the current head
    Second, set current head's previous pointer to the new node
    Lastly, set the list's head to the new node 
    """

    def prepend(self, value):
        new_node = DoublyLinkedListNode(value)

        if self._head is None:
            self._head = new_node
            self._tail = new_node
            self._size += 1
            return

        new_node.set_next(self._head)
        self._head.set_prev(new_node)
        self._head = new_node
        self._size += 1

    """Adding to the Tail
    
    Similarly, first we check if there is a current tail. If not, that means 
    the list is empty, and we can make the new node the head and
    the tail of the list.
    
    If there is a tail to the list, we follow the following steps:
    
    First, set the current tail's next pointer to the new node.
    Second, set new node's previous pointer to the current tail.
    Lastly, set the list's tail to the new node .
    """

    def append(self, value):
        new_node = DoublyLinkedListNode(value)

        if self._head is None:
            self._tail = new_node
            self._head = new_node
            self._size += 1
            return

        self._tail.set_next(new_node)
        new_node.set_prev(self._tail)
        self._tail = new_node
        self._size += 1

    """Removing the head
    
    Removing the head involves updating the pointer to the current
    head:
    
    First, we check that if there is a head to the list. If so,
    we set the current head the next node in the list.
    And then, we update its previous node pointer to None. 
    Then we make sure that we check if the tail also needs to be 
    updated. 
    """

    def remove_head(self):
        if self._head is None:
            return None

        removed_node = self._head
        self._head = removed_node.get_next()

        if self._head:
            self._head.set_prev(None)

        if removed_node == self._tail:
            self._tail = self._head  # equals to None

        self._size -= 1

        return removed_node

    """Removing the tail
    
    Similarly, removing the tail involves updating the pointer to the current
    tail:
    
    First, we check that if there is a tail to the list. If so,
    we set the current tail to the previous node in the list.
    And then, we update its next node pointer to None. 
    Then we make sure that we check if the head also needs to be 
    updated. 
    """

    def remove_tail(self):
        if self._tail is None:
            return

        removed_node = self._tail
        self._tail = self._tail.get_prev()

        if self._tail:
            self._tail.set_next(None)

        if removed_node == self._head:
            self._head = self._tail  # equals to None

        self._size -= 1

        return removed_node

    """
    Removing target value from the List

    We can also remove a node from anywhere in the list. 
    To do so, we need to update two pointers if the node is neither
    the head nor the head:

    Removed node’s preceding node’s next pointer and removed node’s
    following node’s previous pointer.

    There is no need to change the pointers of the removed node.
    If no nodes in the list are pointing to it, the node is orphaned.
    """

    def remove(self, target):
        if self._head is None:
            return None

        if self._head.get_value() == target:
            return self.remove_head()

        current_node = self._head
        next_node = current_node.get_next()
        while next_node:
            if next_node.get_value() == target:
                if next_node == self._tail:
                    return self.remove_tail()
                else:
                    current_node.set_next(next_node.get_next())
                    self._size -= 1
                    return next_node
            current_node = next_node
            next_node = next_node.get_next()

        return None
