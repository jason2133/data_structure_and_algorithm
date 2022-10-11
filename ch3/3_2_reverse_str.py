class string_stack:
    def __init__(self):
        self.string = []
    
    def push(self, item):
        self.string.append(item)
    
    def pop(self):
        if len(self.string) != 0:
            # stack.pop()
            item = self.string.pop(-1)
            return item
        else:
            print('Stack is Empty')
    
    def empty(self):
        if self.string == []:
            return False
        else:
            return True
    
    def top(self):
        if len(self.string) != 0:
            return self.string[-1]
        else:
            print('Stack is Empty')

if __name__ == '__main__':
    str1 = string_stack()
    str1.push('A')
    str1.push('B')
    str1.push('C')
    str1.push('D')
    data = ''
    for i in range(len(str1.string)):
        data += str1.pop()
    print(data)
    