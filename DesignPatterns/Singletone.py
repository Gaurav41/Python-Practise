from abc import ABC,abstractmethod

class Person(ABC):

    @abstractmethod
    def print_data(self):
        """implement in child class"""

class PersonSingletone(Person):

    __instance = None

    def __init__(self,name,age):
        self.name = name
        self.age = age
        PersonSingletone.__instance = self

    def print_data(self):
        print("id",id(self))
        print("name", self.name)
        print("age", self.age)

    @staticmethod
    def get_instance(name, age):
        if PersonSingletone.__instance == None:
            PersonSingletone(name, age)
        else:
            print("One instance already created ...Only one instance can be created ")
        return PersonSingletone.__instance


p = PersonSingletone.get_instance("Gaurav",20)
print(p)
p.print_data()

p = PersonSingletone.get_instance("Pingale",40)
print(p)
p.print_data()