"""Stepik_solutions 10.3 - Small tasks - Dictionaries

Here are the problem statements and solutions to small exercises from the "Generation Python" course.
The problem statements have also been translated literally into English.

"""

# ──────────────────────────────────────────────────────────
# 1. Create a dictionary result where keys are numbers from 1 to 15, and values are their squares. (shortened version of original task)
def task_1() :
    result = {}
    for i in range(1, 16):
        result[i] = result.get(i, i) ** 2

# ──────────────────────────────────────────────────────────
# 2. Merge dict1 and dict2 into result: if a key exists in both, sum the values; if only in one, keep its value. (shortened version of original task)
def task_2() :
    dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
    dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}
    result = dict2.copy()
    for el in dict1:
        if el in result:
            result[el] += dict1[el]
        else:
            result[el] = dict1[el]


