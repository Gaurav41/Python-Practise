class Bird:

    def __init__(self,x):
        self.name = x
        print(f"{self.name} is ready")

    def whoisThis(self):
        print("this is a bird")

class Penguin(Bird):

    def __init__(self,x):
        super().__init__(x)
        print("in Penguin class")

    def whoisThis(self):
        print("this is a Penguin")

    def run(self):
        print("Run faster")



b = Bird("sparrow")
b.whoisThis()

print('******************')
p = Penguin("penguin")
p.whoisThis()
p.run()