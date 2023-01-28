human_years = int(input())

dog_years = 0
for year in range(1, human_years):
    if year == 1 or year == 2:
        dog_years += 10.5
    else:
        dog_years += 4

print(f"Human years: {human_years} years old.", end='\n'
      f"Dog years: {dog_years} years old.")
