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
        while(tmp!=None):
            count += 1
            tmp = tmp.next
        return count
    
    def arrange(self):
        odd_st = odd_end = None
        even_st = even_end = None
        
        tmp = self.head
        while(tmp):
            if tmp.data%2 == 0:
                if even_st==None:
                    even_st = even_end = tmp
                else:
                    even_end.next = tmp
                    even_end = tmp
            if tmp.data%2 != 0:
                if odd_st==None:
                    odd_st = odd_end = tmp
                else:
                    odd_end.next = tmp
                    odd_end = tmp
                    
            tmp = tmp.next
        
        if even_end: 
            even_end.next = None 
        if odd_end: 
            odd_end.next = None  
        
        if odd_st == None:
            self.head = even_st
        elif even_st == None:
            self.head = odd_st
        else:
            odd_end.next = even_st
            self.head = odd_st
            
    
        
    def output(self):
        tmp = self.head
        while(tmp!=None):
            print(tmp.data, end=' ')
            tmp = tmp.next
        
ll = LL()
lst = list(map(int, input().split()))
for i in lst:
    if i==-1: break
    ll.add(i)
    
ll.arrange()
ll.output()