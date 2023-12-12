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

        qualifies = False

        for round in game_split:
            draw = {
                'green': 0,
                'red': 0,
                'blue': 0,
            }

            color_split = round.split(', ')

            for color in color_split:
                split = color.split(' ')
                color_name = split[1]
                number = int(split[0])
                draw[color_name] = number

            # Begin game logic
            if draw['red'] > RED:
                qualifies = False
                break
            elif draw['green'] > GREEN:
                qualifies = False
                break
            elif draw['blue'] > BLUE:
                qualifies = False
                break
            else:
                qualifies = True

        if qualifies:
            total = total + game_number

print(f'Total: {total}')
