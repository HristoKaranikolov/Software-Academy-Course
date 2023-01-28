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

sorting = numbers_lst.sort()
median = numbers_lst[1]
print(f" The median is {median}")
