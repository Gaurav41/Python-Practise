from abc import ABC,abstractmethod


class Polygon(ABC):
    #@abstractmethod
    def sides(self):
        pass


class Triangle(Polygon):

    # def sides(self):
    #     print("Hi")

    def sides2(self):
        print("Hi2222222222")

t = Triangle()
t.sides()
t.sides2()
