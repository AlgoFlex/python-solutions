"""Reverse a LinkedList

Given the pointer to the head of a singly linked list,
reverse the list and return the pointer to the new head.

Example 1:

Input: 1 -> 2 -> 3 -> None
Output: 3

Input: 1 -> None
Output: 1

Input: None
Output: None
"""


class Solution:
    @staticmethod
    def reverse_linked_list(head):
        prev_node = None
        current_node = head

        while current_node:
            temp = current_node.get_next()
            current_node.set_next(prev_node)
            prev_node = current_node
            current_node = temp

        return prev_node
