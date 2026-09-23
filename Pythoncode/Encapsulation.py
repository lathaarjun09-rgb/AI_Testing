"""
Encapsulation: Binding the data and methods together inside a class and later controlling
 the access to the data.
"""

class Employee:
    def __init__(self, Emp_name, Emp_salary):
        self.name = Emp_name
        self.__salary = Emp_salary  # Private variable

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Salary must be positive.")
            
emp = Employee("John", 50000)  
print(emp.get_salary())
emp.set_salary(60000)          