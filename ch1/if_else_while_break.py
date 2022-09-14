# If - elif - else문
# while 및 break문

lst1 = [20, 30, 50]
sum = 0

num = len(lst1)

while num > 0:
    sum += lst1[num-1]
    num = num - 1

print(f'{lst1}의 합계는 {sum}')

while True:
    year = int(input('enter year >> '))
    if year <= 0:
        print('무한 루프인 while 문 종료')
        break
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f'{year}은 윤년')
    else:
        print(f'{year}은 평년')
