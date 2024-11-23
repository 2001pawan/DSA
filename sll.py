#SINGLE LINKED LIST 

class Node:

    def __init__(self,data):
        self.data = data
        self.next = None


class SingleLinkedList:

    def __init__(self):
        self.head = None


    def add_begining(self,data):
        added_node= Node(data)
        added_node.next=self.head
        self.head=added_node

    def add_end(self,data):
        added_node= Node(data)

        if not self.head: 
            self.head=added_node
            
        else: 
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=added_node
    
    def display(self):
        current=self.head
        while current:
            print(current.data)
            current=current.next
    
    def delete_beginning(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
        
    def delete_end(self):
        temp=self.head.next
        prev=self.head

        while temp.next:
            temp=temp.next
            prev=prev.next
        
        prev.next=None

    def delete_postion(self,pos):
        temp=self.head.next
        prev=self.head

        for i in range(1,pos-1):
            temp=temp.next
            prev=prev.next
        
        prev.next=temp.next
         
    # def testing(self):
    #     b=self.head.next.data
    #     print(b)

    def delete_key(self,key):
        temp=self.head.next
        prev=self.head

        if prev.data==key:
            self.head=prev.next
            prev=None
            return

        
        while temp and temp.data != key:
            temp=temp.next
            prev=prev.next
                
        
        if temp is None:
            print("no key")
            return

        prev.next=temp.next
        temp=None

        
        


            


    

s=SingleLinkedList()

s.add_end(1)
s.add_end(2)
s.add_begining(0)

s.display()
print("aaa")
s.delete_key(5)
s.display()

# s.delete_postion(2)
# s.display()

# s.delete_beginning()
# s.display()


# s.testing()

        

