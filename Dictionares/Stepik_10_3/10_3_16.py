"""Stepik_solutions 10.3.16

Given a string of identifiers, make them unique by appending _n to duplicates
(where n is the count of prior occurrences). (shortened version of original task)

"""

a = input().split()
res = {}
for el in a:
    res[el] = res.get(el, -1) + 1
    if res[el] > 0:
        print(el, '_', res[el], sep='', end=' ')
    else:
        print(el, end=' ')
