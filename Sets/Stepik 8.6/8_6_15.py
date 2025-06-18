"""Stepik 8.6 - Common numbers

Problem Statement:
    Given "a" distinct natural numbers, print all digits that appear in **every** number, in ascending order. If there are none, print nothing.

"""
a = int(input())
c = set(list(str(int(input()))))
for i in range(a - 1):
    c = c & set(list(str(int(input()))))
print(*sorted(c))
