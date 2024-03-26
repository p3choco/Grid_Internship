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

def task_1():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    a = set(a)
    b = set(b)
    c = a & b
    print(c)

def task_2():
    dictionary = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

    dictionary_asc = dict(sorted(dictionary.items(), key=lambda item: item[1]))
    dictionary_desc = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))

    print(dictionary_asc)
    print(dictionary_desc)

def task_3():
    dict1 = {1: 10, 2: 20, 7: 80}
    dict2 = {1: 20, 2: 30, 8: 90}
    dict3 = dict1.copy()

    for key, value in dict2.items():
        if key in dict3:
            dict3[key] += value
        else:
            dict3[key] = value
    print(dict3)

def task_4():
    dictionary = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}

    for i in range(3):
        key = max(dictionary, key=dictionary.get)
        value = dictionary.pop(key)
        print('Key: ', key, '   Value: ', value)
