from collections import deque
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    

def create(arr):
    if not arr: return
    
    root = Node(arr[0])
    ind = 1
    queue = deque([root])
    while queue and ind<len(arr):
        curr = queue.popleft()
        if arr[ind]!=-1:
            curr.left = Node(arr[ind])
            queue.append(curr.left)
        ind += 1

        if ind>=len(arr): break

        if arr[ind]!=-1:
            curr.right = Node(arr[ind])
            queue.append(curr.right)
        ind += 1
    
    return root

def is_bst(root, min_val = 0, max_val =0):
    if not root: return True

    if not min_val<root.data<max_val:
        return False
    
    return is_bst(root.left, min_val, root.data) and is_bst(root.right, root.data, max_val)

def height(root):
    if not root: return 0

    lh = height(root.left) if root.left else lh=0
    rh = height(root.right) if root.right else rh=0

    return 1+max(lh, rh)

def largest_bst(root):
    if not root: return 0 

    if(is_bst(root)): return height(root)

    return max(largest_bst(root.left), largest_bst(root.right))

arr = list(map(str, input().split()))
root = create(arr)
print(largest_bst(root))