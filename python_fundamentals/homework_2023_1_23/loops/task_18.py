# Create a program, that reads text as input
# and finds the count of the symbols that are repetitive. Including whitespaces .

word = input()
no_duplicat_word = set(word)

count_duplicat = len(word) - len(no_duplicat_word)
print(count_duplicat)
