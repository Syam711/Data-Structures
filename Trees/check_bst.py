from collections import deque
class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
    
class Tree:
    def __init__(self):
        self.root = None
        
    def create(self, arr):
        if not arr: return
        
        ind = 0
        self.root = Node(arr[ind])
        queue = deque([self.root])
        ind += 1
        while queue:
            curr = queue.popleft()
            if ind<len(arr) and arr[ind]!=-1:
                curr.left = Node(arr[ind])
                queue.append(curr.left)
            ind += 1
            if ind<len(arr) and arr[ind]!=-1:
                curr.right = Node(arr[ind])
                queue.append(curr.right)
            ind += 1
        
def check_bst(root, min_val=float('-inf'), max_val=float('inf')):
    if not root:
        return True
    
    if not (min_val < root.data < max_val):
        return False 

    return (check_bst(root.left, min_val, root.data) and
            check_bst(root.right, root.data, max_val))

    
    

arr = list(map(int, input().split()))
t = Tree()
t.create(arr)
print(check_bst(t.root))