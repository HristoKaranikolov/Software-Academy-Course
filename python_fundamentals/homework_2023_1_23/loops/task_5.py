# Create a program, that finds and prints the count of all even and odd nums.

nums = [x for x in input().split(', ')]

even_nums_count = len([x for x in nums if x % 2 == 0])
odd_nums_count = len([x for x in nums if x % 2 != 0])

print(even_nums_count)
print(odd_nums_count)