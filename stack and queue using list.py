class stack:
    def __init__(self):
        self.stack=[]

    def is_empty(self):
        if len(self.stack)==0:
            print("empty")
        else:
            print("false")
        
    def push(self,item):
    
        self.stack.append(item)
    
    def pop(self):
        
        self.stack.pop()
    
    def display(self):

        print(self.stack)

    def peek(self):

        a=len(self.stack)
        print(self.stack[a-1]) 


# s=stack()
# s.is_empty()
# s.push(1)
# s.push(2)
# # s.pop()
# # s.display()
# s.peek()

class queue:
    
    def __init__(self):
        self.queue=[]

    def is_empty(self):
        return len(self.queue)==0

    def enqueue(self,item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            print("empty")
        else:
            return self.queue.pop(0)
    
    def display(self):
        print(self.queue)

q=queue()
q.dequeue()