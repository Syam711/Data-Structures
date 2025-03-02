from collections import deque
class node:
    def __init__(self, data=None):
        self.data = data
        self.left = None 
        self.right = None
    
class tree:
    def __init__(self, data):
        self.root = node(data)
    
    def create(self, arr):
        if not arr:
            return 
        
        queue = deque([self.root])
        i=1

        while(i<len(arr)):
            parent = queue.popleft()

            if(i<len(arr)):
                parent.left = node(arr[i])
                queue.append(parent.left)
                i += 1
            if(i<len(arr)):
                parent.right = node(arr[i])
                queue.append(parent.right)
                i += 1
        
    def output(self):
        if not self.root: return

        queue = deque([self.root])
        while queue:
            curr = queue.popleft()
            print(curr.data, end=' ')
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
            print()
    
arr = [1,2,3,4,5]

t = tree(arr[0])
t.create(arr)
t.output()
            


