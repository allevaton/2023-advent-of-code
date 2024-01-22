import re
from collections import defaultdict

total = 0

line_re = re.compile(r'Card\s+(\d+):\s+([\d\s]*)\s+\|\s+([\d\s]*)')

with open('./input.txt') as f:
    original_cards_count = defaultdict(int)
    copy_cards_count = defaultdict(int)

    cards = []

    for line in f:
        line_match = line_re.match(line.rstrip())

        card_number = line_match[1]
        winning_numbers = [int(x) for x in re.split(r'\s+', line_match[2])]
        my_numbers = [int(x) for x in re.split(r'\s+', line_match[3])]

        cards.append({
            'card_number': card_number,
            'winning_numbers': winning_numbers,
            'my_numbers': my_numbers
        })

    for card_index, card in enumerate(cards):
        matching_numbers_count = 0

        for winning_number in card['winning_numbers']:
            if winning_number in card['my_numbers']:
                matching_numbers_count += 1

        original_cards_count[card_index + 1] += 1

        if matching_numbers_count == 0:
            continue

        stop = min(len(cards), card_index + matching_numbers_count + 1)

        for i in range(card_index + 1, stop):
            copy_cards_count[i + 1] += copy_cards_count[card_index + 1] + 1

for value in copy_cards_count.values():
    total += value

for value in original_cards_count.values():
    total += value

print(f'Total: {total}')
