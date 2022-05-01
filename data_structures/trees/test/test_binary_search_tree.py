from data_structures.trees import BinarySearchTree


def test_binary_search_tree_init():
    bst = BinarySearchTree()
    assert bst.get_value() is None

    bst = BinarySearchTree(1)

    assert bst.get_value() == 1


def test_binary_search_tree_insert():
    bst_parent = BinarySearchTree(5)
    bst_left_child_01 = 3
    bst_left_child_02 = 2
    bst_left_child_03 = 4
    bst_right_child_01 = 7
    bst_right_child_02 = 6
    bst_right_child_03 = 8

    bst_parent.insert(bst_left_child_01)
    bst_parent.insert(bst_left_child_02)
    bst_parent.insert(bst_left_child_03)
    bst_parent.insert(bst_right_child_01)
    bst_parent.insert(bst_right_child_02)
    bst_parent.insert(bst_right_child_03)

    assert bst_parent.get_left().get_value() == 3
    assert bst_parent.get_right().get_value() == 7

    bst_left_child = bst_parent.get_left()
    assert bst_left_child.get_left().get_value() == 2
    assert bst_left_child.get_right().get_value() == 4

    bst_right_child = bst_parent.get_right()
    assert bst_right_child.get_left().get_value() == 6
    assert bst_right_child.get_right().get_value() == 8


def test_binary_search_tree_find():
    bst = BinarySearchTree(100)
    bst.insert(50)
    bst.insert(125)
    bst.insert(25)
    bst.insert(75)

    assert bst.find(150) is None
    assert bst.find(100).get_value() == 100
    assert bst.find(25).get_value() == 25
    assert bst.find(125).get_value() == 125
    assert isinstance(bst.find(125), BinarySearchTree) is True

