class stack():
    def __init__(self):
        self.lst = []
        
    def isEmpty(self):
        return 1 if not self.lst else 0
    
    def push(self):
        self.lst.append('(')
    
    def pop(self):
        if not self.lst: return 0
        self.lst.pop()
        return 1
    
para = input()
s = stack()
for i in para:
    if i=='(':
        s.push()
    if i==')':
        if not s.pop(): 
            print('false')
            break
else:
    if s.isEmpty():
        print('true')
    else:
        print('false')
        
    