class car:
  
    def __init__(self, model, color):  # It is a constructor which runs automatically when new object got created.
        self.model = model
        self.color = color

# Remove indentation for lines below so they are outside the class
Car1 = car("Audi", "Blue")
print(Car1.model)
print(Car1.color)

#Inheritance: The methods created in the Parent class that allows in the child class
"""
Static/Class variables
A class variable is shared by all objects of the class.

"""

class Employee:
    
    company = "AB Technologies" #Class variable
    
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        
emp1 = Employee("John", 50000)

print(emp1.company) 
print(emp1.name)       