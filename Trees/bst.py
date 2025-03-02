class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
    
class Tree:
    def __init__(self):
        self.root = None
    
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
    
    def inorder(self):
        self._inorder(self.root)
    def _inorder(self, root):
        if not root: return

        self._inorder(root.left)
        print(root.data, end=' ')
        self._inorder(root.right)
    
    def search(self, key):
        if not self.root:
            return False
        else:
            return self._search(self.root, key)
    
    def _search(self, root, key):
        if not root:
            return 'false'
        else:
            if root.data==key:
                return 'true'
            if root.data>key:
                return self._search(root.left, key)
            elif root.data<key:
                return self._search(root.right, key)
        
    def delete(self, val):
        self.root = self._delete(self.root, val)
        
    def _delete(self, root, val):
        if not root:
            return None
        
        if root.data>val:
            root.left = self._delete(root.left, val)
        elif root.data<val:
            root.right = self._delete(root.right, val)
        else:
            
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                succ = self.fetch(root.right)
                root.data = succ.data
                root.right = self._delete(root.right, succ.data)
        
        return root
    def fetch(self, curr):
        while curr.left:
            curr = curr.left
        return curr
        

t = Tree()
t.insert(4)
t.insert(2)
t.insert(3)
t.insert(1)
t.insert(5)
t.insert(6)
t.insert(8)
t.inorder()
print(t.search(1))
t.delete(4)
t.inorder()
print(t.root.data)

