# Question 2) Implement a stack using a linked list. The stack should have methods for push, pop, peek, is_empty, maximum, and minimum 

class Node:

    def __init__(self,data):
        self.data=data
        self.next=None


class stack:

    def __init__(self):
        self.top=None


    def push(self,data):

        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node


    def show(self):

        current=self.top
        elements=[]

        while current:
            elements.append(current.data)
            current=current.next

        return elements

    def pop(self):

        print("hello")
        self.top=self.top.next
        return self.top


        



    # def peek(self,data):



    # def is_empty(self):

    


    # def maximum(self):

    

    # def minimum(self):


s=stack()
s.push(1)
s.push(99)
s.push(111)
print(s.show())


s.pop()
print(s.show())
        



 
    