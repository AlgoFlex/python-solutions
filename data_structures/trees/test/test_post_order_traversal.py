from data_structures.trees import create_tree, post_order_traversal


def test_post_order_traversal():
    arr = [6, 4, 8, 2, 5, 7, 9, 1, 3]
    root = create_tree(arr)

    exp = [1, 3, 2, 5, 4, 7, 9, 8, 6]

    assert post_order_traversal(root) == exp
