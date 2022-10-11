def check_bracket(text):
    stack = []
    
    for index, letter in enumerate(text):
        if letter == '(':
            stack.append(index)
        elif letter == ')':
            if stack:
                stack.pop()
            else:
                stack.append(index)
                return stack
    return stack

if __name__ == '__main__':
    exp = input('Input expression >> ')
    print(check_bracket(exp))
    
    