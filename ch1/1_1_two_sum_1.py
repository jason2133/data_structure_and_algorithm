from typing import *
import time

def twoSum(data: List[int], target: int) -> List[int]: # type hint
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            if data[i] + data[j] == target:
                return [i, j]

if __name__ == '__main__':
    start = time.time()
    a = list(map(int, input('Nums : ').split()))
    b = int(input('Target : '))
    value = twoSum(a, b)
    end = time.time()
    print(value)
    print(end - start)
