# Write a program that finds nums that are divided to 7 and 5 without remainder
# in the range 1500 - 2700.


nums = []
for num in range(1500, 2700 + 1):
    if num % 5 == 0 and num % 7 == 0:
        nums.append(num)

print(nums)