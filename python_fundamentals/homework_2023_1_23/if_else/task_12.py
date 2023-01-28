age = int(input("Enter age(must be greater than 18): "))
sex = input('F/M: ').lower()
marital_status = input('Y/N: ').lower()

working_place = ''
if sex == 'f':
    working_place = 'city regions'
elif sex == 'm':
    if 20 <= age <= 40:
        working_place = 'anywhere'
    elif 40 < age <= 60:
        working_place = 'city regions'
else:
    print("Error: The person doesn't meet the requirements.")
