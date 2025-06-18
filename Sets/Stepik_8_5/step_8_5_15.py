"""Stepik_solutions 8.5 - Counter of correct solutions to problems

Problem Statement:
    Given n submissions (<username>: Correct/Wrong), count unique users with at least one Correct and compute the percentage of correct attempts (rounded).
If no correct answers, print a special message.

"""
def counter_from_text(text):
    lines = text.strip().split('\n')
    a = int(lines[0])
    correct = set()
    corr = 0
    for b in lines[1:1 + a]:
        if b[b.find(":") + 2] == "C":
            correct.add(b[: b.find(":")])
            corr += 1
    if not correct:
        return "You can be the first to solve this problem"
    else:
        percent = int(corr / a * 100 + 0.5)
        return f"{len(correct)} students answered correctly \nOut of all attempts {percent}% are correct"




