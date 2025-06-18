"""Stepik 8.5 - Has the number been encounted before?

Problem Statement:
    Given a string of numbers, output YES if a number has already appeared in the sequence, otherwise NO.

"""
a = input().split()
c = set()
for el in a:
    b = int(el)
    if b in c:
        print("YES")
        c.add(b)
    else:
        print("NO")
        c.add(b)
