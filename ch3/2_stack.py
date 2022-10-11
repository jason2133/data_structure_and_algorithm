def push(stack, item):
    stack.append(item)

def pop(stack):
    if len(stack) != 0:
        # stack.pop()
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
    
    