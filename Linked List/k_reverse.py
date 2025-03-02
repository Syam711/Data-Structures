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
    
    def reverseIt(self, head, k):
        
        if not head or k==0: return head
        
        tmp, count = head, 0
        while tmp and count<k:
            tmp = tmp.next
            count += 1
        
        prev, curr = None, head
        for _ in range(count):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        head.next = self.reverseIt(curr, k)
        return prev
    
    def output(self):
        tmp = self.head
        while(tmp):
            print(tmp.data, end=' ')
            tmp = tmp.next

ll = LL()
lst = list(map(int, input().split()))
for i in lst:
    if i==-1: break
    ll.add(i)


k = int(input())

ll.head = ll.reverseIt(ll.head, k)
ll.output()
