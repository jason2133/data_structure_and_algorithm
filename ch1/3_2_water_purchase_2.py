from typing import *

def waterCal(person: int, water: int) -> List[int]:
    pack = 12
    all = person * water
    answer_1 = all // pack
    answer_2 = all % pack
    price = 10000 * answer_1 + 800 * answer_2
    return answer_1, answer_2, price

if __name__ == '__main__':
    person, water = map(int, input().split())
    result = waterCal(person, water)
    print(result[0], result[1], result[2])
