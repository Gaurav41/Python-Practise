# Question 6:

# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

# Suppose the following input is supplied to the program:

# Hello world!

# Then, the output should be:

# UPPER CASE 1

# LOWER CASE 9

# Hints:

# In case of input data being supplied to the question, it should be assumed to be a console input.
ip = input()
upper_count = lower_count = 0
for i in ip:
    if i.isupper():
        upper_count += 1
    elif i.islower():
        lower_count += 1

print(f"UPPER CASE {upper_count}")
print(f"LOWER CASE {lower_count}")
