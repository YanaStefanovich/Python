"""Stepik 8.7 - Small tasks - Python Set Methods

Here are the problem statements and solutions to small exercises from the "Generation Python" course.
The problem statements have also been translated literally into English.

"""

# ──────────────────────────────────────────────────────────
# 1. isdisjoint() - Given two numbers, check if they share at least one common digit.
def task_1() :
    a, b = set(input()), set(input())
    if a.isdisjoint(b) == True:
        print('NO')
    else:
        print('YES')
# ──────────────────────────────────────────────────────────
# 2. issuperset() - Given two numbers, check if all digits of the second number are present in the first number.
def task_2():
    a, b = set(input()), set(input())
    if a.issuperset(b) == True:
        print('YES')
    else:
        print('NO')
# ──────────────────────────────────────────────────────────
# 3. Computer Science lesson - Given scores (0–10) of three students, print the set of grades shared by the first and second students but not by the third.
def task_3():
    set1 = set(int(i) for i in input().split())
    set2 = set(int(i) for i in input().split())
    set3 = set(int(i) for i in input().split())

    print(*sorted(set1 & set2 - set3, reverse=True))
# ──────────────────────────────────────────────────────────
# 4. Maths lesson - Given math scores of three students (0–10), print grades that appear in no more than two of them.
def task_4():
    set1 = set(int(i) for i in input().split())
    set2 = set(int(i) for i in input().split())
    set3 = set(int(i) for i in input().split())

    result = set1.intersection(set2, set3)

    print(*sorted(set1.union(set2, set3) - result))

# ──────────────────────────────────────────────────────────
# 5. Physics lesson - Given physics scores of three students (0–10), print grades of the third student that are **not present** in the first or second.
def task_5():
    set1 = set(int(i) for i in input().split())
    set2 = set(int(i) for i in input().split())
    set3 = set(int(i) for i in input().split())
    res = set3 - set2 - set1
    print(*sorted(res, reverse=True))
# ──────────────────────────────────────────────────────────
# 6. Biology lesson - Given biology scores (0–10) of three students, print grades that none of them have.
def task_6():
    set1 = set(int(i) for i in input().split())
    set2 = set(int(i) for i in input().split())
    set3 = set(int(i) for i in input().split())
    set4 = set(range(0, 11))
    res = set4 - set1.union(set2, set3)
    print(*sorted(res))
