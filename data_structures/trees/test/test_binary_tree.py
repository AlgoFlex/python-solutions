from data_structures.trees import BinaryTree


def test_init_without_value():
    tree = BinaryTree()

    assert tree.get_root().get_value() is None


def test_init_with_value():
    tree = BinaryTree(1)

    assert tree.get_root().get_value() == 1
