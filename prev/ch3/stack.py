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
