def sum_index(a, b):
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i] + a[j] == b:
                c = [i, j]
                break
    return c

if __name__ == '__main__':
    a = list(map(int, input('Nums : ').split()))
    b = int(input('Target : '))
    value = sum_index(a, b)
    print(value)