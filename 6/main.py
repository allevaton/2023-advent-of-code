import re
from collections import defaultdict

total = 0

symbol_re = re.compile(r'\W')
number_re = re.compile(r'\d')

TOKEN_DOT = 'DOT'
TOKEN_SYMBOL = 'SYMBOL'

schematic: list[list] = []
gear_map = defaultdict(list)

with open('./input.txt') as f:
    for line in f:
        schematic.append([char for char in line])

    for line, sequence in enumerate(schematic):
        number_buffer = ''

        # Boolean or "x,y" coordinate of gear
        found_gear = False

        for i, char in enumerate(sequence):
            if char == '.' or symbol_re.match(char):
                if found_gear and len(number_buffer) > 0:
                    gear_map[found_gear].append(int(number_buffer))
                    found_gear = False
                number_buffer = ''
            else:
                number_buffer = number_buffer + str(char)

                # Found a number
                available_left = i > 0
                available_right = i < len(sequence) - 2
                available_up = line > 0
                available_down = line < len(schematic) - 2

                matching_symbols: list[str] = []

                if available_up:
                    if schematic[line - 1][i] == '*':
                        found_gear = f'{line - 1},{i}'

                    if available_left and schematic[line - 1][i - 1] == '*':
                        found_gear = f'{line - 1},{i - 1}'

                    if available_right and schematic[line - 1][i + 1] == '*':
                        found_gear = f'{line - 1},{i + 1}'

                if available_down:
                    if schematic[line + 1][i] == '*':
                        found_gear = f'{line + 1},{i}'

                    if available_left and schematic[line + 1][i - 1] == '*':
                        found_gear = f'{line + 1},{i - 1}'

                    if available_right and schematic[line + 1][i + 1] == '*':
                        found_gear = f'{line + 1},{i + 1}'

                if available_left and sequence[i - 1] == '*':
                    found_gear = f'{line},{i - 1}'

                if available_right and sequence[i + 1] == '*':
                    found_gear = f'{line},{i + 1}'

for value in gear_map.values():
    if len(value) == 2:
        total = total + (value[0] * value[1])

print(f'Total: {total}')
