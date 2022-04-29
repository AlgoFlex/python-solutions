from typing import TypeVar, Generic, Union

T = TypeVar('T')


class TreeNode(Generic[T]):
    def __init__(self, value: Union[T, None] = None) -> None:
        self._value = value
        self._left: Union[TreeNode, None] = None
        self._right: Union[TreeNode, None] = None

    def get_value(self) -> Union[T, None]:
        return self._value

    def set_value(self, value: Union[T, None] = None) -> None:
        self._value = value

    def set_left_child(self, value: Union[T, None] = None) -> None:
        self._left = TreeNode(value)

    def set_right_child(self, value: Union[T, None] = None) -> None:
        self._right = TreeNode(value)

    def has_left_child(self) -> bool:
        return self._left is not None

    def has_right_child(self) -> bool:
        return self._right is not None
