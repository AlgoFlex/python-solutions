from __future__ import annotations
from typing import Generic, TypeVar, Union

T = TypeVar('T')


class Node(Generic[T]):
    def __init__(self, value: T) -> None:
        self._value = value

    def get_value(self) -> T:
        return self._value
