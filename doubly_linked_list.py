class node:
    def __init__(self, data=None, prev=None, next=None):
        self.data=data
        self.prev=prev
        self.next=next
    
class dll:
    def __init__(self, start=None):
        self.start=start
    
    def is_empty(self):
        return self.start == None
    
    def insert_at_start(self, data):
        if self.is_empty():
            self.start = node(data)
        else:
            temp = node(data)
            temp.next=self.start
            temp.next.prev= temp
            self.start = temp
            
    def insert_at_last(self,data):
        if self.is_empty():
            self.start = node(data)
        else:
            temp= self.start
            t=node(data)
            while temp.next is not None:
                temp = temp.next
            temp.next= t
            t.prev = temp
    
    def insert_afterbefore(self, data,value, after=None, before=None):
        if self.is_empty():
            print('error, ll is empty')
        else:
            n= node(data)

            temp= self.start
            while temp is not None:
                if temp.data== value:
                    if after:
                        temp.next.prev=n
                        n.next=temp.next
                        temp.next=n
                    if before:
                        temp.prev.next=n
                        n.next=temp
                        temp.prev = n
                    break
                temp = temp.next
                
    
    def print_ll(self,reverse=0):
        if self.is_empty():
            print('error, ll is empty')
        else:
            if reverse==0:
                temp = self.start
                while temp is not None:
                    print(temp.data)
                    temp = temp.next
            else:
                temp=self.start
                while temp.next is not None:
                    temp = temp.next
                current = temp
                while current is not None:
                    print(current.data)
                    current = current.prev
            
                
l=dll()
l.insert_at_start(5)
l.insert_at_last(7)
l.insert_at_start(3)
l.insert_at_last(8)

l.insert_afterbefore(4,7,after=True)
l.insert_afterbefore(2,8,before=True)
print('forward')
l.print_ll()
print('reverse')
l.print_ll(reverse=1)    