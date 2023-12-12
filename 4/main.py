import re

RED = 12
GREEN = 13
BLUE = 14

game_re = re.compile(r'Game (\d+): (.*)')

total = 0

with open('./input.txt') as f:
    for line in f:
        game_match = game_re.match(line)
        game_number = int(game_match[1])
        game_content = game_match[2]

        game_split = game_content.split('; ')

        game = {
            'blue': [],
            'green': [],
            'red': [],
        }

        for round in game_split:
            color_split = round.split(', ')

            for color in color_split:
                split = color.split(' ')
                color_name = split[1]
                number = int(split[0])
                game[color_name].append(number)

        min_red = max(game['red'])
        min_green = max(game['green'])
        min_blue = max(game['blue'])

        power = min_red * min_green * min_blue

        print(game, power)

        total = total + power

print(f'Total: {total}')
