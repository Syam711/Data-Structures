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
    
    def isPalindrome(self, tmp1):
        if tmp1==None: 
            self.tmp = self.head
            return True
        
        flag = self.isPalindrome(tmp1.next)
        if not flag:
            return False
        
        if self.tmp.data==tmp1.data:
            self.tmp = self.tmp.next
            return True
        else:
            
            return False
        

ll = LL()
lst = list(map(int, input().split()))
for i in lst:
    if i==-1: break
    ll.add(i)


print('true' if ll.isPalindrome(ll.head) else 'false')
        