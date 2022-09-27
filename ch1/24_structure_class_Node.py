class Node:
    def __init__(self, name, class_id, points):
        self.name = name
        self.class_id = class_id
        self.points = points
    
if __name__ == '__main__':
    s = []
    for i in range(2):
        s.append(Node(*input().split()))
    
    for i in range(2):
        s[i].points = float(s[i].points)
        print(f"{s[i].name}: {s[i].class_id} & {s[i].points:.2f}")
        
        