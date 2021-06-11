from abc import ABC,abstractmethod

class Person(ABC):

    @abstractmethod
    def print_data(self):
        """implement in child class"""

class PersonSingleton(Person):

    __instance = None

    def __init__(self,name,age):
        self.name = name
        self.age = age
        PersonSingleton.__instance = self

    def print_data(self):
        print("id",id(self))
        print("name", self.name)
        print("age", self.age)

    @staticmethod
    def get_instance(name, age):
        if PersonSingleton.__instance == None:
            PersonSingleton(name, age)
        else:
            print("One instance already created ...Only one instance can be created ")
        return PersonSingleton.__instance


p = PersonSingleton.get_instance("Gaurav",20)
print(p)
p.print_data()

p = PersonSingleton.get_instance("Pingale",40)
print(p)
p.print_data()


