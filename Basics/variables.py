class MyClass:

    class_var = "Class Variable" #class variable/ Static variable

    def __init__(self,x):
        self.n = 0; #Instance variables
        self.x = x;


    def print_values(self):
        print(f"n :{self.n}")
        print(f"x :{self.x}")



obj = MyClass(10)
obj.n = 1
obj.print_values()

obj1 = MyClass(20)
obj1.print_values()

print("printing class variable value")
print(obj.class_var)
print(obj1.class_var)


obj.class_var = "obj class var"

print("printing value of changed class variable associated with obj......")

print(obj.class_var)
print(obj1.class_var)


MyClass.class_var = "Myclass class var"
print("printing value of changed class variable associated with MyClass ......")

print(obj.class_var)
print(obj1.class_var)



