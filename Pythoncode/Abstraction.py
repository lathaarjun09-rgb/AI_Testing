"""
Abstraction: It will shows only the necessary information.
It hides the internal implementation data.
"""

from abc import ABC,abstractmethod

class Employee(ABC):
    @abstractmethod
    def work(self):
        pass

class Tester(Employee):
    def work(self):
        print("Tester was testing the application")        
        
class Developer(Employee):
    def work(self):
        print("Developer was developing the application")  
        

tester = Tester()
developer = Developer()

tester.work()
developer.work()