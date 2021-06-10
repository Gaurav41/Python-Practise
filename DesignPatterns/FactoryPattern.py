from abc import ABC
from abc import abstractmethod
class Car(ABC):
    """ Interface class for all types of cars
    """

    @abstractmethod
    def get_properties(self):
        """ Returns properties of car"""
        pass

    @abstractmethod
    def get_price(self):
        """ Returns price of car"""
        pass


class BMW(Car):
    """ class BMW inherits abstract class car """
    def __init__(self):
        self.model = "BMW 3 Series"
        self.price = "Rs50,50,000"
        self.color = "Skyblue"
        self.milage = "20 km\Liter"

    def get_properties(self):
        return {
            "model": self.model,
            "color": self.color,
            "milage": self.milage
        }

    def get_price(self):
        return self.price


class Mercedes(Car):
    """ class Mercedes inherits abstract class car """

    def __init__(self):
        self.model = "Mercedes-Benz Maybach GLS"
        self.price = "Rs2,50,00000"
        self.color = "Skyblue"
        self.milage = "8.5 km\Liter"

    def get_properties(self):
        return {
            "model": self.model,
            "color": self.color,
            "milage": self.milage
        }

    def get_price(self):
        return self.price


class CarFactory():
    """ Facrory class provides get_car() factory method """
    @staticmethod
    def getCar(car):
        try:
            if car == "BMW":
                return BMW()
            if car == "Mercedes":
                return Mercedes()
            raise AssertionError("Car Not Found")
        except AssertionError as e:
            print(e)

if __name__ == "__main__":
    car = CarFactory.getCar("BMW")
    print(car.get_properties())
    print(car.get_price())

    car = CarFactory.getCar("Mercedes")
    print(car.get_properties())
    print(car.get_price())
