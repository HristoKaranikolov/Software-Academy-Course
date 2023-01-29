# Create a program that reads words, while the client writes empty line.
# After that the program prints all words  on new line, excluding the ones that are repeating.

word = input()

text = []
while not word == '':
    text.append(word)

    word = input()

new_text = []
for x in text:
    if x not in new_text:
        new_text.append(x)

print('\n'.join([x for x in new_text]))