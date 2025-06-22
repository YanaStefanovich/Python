"""Stepik_solutions 10.2 - Small tasks - Dictionaries

Here are the problem statements and solutions to small exercises from the "Generation Python" course.
The problem statements have also been translated literally into English.

"""

# ──────────────────────────────────────────────────────────
# 1. Print names (sorted) of users who have no email key. Output in one line, space-separated.
def task_1() :
    users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
             {'name': 'Helga', 'phone': '555-1618'},
             {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
             {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
             {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
             {'name': 'John', 'phone': '233-421-32', 'email': ''},
             {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
             {'name': 'Alina', 'phone': '+7948-799-2434'},
             {'name': 'Robert', 'phone': '420-2011', 'email': ''},
             {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
             {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
             {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
             {'name': 'Roman', 'phone': '+7459-145-8059'},
             {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
             {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
             {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]
    list = []
    for el in users:
        if 'email' in el:
            if el['email'] == '':
                list.append(el['name'])
        else:
            list.append(el['name'])
    print(*sorted(list))

# ──────────────────────────────────────────────────────────
# 2. Convert a natural number to a string where each digit is replaced with its English word (e.g., 203 → two zero three). Output space-separated words.
def task_2() :
    d = {
        '0': "zero",
        '1': "one",
        '2': "two",
        '3': "three",
        '4': "four",
        '5': "five",
        '6': "six",
        '7': "seven",
        '8': "eight",
        '9': "nine"
    }
    for el in str(int(input())):
        print(d[el], end=' ')

# ──────────────────────────────────────────────────────────
# 3. Given a course code, print its classroom number, instructor name, and time. Use a predefined course info dictionary.
def task_3() :
    my_dict = {
        'CS101': ('3004', 'Heinz', '8:00'),
        'CS102': ('4501', 'Alvarado', '9:00'),
        'CS103': ('6755', 'Rich', '10:00'),
        'NT110': ('1244', 'Berk', '11:00'),
        'CM241': ('1411', 'Lee', '13:00'),
    }

    course_number = input()
    audience, teacher, time = my_dict[course_number]
    print(f'{course_number}: {audience}, {teacher}, {time}')



