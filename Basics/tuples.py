#immutable
tuple = (1,2,5)
print(tuple.count(1))
print(tuple.index(5))

#tuple[0]=10 #TypeError: 'tuple' object does not support item assignment
print(tuple[0])
x,y,z = tuple
print(x,y,z)