def twosum(x, y, data):
    answer = []
    for i in range(x-1, y):
        answer.append(data[i])
    return sum(answer)

if __name__ == '__main__':
    a, b = map(int, input().split())
    data = list(map(int, input().split()))
    result = []
    for i in range(b):
        c, d = map(int, input().split())
        ans = twosum(c, d, data)
        result.append(ans)
    for i in range(len(result)):
        print(result[i])
