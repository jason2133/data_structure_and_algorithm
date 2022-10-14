class Stack:
    def __init__(self, size):
        self.data = []
        self.size = size

    def isEmpty(self):
        return len(self.data) == 0
    
    def isFull(self):
        return len(self.data) == self.size
    
    def push(self, value):
        if not self.isFull():
            self.data.append(value)
        
    def pop(self):
        if not self.isEmpty():
            return self.data.pop()
    
    def peek(self):
        if not self.isEmpty():
            return self.data[-1]

'''
후위 표현식 계산 알고리즘

스택 s를 생성하고 초기화한다.
for 항목 in 후위표기식:
    do if (항목이 피연산자이면)
            push(s, item)
        if (항목이 연산자 op이면)
            then second <- pop(s)
                first <- pop(s)
                # op는 +-*/ 중 하나
                result <- first op second 
                push(s, result)
final_result <- pop(s);            
'''

'''
후위 표현식 계산 규칙

1. 수식을 왼쪽에서 오른쪽으로 스캔하여 피연산자이면 스택에 저장
2. 연산자이면 필요한 수만큼의 피연산자를 스택에서 꺼내 연산을 실행
3. 연산의 결과를 다시 스택에 저장

ex) 82/3-32*+는 7이 됨.
'''

def post_calculate(expression):
    s = Stack(20)
    for i in expression:
        if i == '+':
            second = s.pop()
            first = s.pop()
            result = first + second
            s.push(result)
        
        elif i == '-':
            second = s.pop()
            first = s.pop()
            result = first - second
            s.push(result)
        
        elif i == '*':
            second = s.pop()
            first = s.pop()
            result = first * second
            s.push(result)
        
        elif i == '/':
            second = s.pop()
            first = s.pop()
            result = first / second
            s.push(result)
        
        else:
            s.push(int(i))
    
    final_result = s.pop()
    return final_result

if __name__ == '__main__':
    express = input('Enter your expression >> ')
    result = post_calculate(express)
    print(result)
