class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
    
class Tree:
    def __init__(self):
        self.root = None
        self.maxi = 0
    def insert(self, data):
        if not self.root: self.root = Node(data)
        else: self._insert(self.root, data)
            
    def _insert(self, root, data):
        if not root:
            return Node(data)
        if data<root.data:
            root.left = self._insert(root.left, data)
        elif data>root.data:
            root.right = self._insert(root.right, data)
        return root
    
    def diameter(self, root):
        if not root: return 0
        
        lh = self.diameter(root.left)
        rh = self.diameter(root.right)
        
        self.maxi = max(self.maxi, rh+lh)
        
        return 1+max(lh, rh)
        

t = Tree()

while 1:
    n = int(input())
    if n<0: break
    t.insert(n)

print('Diameter of the given binary tree is', t.diameter(t.root))
