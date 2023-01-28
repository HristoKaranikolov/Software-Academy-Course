budget = float(input('Please enter the budget! '))
category_ticket = input('VIP/Normal').lower()
people_count = int(input())

ticket_type_and_price = {'normal': 249.99,
                         'vip': 499.99}

travel_taxes = 0
if 1 <= people_count <= 4:
    travel_taxes = budget * 0.75
elif 5 <= people_count <= 9:
    travel_taxes = budget * 0.60
elif 10 <= people_count <= 24:
    travel_taxes = budget * 0.50
elif 25 <= people_count <= 49:
    travel_taxes = budget * 0.4
else:
    travel_taxes = budget * 0.25

budget -= travel_taxes

ticket_price = ticket_type_and_price[category_ticket]
group_ticket_price = people_count * ticket_price

diff = abs(budget - group_ticket_price)
if budget > group_ticket_price:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")