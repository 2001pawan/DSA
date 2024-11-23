# Question 1) Write a Python program to create a Vehicle class with max_speed and mileage instance attributes and the Vehicle make (e.g. Tesla or GM) as a class attribute.
#  Also, write code to call the Class and print out the the max_speed, mileage, and make.

class vehicle:
    make = "tesla"
    def __init__(self,s,m):
        self.max_speed=s
        self.mileage=m

car=vehicle(10,20)

print(vehicle.make,
car.max_speed,
car.mileage)




    

        
        