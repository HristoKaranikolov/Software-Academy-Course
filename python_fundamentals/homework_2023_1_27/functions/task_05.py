def add(cart: dict, item=input()):
    if item not in cart:
        cart[item] = 1
    else:
        cart[item] += 1

    print(f'Item {item} added to cart.')


def remove(cart: dict, item=input()):
    if item in cart:
        print(f'Removed {item} from cart.')
        del cart[item]
    else:
        print(f'Item {item} not in cart!')


def clear(cart):
    print('cleared')
    cart.clear()


def show(cart):
    print('\n'.join({k: v for k, v in cart.items()}))


def Quit():
    exit()


item_data = input()
shopping_cart = {}

# add(shopping_cart, 'abv')
# show(shopping_cart)
# clear(shopping_cart)
# show(shopping_cart)
# #
# # add('pants', shopping_cart)
# # print(show(shopping_cart))
