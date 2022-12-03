with open('input.txt') as f:
    calories = 0
    max_calories = 0
    for line in f:
        if line == '\n':
            if calories > max_calories:
                max_calories = calories
            calories = 0
            continue
        calories += int(line)

print(f'Max cals {max_calories}')
