"""Stepik_solutions 10.3.12

Print the most frequent word in string s.
 If there's a tie, output the lexicographically smallest one.
 (shortened version of original task)
"""

s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'.split()
res = {}
result = {}
for el in s:
    result[el] = result.get(el,0)+1
a = max(result.values())
for i in result.items():
    if list(i)[1] ==a:
        res[list(i)[0]] = a
print(sorted(res)[0])