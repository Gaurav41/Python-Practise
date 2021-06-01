class Employee:
    work_place = "Cuelogic Pvt"
    def __init__(self,name,id):
        #Instance variables
        self.name = name
        self.id = id;

    # Instance method
    def print_info(self):
        print("Printing Info: ")
        print(f"Emp Name :{self.name}")
        print(f"Emp Id :{self.id}")

    # Accessor method
    def get_name(self):
        return self.name

    # Mutator method
    def set_name(self,name):
        self.name= name

    # Class Method
    @classmethod
    def get_work_place(cls):
        return cls.work_place

    # Static Method
    @staticmethod
    def info():
        return ("This is Cuelogic's emp class")

e1 = Employee("xyz",101)
print("## Accessing instance var...")
print(e1.name)
print(e1.id)
print("_______________________")
print("## Accessing instance methods...")
e1.print_info()
e1.set_name("Gaurav")
print(e1.name)
print("_______________________")

e2 = Employee("abc",102)
print(e1.get_work_place())
print(e2.get_work_place())
print("_______________________")

print("## Calling instance methods...")

print(Employee.get_work_place())
# if we dont use @classmethod decorator
# we get error : get_work_place() missing 1 required positional argument: 'cls'
print("_______________________")

print("Calling static method")
print(Employee.info())
print("_______________________")
