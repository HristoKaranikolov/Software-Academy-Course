# Write a program that finds the longest count of consecutive elements in a list.
# Example: : [3, 2, 3, 4, 2, 2, 4] -> [2, 3, 4]

lst = []
is_valid = False
while not is_valid:
    try:
        lst = [int(x) for x in input().split(', ')]
        is_valid = True
    except ValueError:
        print('Please add list of elements with only digits in it, separated by coma!')


longest_consecutive_items = []
consecutive_items = []
for idx in range(len(lst)):
    curr_item = lst[idx]

    if idx == 0:
        consecutive_items.append(curr_item)
    if idx < len(lst):
        if curr_item - consecutive_items[-1] == 1:
            consecutive_items.append(curr_item)
        else:
            consecutive_items = [curr_item]

        if len(consecutive_items) > len(longest_consecutive_items):
            longest_consecutive_items = consecutive_items

print(longest_consecutive_items)
