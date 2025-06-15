"""Stepik 8.5 - Counter of correct solutions to problems

Problem Statement:
    Given n submissions (<username>: Correct/Wrong), count unique users with at least one Correct and compute the percentage of correct attempts (rounded).
If no correct answers, print a special message.

"""

a = int(input())
correct = set()
corr = 0
for i in range(a):
    b = input()
    if b[b.find(':')+2] == 'C':
        correct.add(b[:b.find(':')])
        corr+=1
if correct == set():
    print('You can be the first to solve this problem')
else:
    print(f'{len(correct)} students answered correctly')
    print(f"Out of all attempts{int(corr/a*100 + 0.5)}% are correct")
