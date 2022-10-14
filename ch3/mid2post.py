from stack import Stack

def precedence(op):
    if op == '(' or op == ')':
        return 0
    elif op == '+' or op == '-':
        return 1
    
    # op % //
    elif op == '*' or op == '/':
        return 2
    else:
        return -1    

def Mid2Post(express):
    s = Stack(20)
    result = []
    for i in express:
        if i in '(':
            s.push('(')
        elif i in ')':
            while not s.isEmpty():
                op = s.pop()
                
                # 왼쪽 괄호가 나올 때까지 스택에서 연산자를 꺼냄
                if op == '(':
                    break

                else:
                    result.append(op)
        
        elif i in '+-*/':
            while not s.isEmpty():
                op = s.peek()
                
                if (precedence(i) <= precedence(op)):
                    result.append(op)
                    s.pop()

                else:
                    break
            
            # 현재 연산자 입력
            s.push(i)
        
        else:
            # 피연산자이면 바로 출력
            result.append(i)
        
    while not s.isEmpty():
        result.append(s.pop())
    
    return result

# 중위표현에서 후위표현 변경 확인 메인 코드
express = input('Enter your expression >> ')
print(Mid2Post(express))
