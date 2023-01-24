numbers_in_bulgarian = {0: 'нула',
                        1: 'едно',
                        2: 'две',
                        3: 'три',
                        4: 'четири',
                        5: 'пет',
                        6: 'шест',
                        7: 'седем',
                        8: 'осем',
                        9: 'девет'
                        }

print('If you want to know how its called a digit, between 0 and 9 in bulgarian, please ask!')
number = int(input('Choose a digit: '))

print(f'The digit {number} is called "{numbers_in_bulgarian[number]}" in bulgarian.')
