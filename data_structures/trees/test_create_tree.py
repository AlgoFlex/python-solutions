from data_structures.trees import create_tree


def test_create_tree():
    arr = [6, 4, 8, 2, 5, 7, 9]
    root = create_tree(arr)

    assert root.get_value() == 6
    assert root.get_left().get_value() == 4
    assert root.get_right().get_value() == 8
    assert root.get_left().get_left().get_value() == 2
    assert root.get_left().get_right().get_value() == 5
    assert root.get_right().get_left().get_value() == 7
    assert root.get_right().get_right().get_value() == 9
