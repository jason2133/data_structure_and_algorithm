# 랜덤 값이기 때문에 임의의 값이 생성된다.

import random

num = [random.randint(1, 10000) for i in range(20)]
print(num)
