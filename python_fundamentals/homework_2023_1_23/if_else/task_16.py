hotel_rooms_and_prices = {'studio': {'may': 50, 'october': 50,
                                     'june': 75.20, 'september': 75.20,
                                     'july': 76, 'august': 76},
                          'apartment': {'may': 65, 'october': 65,
                                        'june': 68.70, 'september': 68.70,
                                        'july': 77, 'august': 77}}

month = input().lower()
nights_count = int(input())

studio_discount_percent = 0
apartment_discount_percent = 0
if 7 <= nights_count <= 14:
    if month == 'may' or month == 'october':
        studio_discount = 0.05
else:
    apartment_discount = 0.10

    if month == 'may' or month == 'october':
        studio_discount = 0.30
    elif month == 'may' or month == 'october':
        studio_discount = 0.20

studio_price = hotel_rooms_and_prices['studio'][month]
total_studio_price = (studio_price * nights_count)
total_studio_price -= total_studio_price * studio_discount_percent

apartment_price = hotel_rooms_and_prices['apartment'][month]
total_apartment_price = (apartment_price * nights_count)
total_apartment_price -= total_apartment_price * apartment_discount_percent

print(total_studio_price)
print(total_apartment_price)
