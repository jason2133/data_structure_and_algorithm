# @dataclass 데코레이션으로 타입 힌트와 함께 활용함으로써
# 구조체 형태를 정의할 수 있음.

from dataclasses import dataclass
from typing import *

@dataclass
class Subject:
    name: str = None
    week: str = None
    credit: int = None

algorithms = Subject()
algorithms.credit = 3
print(f'Credit:: {algorithms.credit}')



