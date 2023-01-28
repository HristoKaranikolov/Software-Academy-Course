def check_even_or_odd(num):
    if num % 2 == 0:
        return 'even'
    return 'odd'


def calc_func(num1, num2, operator):
    result = ""
    if operator == '/' and num2 == 0:
        result = f"Cannot divide {num1} by zero."

    elif operator == '+' or operator == '-' or operator == '*':
        if operator == '+':
            math_result = num1 + num2
        elif operator == '-':
            math_result = num1 - num2
        else:
            math_result = num1 * num2

        result = f"{num1} {operator} {num2} = {math_result} - {check_even_or_odd(math_result)}"

    elif operator == '/':
        math_result = num1 / num2
        result = f"{num1} / {num2} = {math_result:.2f}"

    elif operator == '%':
        math_result = num1 % num2
        result = f"{num1} % {num2} = {math_result}"

    return result


print(calc_func(4, 2, '%'))
