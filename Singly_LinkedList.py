class Node:
    def __init__(self,data=None, next=None):
        self.data=data
        self.next=next

class LL:
    def __init__(self, start=None):
        self.start=start
        
    def is_empty(self):
        return self.start==None
    
    def insert_at_start(self, data=None):
        if self.is_empty():
            self.start = Node(data)
        else:
            temp=Node(data)
            temp.next= self.start
            self.start=temp
    def insert_at_last(self, data=None):
        if self.is_empty():
            self.start = Node(data)
        else:
            temp=self.start
            while temp.next!=None:
                temp=temp.next
            temp.next = Node(data)
    def search(self, value):
        if self.is_empty():
            print('error, ll is empty')
        else:
            temp= self.start
            i=0
            while temp is not None:
                if temp.data ==value:
                    print('value is found at :',i)
                i+=1
                temp=temp.next
    def insert_after(self, fill, value):
        if self.is_empty():
            print('error, empty ll')
        else:
            temp= self.start
            while temp is not None:
                if temp.data==value:
                    t2=Node(fill)
                    t2.next=temp.next
                    temp.next = t2
                temp = temp.next

    def print_value(self):
        if self.is_empty():
            print('error, ll is empty')
        else:
            temp = self.start
            while temp is not None:
                print(temp.data, end=' ')
                temp=temp.next
        print()
                
    def __iter__(self):
        return LL_iter(self.start)
    
    def delete_first(self):
        if self.is_empty():
            print('error ll is empty')
        else:
            temp=self.start
            self.start = temp.next
    
    def delete_last(self):
        if self.is_empty():
            print('error, ll is empty')
        else:
            temp= self.start
            while temp.next.next is not None:
                temp = temp.next
            temp.next=None
            
    def delete_item(self, value):
        if self.is_empty():
            print('error, ll is empty')
        else:
            temp= self.start
            while temp.next is not None:
                if temp.next.data==value:
                    temp.next= temp.next.next
                temp= temp.next
                    

class LL_iter():
    def __init__(self, start):
        self.current=start
        
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.current is None:
            raise StopIteration
        data = self.current.data
        self.current= self.current.next
        return data
        
        

l=LL()
l.insert_at_start(5)
l.insert_at_start(3)
l.insert_at_start(1)
l.insert_at_last(9)
l.insert_after(10, 5)
l.insert_at_start(6)
l.insert_at_start(11)
l.insert_at_last(2)
l.insert_after(4, 5)
l.insert_at_start(12)
l.insert_at_start(7)
l.print_value()

l.delete_first()
l.print_value()
l.delete_item(6)
l.print_value()
l.delete_last()
l.print_value()

# print([i for i in l])
# l.search(5)

                
                
                
                
                
                
                
                
                
                