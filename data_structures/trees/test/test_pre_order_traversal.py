from data_structures.trees import create_tree, pre_order_traversal


def test_pre_order():
    arr = [6, 4, 8, 2, 5, 7, 9, 1, 3]
    root = create_tree(arr)

    exp = [6, 4, 2, 1, 3, 5, 8, 7, 9]

    assert pre_order_traversal(root) == exp
