class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = self.right = None
    
class Tree:
    def __init__(self):
        self.root = None
    
    def insert(self, arr):
        self.root = self._insert(arr, 0, len(arr)-1)

    def _insert(self, arr, start, end):
        if start>end: return 

        mid = (start+end)//2
        root = Node(arr[mid])
        root.left = self._insert(arr, start, mid-1)
        root.right = self._insert(arr, mid+1, end)

        return root
    
    def preorder(self):
        self._preorder(self.root)
    
    def _preorder(self, root):
        if not root: return

        print(root.data, end=' ')
        self._preorder(root.left)
        self._preorder(root.right)

t = Tree()
arr = list(map(int, input().split()))
t.insert(arr)
t.preorder()