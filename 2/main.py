from typing import Optional

total = 0
history = []


def test_buffer_word(token_buffer: str) -> Optional[int]:
    if 'one' in token_buffer:
        return 1
    elif 'two' in token_buffer:
        return 2
    elif 'three' in token_buffer:
        return 3
    elif 'four' in token_buffer:
        return 4
    elif 'five' in token_buffer:
        return 5
    elif 'six' in token_buffer:
        return 6
    elif 'seven' in token_buffer:
        return 7
    elif 'eight' in token_buffer:
        return 8
    elif 'nine' in token_buffer:
        return 9


def test_buffer_number(token_buffer: str) -> Optional[int]:
    if '1' in token_buffer:
        return 1
    elif '2' in token_buffer:
        return 2
    elif '3' in token_buffer:
        return 3
    elif '4' in token_buffer:
        return 4
    elif '5' in token_buffer:
        return 5
    elif '6' in token_buffer:
        return 6
    elif '7' in token_buffer:
        return 7
    elif '8' in token_buffer:
        return 8
    elif '9' in token_buffer:
        return 9


def append_and_total_numbers_array(numbers: list[int]):
    global total

    if len(numbers) == 0:
        history.append(0)
    elif len(numbers) == 1:
        t = int(f'{numbers[0]}{numbers[0]}')
        total = total + t
        history.append(t)
    else:
        t = int(f'{numbers[0]}{numbers[-1]}')
        total = total + t
        history.append(t)


with open('./input.txt') as f:
    for i, line in enumerate(f):
        numbers = []
        token_buffer = ''

        # Find left number first
        for char in line:
            if char == '\n':
                append_and_total_numbers_array(numbers)
                break

            token_buffer = token_buffer + char

            test = test_buffer_word(token_buffer)
            if test is not None:
                numbers.append(test)
                token_buffer = token_buffer[-1]
                continue

            test = test_buffer_number(token_buffer)
            if test is not None:
                numbers.append(test)
                token_buffer = ''
                continue

for i, h in enumerate(history):
    print(f'{i + 1}: {h}')

print('Total:', total)
