from typing import List


def load_data() -> List[int]:
    with open('data') as f:
        data = [int(line.strip()) for line in f.readlines()]
    return data


def valid_number(prev_numbers: List[int], number_to_check: int) -> bool:
    found_matching = False
    for i in prev_numbers:
        for j in prev_numbers:
            if i == j:
                continue
            if i + j == number_to_check:
                found_matching = True
    return found_matching


def part_one() -> int:
    data = load_data()
    for index, val in enumerate(data):
        if index <= 25:
            continue
        lookback = data[index-25:index]
        print(data)
        print(lookback)
        if not valid_number(lookback, val):
            return val, lookback


def part_two(target_number):
    data = load_data()



if __name__ == '__main__':
    print(part_one())

