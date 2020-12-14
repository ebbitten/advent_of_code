from typing import List


def load_data() -> List[int]:
    with open('data') as f:
        return [int(line.strip()) for line in f.readlines()]


def part_one() -> int:
    sorted_list = sorted(load_data())
    one_volt_diffs = 0
    #last one is three volts
    three_volt_diffs = 1
    for index, val in enumerate(sorted_list):
        if index == 0:
            prev_val = 0
        else:
            prev_val = sorted_list[index-1]
        if val - prev_val == 1:
            one_volt_diffs += 1
        elif val - prev_val == 3:
            three_volt_diffs += 1
    return one_volt_diffs * three_volt_diffs

if __name__ == '__main__':
    print(part_one())