# 고객 등급 프로그램
# 판매금액이 300 이상이면 VIP, 아니면 Family

membership = ''
point = int(input('customer point >> '))

if point >= 300:
    membership = 'VIP'
else:
    membership = 'Family'

print(f'Customer membership is {membership}')

