import heapq

def solution(n, works):
	heap = []
	if sum(works) <= n:
		return 0
        
    #그냥 값 대신 (-값, 값)을 push하여 최대힙을 구현하였다. 
	for i in works:
		heapq.heappush(heap, (-i, i))
        
	for i in range(n):
		tmp = heapq.heappop(heap)
		tmp = (tmp[0]+1, tmp[1]-1)
		heapq.heappush(heap, tmp)
        
	ans = 0
	for i in heap:
		ans += i[1]*i[1]

	heap_ans = []
	for i in heap:
		heap_ans.append(i[1])

	return ans, heap_ans

if __name__ == '__main__':
	a = int(input('enter work load >>'))
	b = list(map(int, input('enter remaining work times >>').split()))
	result_1, result_2 = solution(a, b)
	print(result_1)
	print(result_2)
