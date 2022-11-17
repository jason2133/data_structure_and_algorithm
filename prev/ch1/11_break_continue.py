# Break 및 Continue문

fact = 1
n = 0
n = int(input('factorial 정수 입력 >> '))

for n in range(1, n+1):
    fact *= n
    print("n : %d, 누적곱: %d" % (n, fact))
    # break
