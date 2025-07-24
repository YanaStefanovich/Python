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

# ──────────────────────────────────────────────────────────
# 3. Create a dictionary result that counts how many times each character appears in the string text. (shortened version of original task)
def task_3() :
    text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'
    result = {}
    for el in text:
        result[el] = result.get(el, 0) + 1

# ──────────────────────────────────────────────────────────
# 4. From pets, build a dictionary result where each key is a tuple (first name, last name, age) of an owner, and the value is a list of their dogs' names in original order. (shortened version of original task)
def task_4() :
    pets = [('Hatiko', 'Parker', 'Wilson', 50),
            ('Rusty', 'Josh', 'King', 25),
            ('Fido', 'John', 'Smith', 28),
            ('Butch', 'Jake', 'Smirnoff', 18),
            ('Odi', 'Emma', 'Wright', 18),
            ('Balto', 'Josh', 'King', 25),
            ('Barry', 'Josh', 'King', 25),
            ('Snape', 'Hannah', 'Taylor', 40),
            ('Horry', 'Martha', 'Robinson', 73),
            ('Giro', 'Alex', 'Martinez', 65),
            ('Zooma', 'Simon', 'Nevel', 32),
            ('Lassie', 'Josh', 'King', 25),
            ('Chase', 'Martha', 'Robinson', 73),
            ('Ace', 'Martha', 'Williams', 38),
            ('Rocky', 'Simon', 'Nevel', 32)]
    result = {}
    for pet in pets:
        result.setdefault(pet[1:], []).append(pet[0])

# ──────────────────────────────────────────────────────────
# 5. Given a text string, find the least frequent word (case-insensitive). If multiple, return the lexicographically smallest one. (shortened version of original task)
def task_5() :
    s = [w.strip('.,;:-?!') for w in input().lower().split()]
    d = {s.count(i): i for i in sorted(s, reverse=True)}
    print(d[min(d)])


