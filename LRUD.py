# >Imagine euta chessboard 2D- tya euta piece xa. 0,0
# Input - L, R, U, D
# Print current location based on input

current_direction=[0,0]#this should be updated//x,y?

def Move(direction):

    if direction == 'L':
        current_direction[0] -=1

    elif direction == 'R':
        current_direction[0] +=1

    elif direction == 'L':
        current_direction[1] -=1

    else :
        current_direction[1] +=1    

    # new_direction=[current_direction[0],current_direction[1]]

    return current_direction

a=Move('L')
print(a)
a=Move('R')
print(a)
a=Move('U')
print(a)
a=Move('R')
a=Move('R')
print(a)
#latest position is not retained?
#the function should be given the latest position as argument. 

class Chess:

    def __init__(self):
        self.position=[0,0]

    def Move(self,direction):
        if direction == 'L':
            self.position[0] -=1

        elif direction == 'R':
            self.position[0] +=1

        elif direction == 'L':
            self.position[1] -=1

        else :
            self.position[1] +=1 

        return self.position

print("using class:")
C=Chess()
x=C.Move('L')
print(x)