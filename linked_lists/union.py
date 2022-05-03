"""Union of Two Linked Lists

Given the pointers to the heads of two linked list,
find the union of two linked lists.

The union of two sets A and B is the set of elements
which are in A, in B, or in both A and B. For example,
the union of A = [1, 2] and B = [3, 4] is [1, 2, 3, 4].

Input:
A = [1, 2, 3]
B = [2, 3, 4]

Output: SinglyLinkedList([1, 2, 3, 4])
"""
from __future__ import annotations
from typing import TypeVar, Generic, Union
from data_structures.node import SinglyLinkedListNode
from data_structures.linked_list import SinglyLinkedList

T = TypeVar('T')


def union(head_1: SinglyLinkedList[T], head_2: SinglyLinkedListNode[T]) -> SinglyLinkedList[T]:
    pass
