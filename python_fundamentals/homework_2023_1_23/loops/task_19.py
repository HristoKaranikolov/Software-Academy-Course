# Create a program, that takes string as input and turns backwards the symbols
# only if the length of the word is odd, otherwise leave the word untouched.

text = [x for x in input().split()]

valid_text = []
for x in text:
    print(x if len(x) % 2 == 0 else x[::-1], end=' ')



