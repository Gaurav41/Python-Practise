import time


def fun1():
    i=0
    while (i < 99999999):
        i += 1

    else:
        print("Done")

def fun2():
    for i in range(99999999):
        #
        pass

    else:
        print("Done")

start = time.time()

fun1()

end = time.time()

print("Execution time for While loop:{}".format(end-start))

start = time.time()

fun2()

end = time.time()

print("Execution time for for Loop:{}".format(end-start))