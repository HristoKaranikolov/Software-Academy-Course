# Create a program, that prints the letter "M":
#
# *   *
# *   *
# ** **
# * * *
# *   *
# *   *
# *   *


result = []
for i in range(1, 8):
    if i == 3:
        result.append('** **')
    elif i == 4:
        result.append('* * *')
    else:
        result.append('*   *')

print('\n'.join(result))
