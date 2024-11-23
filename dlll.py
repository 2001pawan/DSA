class Node:

    def __init__(self, data):

        self.data = data
        self.next = None
        self.prev = None

class doublelinkedlist:

    def __init__(self):

        self.head=None
        self.tail=None


    def append(self,data):

        new_node=Node(data)

        if not self.head:
            self.head=new_node
            self.tail=new_node

        else:
            self.tail.next=new_node
            new_node.prev=self.tail
            self.tail=new_node


    def print(self):

        current = self.head 
        elements = []

        while current:
            elements.append(current.data)
            current=current.next
        return elements


    def printopp(self):
    
        current = self.tail
        elements = []

        while current:
            elements.append(current.data)
            current=current.prev
        return elements
    

    def insert_head(self,data):

        added_node=Node(data)
        
        self.head.prev=added_node
        added_node.prev=None
        added_node.next=self.head
        self.head=added_node


    def insert_tail(self,data):
    
        added_node=Node(data)
        
        self.tail.next=added_node
        added_node.next=None
        added_node.prev=self.tail
        self.tail=added_node

    
    def add_after(self,data1,data):
        
        added_node=Node(data)

        current=self.head

        while current:
            if current.data == data1:
               added_node.next=current.next
               current.next=added_node
               added_node.prev=current
               added_node.next.prev = added_node 
               
               return
            
            current=current.next



states = [
    "Maine", 
    "New Hampshire", 
    "Massachusetts", 
    "Rhode Island", 
    "Connecticut", 
    "New York", 
    "New Jersey", 
    "Delaware", 
    "Maryland", 
    "District of Columbia", 
    "Virginia", 
    "North Carolina", 
    "South Carolina", 
    "Georgia", 
    "Florida"
]

dll=doublelinkedlist()

for state in states:
    dll.append(state)

dll.insert_head("added")
print(dll.print())
dll.add_after("Maryland","Pennsylvania")

print(dll.print())
print(dll.printopp())
