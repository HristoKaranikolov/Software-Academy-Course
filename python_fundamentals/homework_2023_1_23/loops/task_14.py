import random


def check_if_is_digit(num):
    if num.isdigit():
        return True
    return False


print('Welcome to the number guessing game!')

# Player choosing random number boundaries part
lower_boundary = (input('Choose a bottom boundary number: '))
upper_boundary = (input('Choose a top of range number: '))
if check_if_is_digit(lower_boundary) \
        and check_if_is_digit(upper_boundary):
    lower_boundary = int(lower_boundary)
    upper_boundary = int(upper_boundary)

random_num = random.randint(lower_boundary, upper_boundary)

# Player guessing part
number_guessed = False
guesses_count = 0
while not number_guessed:
    player_guess = input('Make a guess: ')

    if check_if_is_digit(player_guess):
        player_guess = int(player_guess)
    else:
        print('Please type a number!')
        continue
    guesses_count += 1

    if player_guess == random_num:
        number_guessed = True
    else:
        if player_guess < random_num:
            print('Too high!')
            continue
        else:
            print('Too low')
            continue

if number_guessed:
    print(f'Congratulations, you got it!\n'
          f'It took you {guesses_count} turns to guess the number.')
