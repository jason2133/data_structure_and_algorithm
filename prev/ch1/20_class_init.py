class List_():
    def __init__(self):
        self.lst1 = []
    
    def add1(self, var):
        self.lst1.append(var)
    
    def delete1(self, var):
        return self.lst1.remove(var)

    def sort1(self):
        self.lst1.sort()
    
    def display(self):
        print(f'{self.lst1}')
    
if __name__ == '__main__':
    var1 = List_()
    var1.add1(10)
    var1.add1(5)
    var1.add1(40)
    var1.add1(20)
    var1.display()
    var1.sort1()
    var1.display()
    



