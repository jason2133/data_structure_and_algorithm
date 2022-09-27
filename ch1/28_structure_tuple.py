##### 구조체 개념 - Tuple 표현
# collections 모듈의 namedtuple 사용
# 인덱스 외에도 키(key)로도 데이터에 접근할 수 있는 자료형
# tuple과 동일하게 불변의 성질을 가지고 있음.

# Profile = namedtuple(typename='Profile',
#                      field_names = ['name', 'age', 'city', 'phone'])

# temp = Profile()

profile = [('gildong', 20, '서울시', '01055555555'),
           ('young', 22, '부산시', '01055577777')]

print(profile[0])
print(profile[0][0])
print(profile[0][1])
print(profile[0][2])
print(profile[0][3])
print('-' * 50)
print(profile[1])
print(profile[1][0])
print(profile[1][1])
print(profile[1][2])
print(profile[1][3])
