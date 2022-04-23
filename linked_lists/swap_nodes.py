"""Swap Elements in a Linked List

Given the pointer to the head of a singly linked list,
swap two elements in the list and return the pointer
to the head of the new list.

Input: [target1: 2, target2: 4], 1 -> 2 -> 3 -> 4 -> 5 -> None
Output: 1 -> 4 -> 3 -> 2 -> 5 -> None

Input: [target1: 1, target2: 3], 1 -> 2 -> 3 -> 4 -> 5 -> None
Output: 3 -> 2 -> 1 -> 4 -> 5 -> None

Input: [target1: 2, target2: 3], 1 -> 2 -> 3 -> 4 -> 5 -> None
Output: 1 -> 3 -> 2 -> 4 -> 5 -> None

Input: [target1: None, target2: 3], 1 -> 2 -> 3 -> 4 -> 5 -> None
Output: "Swap not possible"

Input: [target1: 2, target2: 3], None
Output: None
"""


class Solution:
    @staticmethod
    def swap_nodes(head, target1, target2):
        if head is None:
            return

        # Optional edge case
        if target1 is None or target2 is None:
            raise ValueError("Target values cannot be None")
            return

        node1_prev, node1 = Solution.swap_nodes_helper(head, target1)
        node2_prev, node2 = Solution.swap_nodes_helper(head, target2)

        if node1_prev is None:  # node1 is head
            head = node2
        else:
            node1_prev.set_next(node2)

        if node2_prev is None:  # node2 is head
            head = node1
        else:
            node2_prev.set_next(node1)

        temp1 = node1.get_next()
        temp2 = node2.get_next()

        node1.set_next(temp2)
        node2.set_next(temp1)

        return head

    @staticmethod
    def swap_nodes_helper(head, target):
        prev = None
        current = head
        while current:
            if current.get_value() == target:
                break
            prev = current
            current = current.get_next()

        return prev, current
