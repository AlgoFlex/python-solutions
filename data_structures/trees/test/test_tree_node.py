from data_structures.trees import TreeNode


def test_tree_node_01():
    node = TreeNode()

    assert node._value is None
    assert node._left is None
    assert node._right is None


def test_tree_node_02():
    node = TreeNode()

    assert node._value == 1
    assert node._left is None
    assert node._right is None
