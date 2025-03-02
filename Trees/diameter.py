from collections import deque
class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
    
class Tree:
    def __init__(self):
        self.root = None
        self.maxi = 0
    def create(self, arr):
        if not arr: return
        
        ind = 0
        self.root = Node(arr[ind])
        queue = deque([self.root])
        ind += 1
        while queue and ind<len(arr)-1:
            curr = queue.popleft()
            curr.left = Node(arr[ind])
            queue.append(curr.left)
            ind += 1
            curr.right = Node(arr[ind])
            queue.append(curr.right)
            ind += 1
    def diameter(self, root):
        if not root: return 0
        
        lh = self.diameter(root.left)
        rh = self.diameter(root.right)
        
        self.maxi = max(self.maxi, rh+lh)
        
        return 1+max(lh, rh)
        
t = Tree()
arr = list(map(int, input().split()))
t.create(arr)
t.diameter(t.root)
print(t.maxi+1)