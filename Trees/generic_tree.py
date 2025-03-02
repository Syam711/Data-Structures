from collections import deque
class Node:
    def __init__(self, data=None):
        self.data = data
        self.children = []
    
class Tree:
    def __init__(self):
        self.root = None

    def insert(self, arr):
        if not self.root: 
            self.root = Node(arr[0])
        
        queue = deque([self.root])
        ind = 1
        while queue:
            curr = queue.popleft()
            n = arr[ind]
            ind += 1
            for _ in range(n):
                nn = Node(arr[ind])
                curr.children.append(nn)
                queue.append(nn)
                ind += 1
            
    
t = Tree()
