#Data Types




# list,set,tuple and dictionary

# String 

name = "Testing" 
text = 'automation'
#String Slicing: It should be in the form of [start:stop:step]

string = name[::-1]# reverse the string
print(string)

print(name[0:2])

print(name[0:4])

print(name.upper())
print(name.lower())

Name = "   Automate the test case by the expected scenario.   "
print(Name.strip()) # remove the extra spaces from the string
text = "Hello Arnav"
print(text)
result = text.replace("Arnav","Shekar")
print(result)
#Split : it converts string to list ["Arnav","Shekar"] 
word = Name.split()
print(word)

result = " ".join(word)
print(result)
position = Name.find("expected")
print(position)
print(Name.count("a"))
print(Name.count("e"))
print(Name.startswith("Auto"))
print(Name.endswith("test"))

url = "https://google.com"
print(url.startswith("https"))
print(url.endswith(".com"))