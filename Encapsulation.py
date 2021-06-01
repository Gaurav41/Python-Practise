class MyClass:

    def __init__(self,x):
        self.__privateVariable = x

    def getPrivateV(self):
        return self.__privateVariable

    def setPrivateV(self,x):
        self.__privateVariable = x


obj = MyClass("Gaurav")
print(obj.getPrivateV())
obj.__privateVariable = "skdfkj"
print(obj.getPrivateV())
