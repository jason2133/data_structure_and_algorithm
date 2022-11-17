# Stack 스택
# 쌓아놓은 더미
# 후입선출
# LIFO : Last In, First Out
# 가장 최근에 들어온 데이터가 가장 먼저 나감

# 삽입 push
# 삭제 pop

# 배열을 이용한 스택의 구현
# 가장 먼저 들어온 요소는 stack[0]에,
# 가장 최근에 들어온 요소는 stack[top]에 저장

def push(stack, item):
    stack.append(item)

def pop(stack):
    if len(stack) != 0:
        # stack.pop()이랑 stack.pop(-1)의 의미는 같음.
        item = stack.pop(-1)
        return item 
    else:
        empty()

def empty():
    print('Stack is Empty')

def top(stack):
    if len(stack) != 0:
        return stack[-1]
    else:
        empty()

if __name__ == '__main__':
    me = []
    pop(me)
    push(me, 'apple')
    push(me, 'orange')
    push(me, 'cherry')
    print(me)
    print(top(me))
    pop(me)
    print(me)

