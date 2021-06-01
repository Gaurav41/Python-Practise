def greet():
    print("hi")

print("call function greet")
greet()

def greet(f_name,l_name):
    print(f"hi {f_name} {l_name}")

print("call function greet")
greet("Gaurav","Pingale")

#keyWord argument
print("call function greet")
greet(l_name="Pingale",f_name="Gaurav",)
