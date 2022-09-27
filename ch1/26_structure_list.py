# 구조체 개념 - 리스트

s = []
# s = list()

for i in range(2):
    temp = input().split()
    s.append(temp)

print(s)

for data in s:
    print(f'{data[0]}: {data[1]} & {data[2]}')
