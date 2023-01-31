# Write a program, that finds the longest count of same elements in a list.
# Example: : [2, 1, 1, 2, 3, 3, 2, 2, 2, 1] -> [2, 2, 2]


lst = [x for x in input().split(', ')]

longest_count_of_same_elems = []
same_elements_lst = []
for idx, item in enumerate(lst):
    if len(same_elements_lst) > len(longest_count_of_same_elems):
        longest_count_of_same_elems = same_elements_lst

    if idx < len(lst) - 1:
        next_item = lst[idx + 1]

        if same_elements_lst:
            if item == same_elements_lst[0]:
                same_elements_lst.append(item)
                continue
            else:
                same_elements_lst = []
                if item == next_item:
                    same_elements_lst.append(item)
        else:
            if item == next_item:
                same_elements_lst.append(item)

    else:
        break

print(longest_count_of_same_elems)
