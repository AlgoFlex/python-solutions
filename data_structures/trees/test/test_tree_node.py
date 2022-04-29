from data_structures.trees import TreeNode


def test_get_value():
    node = TreeNode()

    assert node.get_value() is None
    assert node._left is None
    assert node._right is None

    node = TreeNode(1)

    assert node.get_value() == 1
    assert node._left is None
    assert node._right is None


def test_set_value():
    node = TreeNode()

    assert node.get_value() is None

    node.set_value(1)

    assert node.get_value() == 1


def test_set_left_and_right_child():
    node = TreeNode(3)

    assert node._left is None
    assert node._right is None

    node.set_left_child(2)
    node.set_right_child(4)

    assert node._left.get_value() == 2
    assert node._right.get_value() == 4


def test_has_left_and_right_child():
    node = TreeNode(3)

    assert node.has_left_child() is False
    assert node.has_right_child() is False

    node.set_left_child(2)
    node.set_right_child(4)

    assert node.has_left_child() is True
    assert node.has_right_child() is True

