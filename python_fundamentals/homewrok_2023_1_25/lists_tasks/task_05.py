from random import randint

lottery_numbers = []

while len(lottery_numbers) < 6:
    number = randint(1, 49)
    if number not in lottery_numbers:
        lottery_numbers.append(number)

print(', '.join(str(x) for x in sorted(lottery_numbers)))

