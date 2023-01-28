from math import pow

# Create a program that prints all formulas that are : c^3 = a^2 + b^2.

result = []
for i in range(1, 51):
    for j in range(1, 51):
        for k in range(1, 51):
            first_num = pow(i, 2)
            second_num = pow(j, 2)
            third_num = pow(k, 3)

            nums_sum = first_num + second_num
            if nums_sum == third_num:
                res = f'{i}^2 + {j}^2 = {k}^3'
                result.append(res)

print('\n'.join([x for x in result]))
