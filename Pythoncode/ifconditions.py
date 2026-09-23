# If condition used to make decisions
age = 20
if age >= 25:
    print("He can eligible to get the job")
#if-else : Two possible outcomes  
if age <= 18:
    print("The person is eligible for voting")
else:
    print("He is not eleigible for voting") 
    
#if-elif-else  : You have multiple conditions     

Employee_sal = 35000

if  Employee_sal >= 32000:
    print("He can able to maintain the emis")
elif Employee_sal <= 20000:
    print("He cannot have a chance to maintain the emi's")
else:
    print("The employee not related to this category")    
        
if age >= 25 and Employee_sal >=35000:
    print("The person is Eleigible to pay the car emi")
else:
    print("Not eleigible to pay the car emi")  
    
if age >= 25 or Employee_sal >=35000:
    print("The person is Eligible to pay the car emi")
else:
    print("Not eleigible to pay the car emi")            
    
is_logged_in = False

if not is_logged_in: 
    print("Please login to the application")
    
username = "Automation"

if username == "TestAutomation":
    print("Valid username")
else:
    print("Invalid username")    
#Even Numbers:
number = 25
if number % 2 ==0:
    print("The number is Even")
else:
    print("It is an odd number")   
    
#positive or Negative number
num = -15
if num >0:
    print("Positive Number")
else:
    print("Negative Number")          
#Largest of three numbers
    