# 구조체 개념 - 딕셔너리 표현

from collections import defaultdict

s = defaultdict(list)

for i in range(2):
    s['name'].append(input('enter name >> '))
    s['class_id'].append(input('enter id >> '))
    s['points'].append(input('enter point >> '))

for i in range(2):
    print(f"{s['name'][i]}: {s['class_id'][i]} & {s['points'][i]}")

