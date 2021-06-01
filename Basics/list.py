numbers = [5,10,20,3,0,40]

print(numbers[0]) #5
print(numbers[:]) #[5, 10, 20, 3, 0, 40]
print(numbers[3:])#[3, 0, 40]
print(numbers[0:3])#[5, 10, 20]
print(numbers[1:-2])#[10, 20, 3]
print(numbers[0:10])#[5, 10, 20, 3, 0, 40]
print(numbers[1::2])#[10, 3, 40]
print(numbers[1:0:2])#[]

#List Method
for n in numbers:
    print(n)


(numbers.append(100))
print(numbers)

print(numbers.insert(0,100))
print(numbers)

print(numbers.index(100))
#print(numbers.index(99)) # error

print(99 in numbers) #false

print(numbers.count(100))#2

print(numbers.pop())#100

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

print(numbers.remove(100))
print(numbers)