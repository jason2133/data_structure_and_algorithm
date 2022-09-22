# List, Dictionary에 Comprehension 적용

odd_n_1 = [i for i in range(1, 21, 2)]
odd_n_2 = [i for i in range(21) if i % 2 != 0]

print(odd_n_1)
print(odd_n_2)

data = [i for i in range(1, 101) if i % 3 == 0]
print(data)

data = [ "even" if i % 2 == 0 else "odd" for i in range(1,21)]
print(data)

# 1~10000 사이의 정수를 랜덤하게 20개 생성하는 리스트 컴프리헨션 코드
import random
# random.seed(777)
data = [ random.randint(1,10000) for i in range(20)] #randrange(1,10001)
print(data)

# enumerate : 인덱스를 가지는 집합형 자료형에 적용되는 내장함
data = [3,1,7,4,8,9,10,2,11,15,18,21,22,14,6]
result = enumerate(data)
for i in result:
    print(i)

result = [(i,value) for i, value in enumerate(data)]
print(result)
