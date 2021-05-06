# Question 5:

# Write a program that accepts a sentence and calculate the number of letters and digits.

# Suppose the following input is supplied to the program:

# hello world! 123

# Then, the output should be:

# LETTERS 10

# DIGITS 3


# Hints:

# In case of input data being supplied to the question, it should be assumed to be a console input.

ip = input()

digit_count = 0
letters_count = 0
for i in ip:
    if i.isdigit():
        digit_count += 1
    elif i.isalpha():
        letters_count += 1

print(f"LETTERS {letters_count}")
print(f"DIGITS {digit_count}")



