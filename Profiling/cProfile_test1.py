import cProfile
import pstats
import io

def fun():
    for i in range(0,1000000000):
        # print("Hi")
        pass

def profile(fun):
    """ A decorator @profile that uses cProfile to profile to function"""

    def inner(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        fun()
        pr.disable()
        pr.print_stats()

    return inner()

profile(fun)