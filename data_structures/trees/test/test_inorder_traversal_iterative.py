from data_structures.trees import create_tree, inorder_traversal_iterative


def test_inorder_traversal_iterative():
    arr = [6, 4, 8, 2, 5, 7, 9, 1, 3]
    root = create_tree(arr)

    exp = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    assert inorder_traversal_iterative(root) == exp
