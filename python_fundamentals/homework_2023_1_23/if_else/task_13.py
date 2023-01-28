# Write a program, that reads a 4-digit number from the console
# and prints it backwards.

number = int(input())
num_as_str = str(number)
num_as_str_backwards = num_as_str[::-1]
num_backwards = int(num_as_str_backwards)
print(type(num_backwards))