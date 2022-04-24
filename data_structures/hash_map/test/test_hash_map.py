from data_structures.hash_map import HashMap


def test_init():
    hash_map = HashMap()

    assert len(hash_map) == 10
    assert hash_map._array == [None for _ in range(10)]


def test_assign_retrieve():
    hash_map = HashMap()

    key = "foo"
    value = "bar"
    hash_map.assign(key, value)
    assert hash_map.retrieve(key) == value

    key = "bar"
    value = "baz"
    hash_map.assign(key, value)
    assert hash_map.retrieve(key) == value

    key = "baz"
    assert hash_map.retrieve(key) is None
