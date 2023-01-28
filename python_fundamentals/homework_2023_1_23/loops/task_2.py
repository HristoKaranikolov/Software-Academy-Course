# Create a program, that takes 5 numbers from the console and calculates theirs sum.


nums = []
for _ in range(5):
    num = int(input())
    nums.append(num)

print(sum(nums))