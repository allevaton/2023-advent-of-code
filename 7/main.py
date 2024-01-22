import re

total = 0

line_re = re.compile(r'Card\s+\d+:\s+([\d\s]*)\s+\|\s+([\d\s]*)')

with open('./input.txt') as f:
    for line in f:
        line_match = line_re.match(line.rstrip())

        winning_numbers = [int(x) for x in re.split(r'\s+', line_match[1])]
        my_numbers = [int(x) for x in re.split(r'\s+', line_match[2])]

        points = 0

        for winning_number in winning_numbers:
            if winning_number in my_numbers:
                if points > 0:
                    points = points * 2
                else:
                    points = 1

        total = total + points

print(f'Total: {total}')
