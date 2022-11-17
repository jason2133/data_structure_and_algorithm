import random
from typing import *

# def guess(com_n: set) -> List[bool]:
def guess():
    result = []
    computer_num = []
    my_num = []
    for i in range(3):
        r = random.randint(1, 30)
        point = int(input('your number >> '))
        computer_num.append(r)
        my_num.append(point)
        if r == point:
            result.append('True')
        else:
            result.append('False')
    return result, computer_num, my_num

if __name__ == '__main__':
    ans = guess()
    print(f'Result : {ans[0]}')
    print(f'Computer Number : {ans[1]}')
    print(f'My Number : {ans[2]}')
