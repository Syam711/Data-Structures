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
    
    def right_view(self, curr, lst, lvl=0):
        if not curr: return
        
        if len(lst)==lvl: lst.append(curr.data)
        
        self.right_view(curr.right, lst, lvl+1)
        self.right_view(curr.left, lst, lvl+1)
        

t = Tree()

while 1:
    n = int(input())
    if n<0: break
    t.insert(n)

lst = []
t.right_view(t.root, lst)
print(*lst)