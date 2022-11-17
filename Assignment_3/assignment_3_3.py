import heapq

def night_work(a, b):
    if a >= sum(b):
        return 0
    
    b = [-i for i in b]
    heapq.heapify(b)

    for i in range(a):
        i = heapq.heappop(b)
        i += 1
        heapq.heappush(b, i)
    
    result_1 = []
    for i in range(len(b)):
        result_1.append(-b[i])

    result_2 = sum([i ** 2 for i in b])

    return result_1, result_2

if __name__ == '__main__':
    a = int(input('enter remaining work times >>'))
    b = list(map(int, input().split('enter work load >>')))
    result_1, result_2 = night_work(a, b)
    print(result_1)
    print(result_2)
