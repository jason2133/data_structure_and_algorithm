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

def Post2Result(express):
    s = Stack(20)
    for i in express:
        if i not in '+-*/':
            s.push(i)
        else:
            second = s.pop()
            first = s.pop()
            s.push(str(eval(first+i+second)))
    print(s.data)
    return s.pop()

if __name__ == '__main__':
    express = input('enter your expression >> ').split()
    print(f'후위식 {express}의 결과는 {Post2Result(express)}')

