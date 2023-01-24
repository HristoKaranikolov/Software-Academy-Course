# Write a program, that finds the largest num in between 3 numbers.

numbers_lst = []
print('Please write your 3 digits!')

for _ in range(1, 4):
    while True:
        try:
            numbers_lst.append(int(input(f'Enter a digit: ')))
            break
        except ValueError:
            print('Please enter a number!')
            continue

largest_num = max(numbers_lst)
print(f"The largest number in between the numbers: {numbers_lst} is {largest_num}")
