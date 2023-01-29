# Create a program, that asks the client for number, then prints its fibonacci number.
# Do it with recursion.


def fib_func(num):
    if num == 0:
        return f'The {num}th fib term is 0'
    elif num == 1 or num == 2:
        return f'The {num}th fib term is 1'

    summing = fib_func(num - 1) + fib_func(num - 2)

    result = f'The {num}th fib term is {summing}'

    return result


print(fib_func(2))
