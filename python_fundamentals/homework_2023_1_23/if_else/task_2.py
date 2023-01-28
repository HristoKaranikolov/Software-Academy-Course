# Write a program, that shows the sign('+' or '-')
# from the quotient of two real numbers, but without calculating the result.

num1 = int(input())
num2 = int(input())

if (num1 // num2) > 0:
    print('+')
else:
    print('-')