# Create a program that reads numbers, while the client writes empty line.
# After that print all numbers in order: negative, zero, positive.
# All the  numbers must be in the order they were entered.
# Example:
# input: 3, -4, 1, 0, -1, 0, -2,
# output: -4, -1, -2, 0, 0, 3, 1

numbers_lst = []
num = input()
while not num == '':
    try:
        num = int(num)
    except ValueError:
        print('Please enter a digit: ')

    numbers_lst.append(num)
    num = input()

negative_nums = []
zeros = []
positive_nums = []

for x in numbers_lst:
    if x == 0:
        zeros.append(x)
    elif x < 0:
        negative_nums.append(x)
    else:
        positive_nums.append(x)

result = negative_nums + zeros + positive_nums
print('\n'.join(str(x) for x in result))
