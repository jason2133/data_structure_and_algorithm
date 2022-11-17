import heapq

def night_work(a, b):
    if b >= sum(a):
        return 0
    
    a = [-i for i in a]
    heapq.heapify(a)

    for i in range(b):
        i = heapq.heappop(a)
        i += 1
        heapq.heappush(a, i)
    
    result_1 = []
    for i in range(len(a)):
        result_1.append(-a[i])
    result_1 = sorted(result_1)

    result_2 = sum([i ** 2 for i in a])

    return result_1, result_2

if __name__ == '__main__':
    a = list(map(int, input('enter work load >> ').split()))
    b = int(input('enter remaining work times >> '))
    result_1, result_2 = night_work(a, b)
    print(result_1)
    print(result_2)
