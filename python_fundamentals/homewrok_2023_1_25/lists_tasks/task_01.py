# Create a program, that reads integers and saves them in a list.
# The program should read an integer while the client enters 0.
# After that it should print all numbers from the list ordered on ascending order
# and every value on new line.
# Use .sort() or sorted()

numbers_lst = []
num = int(input())
while not num == 0:
    numbers_lst.append(num)

    num = int(input())

numbers_lst.sort()
print('\n'.join([str(x) for x in numbers_lst]))
