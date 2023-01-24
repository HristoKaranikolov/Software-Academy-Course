# Write if statement which checks values of two integers
# and exchanges them only if the first value is greater than the second.

num_1 = int(input())
num_2 = int(input())

if num_1 > num_2:
    num_2, num_1 = num_1, num_2


print(f"first number: {num_1}", end='\n'
      f"second number: {num_2}")
