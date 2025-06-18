"""Stepik_solutions 8.8 - Exam tasks

The tasks are taken from the practical part of the exam on sets from the Stepik_solutions platform, Generation Python: Advanced course.
Tasks have also been translated literally into English.

"""
# ──────────────────────────────────────────────────────────
# 1. Given n students, m whose homework was eaten by a dog, k who lost power, and p affected by both, find how many did the homework.
def task_1():
    print(int(input()) - int(input()) - int(input()) + int(input()))

# ──────────────────────────────────────────────────────────
# 2.Given a list of positive integers (satellite readings), remove duplicates. Output the maximum number of readings that can be removed without affecting analysis.
def task_2():
    a = input().split()
    b = set(a)
    print(len(a) - len(b))

# ──────────────────────────────────────────────────────────
# 3. Timur and Ruslan play a city-naming game. Track named cities and print a message when a city is repeated.
def task_3():
    a = int(input())
    b = {input() for el in range(a + 1)}
    if a + 1 == len(b):
        print('OK')
    else:
        print('REPEAT')

# ──────────────────────────────────────────────────────────
# 4. Given a summer reading list and a list of books Ruslan owns, check for each required book whether he has it or not.
def task_4():
    m, n = int(input()), int(input())
    libr = {input() for _ in range(m)}

    for _ in range(n):
        if input() in libr:
            print('YES')
        else:
            print('NO')

# ──────────────────────────────────────────────────────────
# 5. Timur writes numbers from two math problems on separate sheets. Find and print the common numbers, or print that the day was unsuccessful if there are none.
def task_5():
    a, b = set(input().split()), set(input().split())
    dig = {int(el) for el in a.intersection(b)}
    if dig == set():
        print('BAD DAY')
    else:
        print(*sorted(dig, reverse=True))

# ──────────────────────────────────────────────────────────
# 6. Given two lists — shown numbers and recalled numbers — check if the candidate named all and only the shown numbers, regardless of order or duplicates.
def task_6():
    if set(input().split()) == set(input().split()):
        print('YES')
    else:
        print('NO')

# ──────────────────────────────────────────────────────────
# 7. Find how many students study only math, given sets of those studying both math & CS (m) and CS (n).
def task_7():
    m, n = int(input()), int(input())
    MI = {input() for i in range(m)}
    INF = {input() for i in range(n)}
    print(len(MI - INF))

# ──────────────────────────────────────────────────────────
# 8. Given lists of students studying math and CS, find how many study only one of the subjects.
def task_8():
    m, n = int(input()), int(input())
    MI = {input() for i in range(m)}
    INF = {input() for i in range(n)}
    if MI ^ INF == set():
        print('NO')
    else:
        print(len(MI ^ INF))

# ──────────────────────────────────────────────────────────
# 9. Given two name lists from the director and assistant, print all common students they both remembered.
def task_9():
    print(*sorted(set(input().split()).union(set(input().split()))))

# ──────────────────────────────────────────────────────────
# 10. Given mixed lists of students studying math and CS, find how many study only one of the subjects.
def task_10():
    m, n = int(input()), int(input())
    lis = {input() for i in range(m + n)}
    result = len(lis) - (m + n - len(lis))
    if result == 0:
        print('NO')
    else:
        print(result)

# ──────────────────────────────────────────────────────────
# 11. Input: number of lessons, then for each lesson — number of students and their names. Output: names of students who attended every lesson.
def task_11():
    m, n = int(input()), int(input())
    a = {input() for j in range(n)}
    for i in range(m - 1):
        a = a.intersection({input() for j in range(int(input()))})
    print(*sorted(a), sep='\n')







