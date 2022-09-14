# If - elif - else문 (1)

n = input("enter integer >> ")
print(type(n))

num = int(input('enter integer'))
print(type(num))

if num > 10:
    result = num // 2
else:
    result = num % 2

print(f'result: {result}')

