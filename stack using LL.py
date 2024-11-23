 #stack implementation using linked list

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class stack:
    def __init__(self):
        self.top=None


    def is_empty(self):
        return self.top== None


    def push(self,data):
        # temp=self.top
        # item=Node(data)

        added_node= Node(data)
        added_node.next=self.top
        self.top=added_node

        # if self.is_empty():
        #     self.top=item
        
        # else:
        #     while temp.next:
        #         temp=temp.next
        #     temp.next=item


    def pop(self):#looks like peek is happening
        if self.is_empty():
            print("no items")

        else:
            temp=self.top
            self.top=temp.next
            temp.next=None
            # temp=self.top
            # while temp.next:
            #     temp=temp.next
            # a=temp.data
            # temp=None

        

    def display(self):
        temp=self.top
        
        if self.is_empty():
            print("empty")
            
        
        else:
            while temp is not None:
                print(temp.data,"av")
                temp=temp.next

        




s=stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
print(s.pop())
s.display()
print("aaa")
print(s.is_empty())