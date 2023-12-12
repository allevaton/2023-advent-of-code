import re

total = 0

symbol_re = re.compile(r'\W')
number_re = re.compile(r'\d')

TOKEN_DOT = 'DOT'
TOKEN_SYMBOL = 'SYMBOL'

schematic: list[list] = []

with open('./input.txt') as f:
    for i, line in enumerate(f):
        schematic.append([])

        for char in line:
            if char == '.' or char == '\n':
                schematic[i].append(TOKEN_DOT)
            elif symbol_re.match(char):
                schematic[i].append(TOKEN_SYMBOL)
            elif number_re.match(char):
                schematic[i].append(int(char))

    for line, sequence in enumerate(schematic):
        number_buffer = ''
        found_symbol = False

        for i, char in enumerate(sequence):
            if char == TOKEN_DOT or char == TOKEN_SYMBOL:
                if found_symbol and len(number_buffer) > 0:
                    total = total + int(number_buffer)
                    found_symbol = False
                number_buffer = ''
            else:
                number_buffer = number_buffer + str(char)

                # Found a number
                if not found_symbol:
                    available_left = i > 0
                    available_right = i < len(sequence) - 2
                    available_up = line > 0
                    available_down = line < len(schematic) - 2

                    if available_up:
                        if schematic[line - 1][i] == TOKEN_SYMBOL:
                            found_symbol = True

                        if available_left and schematic[line - 1][i - 1] == TOKEN_SYMBOL:
                            found_symbol = True

                        if available_right and schematic[line - 1][i + 1] == TOKEN_SYMBOL:
                            found_symbol = True

                    if available_down:
                        if schematic[line + 1][i] == TOKEN_SYMBOL:
                            found_symbol = True

                        if available_left and schematic[line + 1][i - 1] == TOKEN_SYMBOL:
                            found_symbol = True

                        if available_right and schematic[line + 1][i + 1] == TOKEN_SYMBOL:
                            found_symbol = True

                    if available_left and sequence[i - 1] == TOKEN_SYMBOL:
                        found_symbol = True

                    if available_right and sequence[i + 1] == TOKEN_SYMBOL:
                        found_symbol = True

print(f'Total: {total}')
