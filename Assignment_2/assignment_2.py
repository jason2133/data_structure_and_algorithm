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
