class node():
    def __init__(self, data=None):
        self.data = data
        self.next = None
        
class LL():
    def __init__(self):
        self.head = None
        self.tail = None
        self.tmp = None
        
    def add(self, data):
        nn = node(data)
        if self.head == None:
            self.head = nn
            self.tail = nn
        else:
            self.tail.next = nn
            self.tail = nn
    
    def length(self):
        tmp = self.head
        count = 0
        while(tmp):
            count += 1
            tmp = tmp.next
            
        return count
    
    def delete(self, ind):
        if self.head is None: return
        
        if ind>=self.length(): return
        if ind==0: self.head = self.head.next
        
        else:
            pos = 1
            tmp = self.head
            while(tmp and pos<ind):
                tmp = tmp.next
                pos += 1
            curr = tmp.next
            tmp.next = curr.next
            curr.next = None
        
    def output(self):
        if self.head is None:
            print(' ')
            return
        tmp = self.head
        while(tmp):
            print(tmp.data, end=' ')
            tmp = tmp.next

ll = LL()
lst = list(map(int, input().split()))
for i in lst:
    if i==-1: break
    ll.add(i)


ind = int(input())

ll.delete(ind)
ll.output()
