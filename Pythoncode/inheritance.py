#inheritance: To inherit the attributes and methods to one class to another class
class Animal: # Parent class
    def __init__(self,name):
        self.name = name
        
    def info(self):
        print("The Animal Name:", self.name)
        
        
class Cat(Animal):    #Child class
    def sound(self):
        print(self.name, "Meows")  
        
c = Cat("Meenu")
c.info()
c.sound()              