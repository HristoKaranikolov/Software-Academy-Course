# Create a program, that asks the client for number,
# then calculate the factorial of this number and print it.
# Do it with recursion.

def calc_factorial(num):
    if num == 1:
        return num
    else:
        return num * calc_factorial(num - 1)


number = int(input())

print(calc_factorial(number))
