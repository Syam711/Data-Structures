from collections import deque
class node:
    def __init__(self, data):
        self.data = data
        self.child = []
    
class tree:
    def __init__(self):
        self.root = None
    
    def create(self, arr):
        if not arr: return

        self.root = node(arr[0])
        ind = 1
        queue = deque([self.root])
        while ind<len(arr):
            curr = queue.popleft()
            n = arr[ind]
            ind += 1
            for _ in range(n):
                if ind>=len(arr): return
                nn = node(arr[ind])
                curr.child.append(nn)
                queue.append(nn)
                ind += 1     

def height(root):
    if not root: return 0
    max_height = 0
    
    for i in root.child:
        h = height(i)
        max_height = max(max_height, h)
    
    return max_height+1

t = tree()
arr = [0, 1, 0]
t.create(arr)
print(height(t.root))
