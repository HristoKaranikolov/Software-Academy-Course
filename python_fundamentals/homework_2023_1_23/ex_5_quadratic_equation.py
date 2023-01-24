from math import sqrt, pow

while True:
    a = int(input('This digit must be greater than 0! - '))
    if a == 0:
        continue
    break

b = int(input())
c = int(input())

discriminant = pow(b, 2) - 4 * a * c
x1 = 0
x2 = 0
are_there_solutions = False
if discriminant > 0:
    are_there_solutions = True
    x1 = (-b + sqrt(discriminant)) / 2 * a
    x2 = (-b - sqrt(discriminant)) / 2 * a

elif discriminant == 0:
    are_there_solutions = True
    x1 = x2 = -b / 2 * a
else:
    print('There are no real number solution for this equation, the solution is a complex number!')

if are_there_solutions:
    print(x1)
    print(x2)
