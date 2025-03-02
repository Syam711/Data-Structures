class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LL:
    def __init__(self):
        self.head = None

    def insert(self, data):
        nn = Node(data)
        if self.head==None: 
            self.head = nn
        else:
            tmp = self.head
            while tmp.next!=None:
                tmp = tmp.next
            tmp.next = nn
    
    def output(self):
        tmp = self.head
        while tmp!=None:
            print(tmp.data, end=' ')
            tmp = tmp.next

ll = LL()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.output()