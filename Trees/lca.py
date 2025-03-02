from collections import deque
class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = self.right = None

class Tree:
    def __init__(self):
        self.root = None
    
    def create(self, data):
        self.root = self._create(self.root, data)

    def _create(self, root, data):
        if not root: 
            return Node(data)
        
        if data<root.data:
            root.left = self._create(root.left, data)
        if data>root.data:
            root.right = self._create(root.right, data)
        
        return root
    
def lca(root, a, b):
    if not root: return 

    if root.data==a or root.data==b:
        return root

    l_lca = lca(root.left, a, b)
    r_lca = lca(root.right, a, b)

    if l_lca and r_lca:
        return root
    
    return l_lca if l_lca else r_lca

t = Tree()
arr = list(map(int, input().split()))
for i in range(len(arr)-1):
    t.create(arr[i])

a, b = map(int, input().split())
ancestor = lca(t.root, a, b)
print(ancestor.data if ancestor else -1)