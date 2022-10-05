from typing import List

N = 7

def insert(data: List[int], location: int, value: int):
    global count
    if location > N-1 or count > N:
        raise IndexError('인덱스가 초과되었습니다')
    
    for i in range(N-1, location, -1):
        data[i] = data[i-1]
    
    data[location] = value
    count += 1

def delete_(data, location) -> int:
    global count
    if location > N-1 or location < 0 or count == 0:
        raise IndexError('인덱스가 잘못되었습니다')
    else:
        temp = data[location]
        for i in range(location, N-1):
            data[i] = data[i+1]
        for i in range(count, N):
            data[i] = None
        count -= 1
    return temp

if __name__ == '__main__':
    data = [None] * N
    count = 0
    for i in range(4):
        data[i] = i * 10 + 10
        count += 1
    
    print(data, count)
    insert(data, 2, 123)
    insert(data, 4, 789)
    print(data, count)
    print(delete_(data, 2))
    print(data, count)
