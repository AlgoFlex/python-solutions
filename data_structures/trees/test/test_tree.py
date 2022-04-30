from data_structures.trees import Tree


def test_init_without_value():
    tree = Tree()

    assert tree.get_root().get_value() is None


def test_init_with_value():
    tree = Tree(1)

    assert tree.get_root().get_value() == 1
