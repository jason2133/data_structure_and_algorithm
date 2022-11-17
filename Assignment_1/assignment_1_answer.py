import sys

if __name__ == '__main__':
    scan = sys.stdin.readline
    num, count = [int(i) for i in scan().split()]
    
    data = [int(i) for i in scan().split()]
    pre_sum = [0]
    add = 0
    result = []
    for i in data:
        add += i
        pre_sum.append(add)
    
    for i in range(count):
        start, end = [int(i) for i in scan().split()]
        result.append(pre_sum[end] - pre_sum[start-1])
    
    print(f'[result]')
    for i in result:
        print(i)
