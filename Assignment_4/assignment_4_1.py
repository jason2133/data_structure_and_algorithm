class Bst(object):
    def __init__(self):
        self.root = None
    
    def inorder_traversal(self, t):
        if t.item is not None:
            if t.left:
                self.inorder_traversal(t.left)
            print(str(t.item), ' ', end='')
        
            if t.right:
                self.inorder_traversal(t.right)
    
    def bst_remove(self, key):
        self.root, remove = self.remove_f(self.root, key)
        remove.left = remove.right = None
        return self.inorder_traversal(remove)
    
    def remove_f(self, t, key):
        if t.data == key:
            r_node = True
            if t.left and t.right:
                parent, child = t, t.right
                while child.left is not None:
                    parent, child = child, child.left
                child.left = t.left
                if parent != t:
                    parent.left = child.right
                    child.right = t.right
                t = child
            
            elif t.left or t.right:
                t = t.left or t.right
            
            else:
                t = None
        
        elif key > t.key:
            t.right, r_node = self.remove_f(t.right, key)
        
        elif key < t.key:
            t.left, r_node = self.remove_f(t.left, key)
        
        else:
            return None, None
        
        return t, r_node


