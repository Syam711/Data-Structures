class queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []
        
    def insert(self, data):
        self.s1.append(data)
        
    def delete(self):
        if not self.s2:
            if not self.s1: return -1
            while self.s1:
                self.s2.append(self.s1.pop())
        self.s2.pop()
    
    def front(self):
        if not self.s2:
            if not self.s1: return -1
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]
        
n = int(input())
q = queue()
for _ in range(n):
    inp = list(map(int, input().split()))
    if inp[0]==1:
        q.insert(inp[1])
    elif inp[0]==2:
        q.delete()
    else:
        print(q.front())
        