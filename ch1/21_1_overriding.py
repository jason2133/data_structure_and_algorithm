# 객체지향의 특징
# 상속성과 다형성 (Python은 Overriding을 의미)
# 상속 : 특정 클래스의 모든 기능을 상속받아 사용하며 추가적인 기능을 작성하여 확정
# 파이썬은 다중상속을 지원함
# 오버라이딩 : 상속받은 기능 중에서 일부를 변경

from abc import *

class Add:
    def __init__(self, var1, var2):
        self.v1 = var1
        self.v2 = var2
    
    @abstractmethod
    def add_(self):
        pass

class Minus(metaclass=ABCMeta):
    def __init__(self, var1, var2):
        self.v1 = var1 + 10
        self.v2 = var2
    
    @abstractmethod
    def minus_(self):
        pass

class Calculator(Add, Minus):
    def add_(self):
        return self.v1 + self.v2
    def minus_(self):
        return self.v1 - self.v2

if __name__ == '__main__':
    first = Calculator(10, 6)
    print(first.add_())
    print(first.minus_())