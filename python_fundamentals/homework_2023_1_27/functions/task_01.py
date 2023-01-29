def find_el_in_list(lst: list, element):
    if element in lst:
        for idx, el in enumerate(lst):
            if el == element:
                result = idx
                return f'Position {result}'

    return 'Not found'


list_items = [x for x in input('Enter elements separated by ", ": ').split(', ')]

el_to_search = input('Enter element to search: ')
if el_to_search.isdigit():
    el_to_search = int(el_to_search)

print(find_el_in_list(list_items, el_to_search))
