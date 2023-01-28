# Create a program, that prints:
#  ***
# *   *
# *   *
# *****
# *   *
# *   *
# *   *


res = ''
for i in range(1, 8):
    if i == 1:
        res += ' *** '
        res += '\n'
    elif i == 4:
        res += '*****'
        res += '\n'
    else:
        res += '*   *'
        res += '\n'

print(res)
