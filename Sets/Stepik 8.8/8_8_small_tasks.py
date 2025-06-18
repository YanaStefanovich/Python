"""Stepik_solutions 8.8 - Small tasks - Set Comprehension

Here are the problem statements and solutions to small exercises from the "Generation Python" course.
The problem statements have also been translated literally into English.

"""

# ──────────────────────────────────────────────────────────
# 1. Set Comprehension - Use set comprehension to get unique values from items.
def task_1() :
    items = [10, '30', 30, 10, '56', 34, '12', 90, 89, 34, 45, '67', 12, 10, 90, 23, '45', 56, '56', 1, 5, '6', 5]
    a = {int(el) for el in items}
    print(*sorted(a))

# ──────────────────────────────────────────────────────────
# 2. Set Comprehension - Use set comprehension to get first letters (lowercase) of words in words. Print sorted result, space-separated.
def task_2() :
    words = ['Plum', 'Grapefruit', 'apple', 'orange', 'pomegranate', 'Cranberry', 'lime', 'Lemon', 'grapes',
             'persimmon', 'tangerine', 'Watermelon', 'currant', 'Almond']
    print(*sorted({el.lower()[0] for el in words}))

# ──────────────────────────────────────────────────────────
# 3. Set Comprehension - Use set comprehension to get unique lowercase words from sentence. Print sorted result, space-separated.
def task_3() :
    sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''
    print(*sorted({el.lower().strip('.,;:-?!)(') for el in sentence.split()}))

# ──────────────────────────────────────────────────────────
# 4. Set Comprehension - Use set comprehension to get unique words from sentence with length < 4. Convert to lowercase, sort, and print space-separated.
def task_4() :
    sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''
    print(*sorted({el.lower().strip('.,;:-?!)(') for el in sentence.split() if len(el.strip('.,;:-?!)(')) < 4}))

# ──────────────────────────────────────────────────────────
# 5. Set Comprehension - Use set comprehension to get unique .png filenames from files, case-insensitive. Print lowercase names with extension, sorted and space-separated.
def task_5() :
    files = ['python.png', 'qwerty.py', 'stepik.png', 'beegeek.org', 'windows.pnp', 'pen.txt', 'phone.py', 'book.txT',
             'board.pNg', 'keyBoard.jpg', 'Python.PNg', 'apple.jpeg', 'png.png', 'input.tXt', 'split.pop',
             'solution.Py', 'stepik.org', 'kotlin.ko', 'github.git']
    print(*sorted({el.lower() for el in files if el[-4::].lower() == '.png'}))









