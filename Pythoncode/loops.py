#Loops:The task which we are performing repeatedly
# For and while loop

#for loop : It is used to iterate a particular task.
names = ["tej","test","Raj","Seema"]
for i in names:
    print(i)
    
name = "Python"
for i in name:
    print(i)    
    
Print numbers from 1 to 10

for i in range(10): # it starts with 0
    print(i+1) #0 + 1 = 1
    
for i in range(1,6):# it stops before 6
    print(i) 
  
    
for i in range(5):
    print("Hello !Welcome")    
    
#range(start,stop,step)  

for i in range(0,100,2): # 1, 1+2=3,3+2=5,5+2=7........
    print(i) 
    
for i in range(10,1,-1): # 1, 1+2=3,3+2=5,5+2=7........
    print(i) 
 #Even number 
        
for num in range(1,6):
    if num % 2 ==0:
        print("Even",num)
    else:
        print("Odd", num) 
        
number = 6
for i in range(1,11):
    result = number * i
    print(number, "x" , i ,"=",result)       

#break & continue
for i in range(1,11):#1,2,3,4,i ==5
    if i == 6:
        break
    print(i)     
    
for i in range(1,8):#1,2,3,4,i ==5
    if i == 3:
        continue
    print(i)  
    
for i in range(1,8):#1,2,3,4,i ==5
    if i == 3:
        pass
    print(i) 
    
While  : A loop executes a block of code when condition is true
while condition:
#     statement                    
# i = 1
# while i <= 5: 
#     print(i)
#     i = i + 1
# """
# i = 1
# 1<=5=true then it will print 1 i = 1+1;1+1 =2
# 2<=5 2
# 3<=5 3
# 4<=5 4
# 5<=5 5
# """
#infinite

# i = 1
# while i <= 5:
#     print(i)
    
# Break
# i = 1
# while i<=10:
#     if i == 2:
#         break
#     print(i)
#     i=i+1    
# # Continue
# i = 1
# while i <= 10:
#     if i == 2:
#         i=i+1
#         continue
#     print(i)
#     i=i+1     
    
# # Nested loops
# for i in range(1,5):
#     for j in range(1,5):
#         print(i,j)   
# Nested loop with pattern
# for i in range(1,6):
#     for j in range(i):
#         print("&", end = " ")
        
#     print()     

# Encoded data representing the structural outline of the India map
encoded_map = (
    "TFy! QJu ROo TNn(ROo)SLq SLq ULo+UHs UJq TNn*RPn/QP,"
    "bEWS_JSWQAIJO^NBELPeHBFHT}TnALVlBLOFAkHFOuFETpHCStHAUFAgcEAelc,"
    "lcn^r^r\\tZvYxXyT|S~Pn SPm SOn TNn ULo0ULo#ULo-WHq! WFs XDt!"
)

# Initialize variables to keep track of indices and character switching
char_index = 0
line_position = 10  # Used to track when to wrap to a new line
print(char_index)
# Outer loop: Iterates through each character block of the encoded data
for char_index in range(len(encoded_map)):
    ascii_val = ord(encoded_map[char_index])
    
    # Inner loop: Prints the respective number of spaces or stars 
    # determined by subtracting 64 from the ASCII value
    for repeat in range(ascii_val - 64):
        line_position += 1
        
        # When line_position reaches 90, wrap to the next row
        if line_position == 90:
            line_position = 10
            print()  # Moves to the next line
        else:
            # Alternates between a star (*) and a space based on character index parity
            if char_index % 2 == 0:
                print("&", end="*")
            else:
                print(" ", end=" ")
