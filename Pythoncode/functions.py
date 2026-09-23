"""
#Functions: It is reusable block of code that performs a particular task. 
# Whenever requires we are reusing that method.
Why we have to use the function?
Welcome to the Playwright session 10 times
print("Welcome to the Playwright session")
print("Welcome to the Playwright session")
print("Welcome to the Playwright session")
def functionname():
 print statement
 variable declaration
"""

def name():
    print("the name of the person")
    
name()   

def add():
    return 10+30
result = add()
print(result)

#print: It is used to display the result
#return : it sends the result back so we can store and we can use it later

def mul(a,b):# parameter is nothing but passing the variables to the function
    return a*b

result = mul(5,7)
print(result)

def sub(c,d):
    print(c-d)
    
sub(15,8)  
"""
1. Code reusability
2. Redusces the duplicate code
3. Makes the code easier to understand
4. The debug is easier
5. It will help you to maintain the code for large applications

1.Function Definition: Creating the function.
2.Function Call:When executing the function.

Parameter and the Argument: 
Parameter : Variable inside the function definition
Argument: Actual value passed during the function call or execution

"""  
#Expecting multiple values in the function
def calculate(a,b):
    add = a + b
    sub = a - b
    mul = a * b
    div = a / b
    mod = a % b
    return add,sub,mul,div,mod
result = calculate(15,3)
print(result)#print the result

#Default Argument: While passing the parameters we are declaring the value for that parameter

def add(a=19,b=23):
    print(a+b)
    
add(10,19)    

#Keyword Argument: Instead of passing the arguments based on their position, we can specify the parameter names.
def employee(name,age,salary):
    print(name)
    print(age)
    print(salary)
    
employee(
    name = "Tej",
    salary = 58538,
    age = 25,
)    
#*args: sometimes there will be more arguments we are using * to overcome

def student(*stu_id): # Pass variable number of positional arguments
    print(stu_id)
    
student(12,13,14,19,90) 

#**kwargs 

def student_details(**details): #Number of keyword arguments
    print(details)
    
student_details(name = "Tej",age =16,stu_id=15,city = "Hyderabad")

def check_number(num):
    if num > 0:
        return "Positive"
    elif num<0:
        return "Negative"
    else:
        return "Zero"
    
print(check_number(10))
print(check_number(-6))
print(check_number(0))    

def print_numbers():
    for i in range(1,7):
        print(i)
        
print_numbers()        

# Function calling in another function

def add(a,b):
    return a+b

def show_result():
    result = add(10,34)
    print("The result of the add is:", result)
    
show_result()     

# Recursive Function: The function calling itself

def factorial(n):
    if n==1:
        return 1    
    return n*factorial(n-1) 

print(factorial(5))      
#Advantages of Function:
    