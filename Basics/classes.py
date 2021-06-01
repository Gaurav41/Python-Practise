class MyClass:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def show(self):
        print(f"x: {self.x} y: {self.y}")

my_class = MyClass(5,10)
my_class.show()

print(my_class.x)