# Question 8:
# Define a class with a generator which can iterate the numbers,
# which are divisible by 7, between a given range 0 and n.

s,e = [int(x) for x in input().split(" ")]

def generator(s,e):
     for i in range(s,e):
         if(i % 7 == 0):
             yield i
         else:
             pass

for i in generator(s,e):
    print(i)

# a = generator(s,e)
# print(next(a))
# print(next(a))
# print(next(a))