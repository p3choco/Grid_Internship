import tasks
import pytest

@pytest.mark.parametrize('a, b, expected_value', [
    ([1, 2, 3, 4], [3, 4, 5, 6], [3, 4]),
    ([10, 20, 30], [20, 30, 40, 50], [20, 30]),
    ([15, 22, 34], [22, 34, 56, 78], [34, 22]),
    ([2, 3, 5, 13], [3, 5, 8, 13, 21], [13, 3, 5]),
    ([100, 200], [200, 300, 400], [200]),
    ([4, 5], [5, 6, 7], [5])
])
def test_task_1_basic_case(a, b, expected_value):
    assert tasks.task_1(a,b) == expected_value

def test_task_1_no_common_elements():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [9, 10, 11, 12]

    assert tasks.task_1(a, b) == []

def test_task_1_empty_listst():
    a = []
    b = []

    assert tasks.task_1(a, b) == []

@pytest.mark.parametrize('dictionary, expected_asc, expected_desc', [
    pytest.param({1: 2, 3: 4, 4: 3, 2: 1, 0: 0}, {0: 0, 2: 1, 1: 2, 4: 3, 3: 4}, {3: 4, 4: 3, 1: 2, 2: 1, 0: 0}, id='basic_case'),
    pytest.param({'a': 3, 'b': 1, 'c': 2}, {'b': 1, 'c': 2, 'a': 3}, {'a': 3, 'c': 2, 'b': 1}, id='keys_as_letters'),
    pytest.param({}, {}, {}, id='empty_dict'),
    pytest.param({1: 10, 2: 20}, {1: 10, 2: 20}, {2: 20, 1: 10}, id='already_ascending'),
    pytest.param({'apple': 5, 'banana': 2, 'orange': 10, 'grapes': 7}, {'banana': 2, 'apple': 5, 'grapes': 7, 'orange': 10}, {'orange': 10, 'grapes': 7, 'apple': 5, 'banana': 2}, id='words_as_keys'),
    pytest.param({1: -1, 2: -2, 3: -3}, {3: -3, 2: -2, 1: -1}, {1: -1, 2: -2, 3: -3}, id='numbers_below_zero'),
    pytest.param({'a': 'z', 'b': 'y', 'c': 'x'}, {'c': 'x', 'b': 'y', 'a': 'z'}, {'a': 'z', 'b': 'y', 'c': 'x'}, id='values_and_keys_as_letters'),
])
def test_task_2(dictionary, expected_asc, expected_desc):
    assert tasks.task_2(dictionary) == (expected_asc, expected_desc)

def test_task_3_basic_case():
    dict1 = {1: 10, 2: 20}
    dict2 = {1: 20, 2: 30}
    assert tasks.task_3(dict1, dict2) == {1: 30, 2: 50}

def test_task_3_empty_dicts():
    dict1 = {}
    dict2 = {}
    assert tasks.task_3(dict1, dict2) == {}

def test_task_3_one_dict_empty():
    dict1 = {}
    dict2 = {1: 50}
    assert tasks.task_3(dict1, dict2) == {1: 50}

def test_task_3_no_common_keys():
    dict1 = {3: 30, 4: 40}
    dict2 = {1: 10, 2: 20}
    assert tasks.task_3(dict1, dict2) == {3: 30, 4: 40, 1: 10, 2: 20}

@pytest.mark.parametrize('test_input, expected_output', [
    pytest.param({'a':500, 'b':5874, 'c': 560, 'd':400, 'e':5874, 'f': 20}, ('e', 'b', 'c'), id='standard_case'),
    pytest.param({'g':10, 'h':20, 'i':30}, ('i', 'h', 'g'), id='minimal_case'),
    pytest.param({'j':300, 'k':200, 'l':100, 'm':300, 'n':300}, ('n', 'm', 'j'), id='tie_case'),
    pytest.param({'x': -10, 'y': -20, 'z': -5, 'w': -15}, ('z', 'x', 'w'), id='negative_values'),
    pytest.param({'g': 0.001, 'h': 0.002, 'i': 0.003, 'j': 0.0001}, ('i', 'h', 'g'), id='close_values'),
    pytest.param({'big1': 10**10, 'big2': 10**11, 'big3': 10**12, 'big4': 10**9}, ('big3', 'big2', 'big1'), id='large_numbers')
])
def test_task_4(test_input, expected_output):
    assert tasks.task_4(test_input) == expected_output