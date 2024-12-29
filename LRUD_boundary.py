class Chess:

    def __init__(self):
        self.position=[0,0]#[x,y]
        self.i=4
        self.j=4

    def Move(self,direction):
       
        #if x,y are inside range 0,0 to i,j we need to update
        #else not update and return -1
        x,y = self.position[0],self.position[1]
                
        if direction == 'L':
            x -=1

        elif direction == 'R':
            x +=1

        elif direction == 'U':
            y -=1

        elif direction == 'LD':
            x -=1
            y +=1

        elif direction == 'LU':
            x -=1
            y -=1

        elif direction == 'RD':
            x +=1
            y +=1

        elif direction == 'RU':
            x +=1
            y -=1

        elif direction == 'D':
            y +=1

        else:
            return -1

        if x in range(0,self.i) and y in range(0,self.j):
            self.position=[x,y]
            return self.position
        
        else:
            return -1
        

       

print("using class:")
C=Chess()
x=C.Move('L')
print(x)
x=C.Move('RD')
print(x)
x=C.Move('RU')
print(x)
x=C.Move('R')
x=C.Move('R')
x=C.Move('R')
x=C.Move('R')
print(x)
x=C.Move('D')
print(x)
