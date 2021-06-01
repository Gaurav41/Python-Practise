def value():
    global a
    a = 10
    print("outer a:",a)
    def inner_value():
        global a
        a = 20
        print("inner a:", a)
    inner_value()
a = 30
print("global a:", a)
value()
print("global a:", a)

