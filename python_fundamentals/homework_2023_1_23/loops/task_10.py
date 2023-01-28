# Create a program that calculates the sum from 1 to 50 in that order: 1*2 + 2*3*4 +..+n*(n+1)*(n+2)*..*2*n.


num = int(input())

total_sum = 0
counter = 1
for i in range(1, num + 1):
    start = i + 1  # we want to start multiplying everytime with the number after i.

    end = i + 1 + counter  # we want to add a number to multiply i, starting with a number i + 1
    # and everytime to add additional number for multiplying to reach the needed numbers for multiplication.

    adding = i
    for j in range(start, end):
        adding *= j

    total_sum += adding
    counter += 1

print(total_sum)
