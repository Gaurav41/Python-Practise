from dataclasses import dataclass

@dataclass
class DataClassCard:
    rank: str
    suit: str


dataClassObj = DataClassCard("A","ACE")
print(dataClassObj)
print(dataClassObj.suit)
print(dataClassObj.__dir__())

anotherObj = DataClassCard("A","ACE")
print(dataClassObj == anotherObj)

anotherObj = DataClassCard("Q","Queen")
print(dataClassObj == anotherObj)


# @dataclass
# class Position:
#     name: str
#     lon: float = 0.0
#     lat: float = 0.0
#
# print(Position("india"))
# print(Position("india",100,5000))


# @dataclass(frozen=True)
# class Position:
#     name: str
#     lon: float = 0.0
#     lat: float = 0.0
#
# obj = Position("india",100,5000)
# print(obj)
# #obj.name = "sdf" #dataclasses.FrozenInstanceError: cannot assign to field 'name'


# @dataclass
# class Position:
#     name: str
#     lon: float
#     lat: float
#
# @dataclass
# class Capital(Position):
#     country: str
#
# obj = Capital("Delhi",100,5000,"India")
# print(obj)