from data_structures.trees import create_tree, level_order_traversal


def test_level_order_traversal_01():
    assert level_order_traversal(None) is None


def test_level_order_traversal_02():
    arr = [1]
    root = create_tree(arr)

    exp = [1]

    assert level_order_traversal(root) == exp


def test_level_order_traversal_03():
    arr = [6, 4, 8, 2, 5, 7, 9]
    root = create_tree(arr)

    exp = [6, 4, 8, 2, 5, 7, 9]

    assert level_order_traversal(root) == exp
