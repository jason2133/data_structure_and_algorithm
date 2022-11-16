import heapq

def night_work(load, times):
    if times >= sum(load):
        return 0
    
    times = [-i for i in load]
    heapq.heapify(times)

    for i in range(load):
        k = heapq.heappop(load)
        k += 1
        heapq.heappush(load, k)
    
    ans_1 = load
    ans_2 = sum([i ** 2 for i in load])
    return ans_1, ans_2

if __name__ == '__main__':
    a = list(map(int, input().split()))
    b = int(input())
    result_1, result_2 = night_work(a, b)
    print(result_1)
    print(result_2)

# if __name__ == '__main__':
# 	a = list(map(int, input('enter remaining work times >>').split()))
#     b = int(input('enter work load >>'))

    # b = int(input('enter work load >>'))
	# result_1, result_2 = night_work(a, b)
	# print(result_1)
	# print(result_2)



