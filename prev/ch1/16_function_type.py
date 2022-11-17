# 1. 매개변수와 반환값이 모두 있는 경우
def multi1(a, b):
    result = a * b
    return result

m1 = multi1(5, 9)
print(m1)

# 2. 매개변수만 있는 경우
def multi2(a, b):
    result = a * b
    print(f'result: {result}')

multi2(5, 9)

# 3. 반환값만 있는 경우
def multi3():
    a = 5
    b = 9
    result = a * b
    return result

m3 = multi3()
print(m3)

# 4. 매개변수와 반환값이 모두 없는 경우
def multi4():
    a = 5
    b = 9
    result = a * b
    print(f'result: {result}')

multi4()
