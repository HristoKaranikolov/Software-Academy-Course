# Create a program, that prints all nums from 0 to 6, excluding 3 and 6.

nums = []
for i in range(7):
    if not i % 3 == 0 or i == 0:
        nums.append(i)

print(nums)
