"""
1-Having those 2 lists, print the list which contains elements, which are common for those 2 lists:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13].

2-Having dictionary:
{1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
Sort it ask and desc based on values;

3-Write a code, which will concat 2 dictionary into the one and sum up values for common keys.
dict1 = {1:10, 2:20}; disc2 = {1:20, 2:30}

4-Find top 3 dict keys which have the highest values.
{'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
"""

def task_1(a, b):
    c = set()

    for a_element in a:
        if a_element in b:
            c.add(a_element)

    return list(c)

def quick_sort_items(tuples_list, ascending=True):
    if len(tuples_list) <= 1:
        return tuples_list
    else:
        pivot = tuples_list[0][1]

        if ascending:
            before_pivot = [item for item in tuples_list[1:] if item[1] <= pivot]
            after_pivot = [item for item in tuples_list[1:] if item[1] > pivot]
        else:
            before_pivot = [item for item in tuples_list[1:] if item[1] >= pivot]
            after_pivot = [item for item in tuples_list[1:] if item[1] < pivot]

        return quick_sort_items(before_pivot, ascending) + [tuples_list[0]] \
                + quick_sort_items(after_pivot, ascending)

def task_2(dictionary):
    dictionary_asc = list(dictionary.items())
    dictionary_desc = list(dictionary.items())

    dictionary_asc = quick_sort_items(dictionary_asc, ascending=True)
    dictionary_desc = quick_sort_items(dictionary_desc, ascending=False)

    return dict(dictionary_asc), dict(dictionary_desc)

def task_3(dict1, dict2):
    dict3 = dict1.copy()

    for key, value in dict2.items():
        if key in dict3:
            dict3[key] += value
        else:
            dict3[key] = value

    return dict3

def task_4(dictionary):
    dictionary = list(dictionary.items())
    sorted_dictionary = quick_sort_items(dictionary, ascending=False)
    x, y, z = tuple(item[0] for item in sorted_dictionary[:3])
    return x, y, z
