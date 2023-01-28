points = int(input("Write points! - "))

bonus_points = 0
is_there_error = False
if 1 <= points <= 3:
    bonus_points = 10

elif 4 <= points <= 6:
    bonus_points = 100

elif 7 <= points <= 9:
    bonus_points = 1000

else:
    is_there_error = True

if not is_there_error:
    total_points = points * bonus_points
    print(total_points)
else:
    print('Error')