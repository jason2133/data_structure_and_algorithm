# 배열구조 이용 코드

# Python의 리스트는 List ADT를 동적 배열 방법으로 구성한 예이므로,
# 자료구조인 리스트의 장단점을 파악하기 위해서 정적인 리스트의 ADT를 구현함.

def head_insert(s, item):
    if s == []:
        s.append(item)
    else:
        s.append(None)
        size = len(s)
        for i in range(size, 1, -1):
            s[i-1] = s[i-2]
    
        s[0] = item

def insert_after(s, item, p):
    if p == len(s) - 1:
        s.append(item)
    else:
        s.append(None)
        size = len(s)
        for i in range(size, p+1, -1):
           s[i-1] = s[i-2]
        s[p] = item

if __name__ =='__main__':
    fruit = []
    head_insert(fruit, 'orange')
    head_insert(fruit, 'cherry')
    head_insert(fruit, 'banana')
    head_insert(fruit, 'blueberry')
    insert_after(fruit, 'apple', 1)
    insert_after(fruit, 'pear', 0)
    print(fruit)







