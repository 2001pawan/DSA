 #stack implementation using linked list

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class queue:

    def __init__(self):
        self.front=None
        self.rear=None 


    def is_empty(self):
        return self.front== None


    def enqueue(self,data):
        
        item=Node(data)

        if self.rear is None:
            self.front=self.rear=item
        
        else:
            self.rear.next=item
            self.rear=item



    def dequeue(self):
        if self.is_empty():
            print("no items")
            return None
        
        else:
            a=self.front.data
            self.front=self.front.next
            
            if self.front is None:
                self.rear=None

            print("deqd",a)
            

    def peek(self):
        if self.is_empty():
            print("empty")
            return None
        return self.front.data

        

    def display(self):
        temp=self.front
        
        if self.is_empty():
            print("empty")
        
        else:
            while temp:
                print(temp.data)
                temp=temp.next
            
        




s=queue()
s.enqueue(1)
s.enqueue(2)
s.enqueue(3)
s.enqueue(4)
s.dequeue()
s.dequeue()
s.display()
print(s.is_empty())