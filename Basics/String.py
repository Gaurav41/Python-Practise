
str = "Hello World"
print(str)

fName = 'Gaurav'
lName = "Pingale"
print(f'First Name is {fName}, Last Name is {lName} ' )

print(str.upper())
print(str.lower())
print(len(str))
print(fName == lName)

#find() is case sensitive
print(fName.find("G")) #-0
print(fName.find("g")) #-1
print(str.find("World"))

#replace
print(str.replace("Hello","hi")) #hi World
print(str.replace("sdfmldmf","hi")) # Hello World No error

#in
print('world' in str) # false ,case sensitive

str1 = "this is title"
print(str1.title()) #This Is Title




