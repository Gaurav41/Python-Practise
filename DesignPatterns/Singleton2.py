# method 2

class Singleton(object):


    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,"_instance"):
            cls._instance = super().__new__(cls,*args,**kwargs)
        return cls._instance



o1 = Singleton()
print("Object",o1)
o1.data = 10
print("Object data",o1.data)

o2 = Singleton("gaurav")
print("Object",o2)
print("Object data",o2.data)