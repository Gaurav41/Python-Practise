try:
    print(10/0)
except ZeroDivisionError:
    print("Divide by zero error")
except :
    print("unknown error")