# Create a program, that prints the letter 'D':
# ****
# *   *
# *   *
# *   *
# *   *
# *   *
# ****


result = []
for i in range(1, 8):
    if i == 1 or i == 7:
        result.append('****')
    else:
        result.append('*   *')

print('\n'.join(result))
