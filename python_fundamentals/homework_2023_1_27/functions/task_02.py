def printing(item):
    if not item:
        print('Not found')
    else:
        print(item)


def find_el_in_list(lst: list, element):
    if element in lst:
        for idx, el in enumerate(lst):
            if el == element:
                result = idx
                return f'Position {result}'

    return False


list_items = [x for x in input('Enter elements separated by ", ": ').split(', ')]

el_to_search = input('Enter element to search: ')

printing(find_el_in_list(list_items, el_to_search))
