import re

total = 0

with open('./input.txt') as f:
    for line in f:
        numbers = re.sub(r'\D', '', line)

        if len(numbers) == 0:
            continue
        elif len(numbers) == 1:
            total = total + int(f'{numbers}{numbers}')
        else:
            total = total + int(f'{numbers[0]}{numbers[-1]}')

print(total)
