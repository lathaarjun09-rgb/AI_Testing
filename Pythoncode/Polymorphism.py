# Polymorphism:One interface and multiple methods or behavior

class Tester:
    def work(self):
        print("Tester was testing the application")        
        
class Developer:
    def work(self):
        print("Developer was developing the application")
        
class Manager:
    def work(self):
        print("Manager manages the application")   
        
tester = Tester()
developer = Developer()
manager = Manager()

tester.work()
developer.work()
manager.work()         

"""
Method Overloading: Same method name with different parameters. It is not supported 
in python. But we can achieve it by using default arguments.

Method Overriding: Same method name with same parameters in the child class.
It is supported in python.

"""
class Employee:
    def work(self):
        print("Employee is working")

class Tester(Employee):
    def work(self):
        print("Tester was testing the application")        
        
class Developer(Employee):
    def work(self):
        print("Developer was developing the application")  
        
employee = Employee()  
tester = Tester()
developer = Developer()

employee.work()
tester.work()
developer.work()