# List
# For문
# List에서의 Slicing


lst1 = [20, 30, 50]
sum = 0

for i in range(0, 10, 1):
    print(i, end=' ')
print()

for i in range(10):
    print(i, end='\t')
print()

for i in lst1:
    sum += i

print(f'{lst1}의 합계 : {sum}')

result = 0
for i in range(len(lst1)):
    result += lst1[i]

print(f'{lst1}의 합계 : {result}')


