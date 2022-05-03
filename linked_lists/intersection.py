"""Intersection of Two Linked Lists

Given the pointers to the heads of two linked list,
find the intersection of two linked lists

The intersection of two sets A and B, denoted by A ∩ B,
is the set of all objects that are members of both sets
A and B. For example, the intersection of A = [1, 2, 3]
and B = [2, 3, 4] is [2, 3].

Input:
A = [1, 2, 3]
B = [2, 3, 4]

Output: SinglyLinkedList([2, 3])
"""
from __future__ import annotations
from typing import TypeVar, Generic, Union
from data_structures.node import SinglyLinkedListNode
from data_structures.linked_list import SinglyLinkedList

T = TypeVar('T')


def intersection(head_1: SinglyLinkedList[T], head_2: SinglyLinkedListNode[T]) -> SinglyLinkedList[T]:
    pass
