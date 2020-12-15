from typing import List
from functools import lru_cache

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

@lru_cache(maxsize=None, typed=False)
def helper_two(num, xlist):
    if num not in xlist:
        return 0
    if num == 0:
        return 1
    else:
        partial_1 = helper_two(num-1, xlist)
        partial_2 = helper_two(num-2, xlist)
        partial_3 = helper_two(num-3, xlist)
        return sum([partial_1, partial_2, partial_3])

def part_two():
    data = load_data()
    data.append(max(data)+3)
    @lru_cache(maxsize=None, typed=False)
    def helper_two(num):
        print(num)
        if num == 0:
            return 1
        if num not in data:
            return 0
        else:
            return sum([helper_two(num-offset) for offset in range(1, 4)])
    return helper_two(max(data))




if __name__ == '__main__':
    # print(part_one())
    print(part_two())