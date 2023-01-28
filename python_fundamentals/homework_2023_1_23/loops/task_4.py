# Create a program, that prints a text backwards, which text is given from the console.(Use 'for' loop)

word = input()
word_backwards = ''
for i in range(len(word) - 1, -1, -1):
    word_backwards += word[i]

print(word_backwards)

print(word[::-1])  # Without the for loop :)
