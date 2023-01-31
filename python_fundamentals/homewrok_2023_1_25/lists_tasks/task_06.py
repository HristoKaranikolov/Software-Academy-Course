def display_sublist(lst):
    new_lists = [[]]

    for i in range(len(lst) + 1):
        for j in range(i + 1, len(lst) + 1):
            sub = lst[i:j]
            new_lists.append(sub)

    return new_lists


data = [x for x in input().split(', ')]
print(display_sublist(data))
