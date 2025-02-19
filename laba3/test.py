import pytest
from your_module import unpack_recursive  # Замените на соответствующий путь к вашей функции

def test_flat_list():
    assert unpack_recursive([1, 2, 3]) == [1, 2, 3]

def test_nested_list():
    assert unpack_recursive([1, [2, [3]], 4]) == [1, 2, 3, 4]

def test_tuple():
    assert unpack_recursive((1, 2, 3)) == [1, 2, 3]

def test_nested_tuple():
    assert unpack_recursive((1, (2, (3, 4)), 5)) == [1, 2, 3, 4, 5]

def test_set():
    assert unpack_recursive({1, 2, 3}) == [1, 2, 3]  # Порядок элементов в множестве может варьироваться

def test_nested_set():
    assert unpack_recursive({1, (2, 3), [4, 5]}) == [1, 2, 3, 4, 5]  # Порядок может варьироваться

def test_dict():
    assert unpack_recursive({'a': 1, 'b': 2}) == ['a', 'b', 1, 2]

def test_nested_dict():
    assert unpack_recursive({'a': 1, 'b': {'c': 2}}) == ['a', 'b', 1, 'c', 2]

def test_mixed_types():
    assert unpack_recursive([1, (2, 3), {'a': 4, 'b': 5}, [6]]) == [1, 2, 3, 'a', 'b', 4, 5, 6]

def test_empty_list():
    assert unpack_recursive([]) == []

def test_empty_nested_structures():
    assert unpack_recursive([[], {}, (), set()]) == []
