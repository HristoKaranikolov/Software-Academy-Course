# Sort 3 real numbers in ascending order. Use nested for loops.
from collections import deque

nums = []
nums_ordered_asc = deque()
max_num = 0
for i in range(3):
    num = int(input())
    nums.append(num)
    if num > max_num:
        max_num = num
        nums_ordered_asc.appendleft(num)
    else:
        nums_ordered_asc.append(num)

print(', '.join([str(x) for x in list(nums_ordered_asc)]))

# And can be done as easy as that
print(sorted(nums, reverse=True))
