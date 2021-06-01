import cProfile

def fun():
    print("Hi")


cProfile.run("fun()")