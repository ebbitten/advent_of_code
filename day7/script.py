from typing import List, Set
RULES_DICK = {}
from functools import wraps
import sys
# sys.setrecursionlimit(10000)

def load_data() -> List[str]:
    with open('data') as f:
        return [line.strip('.\n').replace('bags', '').replace('bag', '') for line in f.readlines()]


def parse_line(line):
    outer_bag_string, inner_bag_string = line.split('contain')
    # print(outer_bag_string, '\n', inner_bag_string)
    outer_bag = outer_bag_string.strip(' ')
    inner_bags = [bag.strip(' ') for bag in inner_bag_string.split(' , ')]
    # print(outer_bag, '\n', inner_bags)
    RULES_DICK[outer_bag] = inner_bags


def traverse_dick(current_bag: str, bags_to_check: Set[str], bags_already_checked: Set[str]) -> int:

    # print(current_bag)
    # print(bags_to_check)
    # print(bags_already_checked)
    values = RULES_DICK.get(current_bag)
    if values:
        for value in values:
            new_key = value[2:]
            if new_key == 'shiny gold':
                return 1
            if new_key not in bags_already_checked:
                bags_to_check.add(new_key)
    if bags_to_check:
        bags_already_checked.add(current_bag)
        return traverse_dick(bags_to_check.pop(), bags_to_check, bags_already_checked)
    else:
        return 0

def part_one():
    data = load_data()
    for line in data:
        parse_line(line)
    checking_bags = [traverse_dick(key, set(), set()) for key in RULES_DICK.keys()]
    print(checking_bags)
    return sum([traverse_dick(key, set(), set()) for key in RULES_DICK.keys()])

def memoize(func):
    cache = func.cache = {}
    def memoized_func(key):
        if key not in cache:
            cache[key] = func(key)
        return cache[key]
    return memoized_func


@memoize
def part_two_fluffer(current_bag: str) -> int:
    values = RULES_DICK.get(current_bag)
    accumulator = 1
    if values:
        print(current_bag, values)
        for value in values:
            if value == 'no other':
                continue
            num_bags = int(value[0])
            new_key = value[2:]
            # print(new_key)
            accumulator += num_bags * part_two_fluffer(new_key)
            # print(accumulator)
    print(accumulator)
    return accumulator




def part_two():
    data = load_data()
    for line in data:
        parse_line(line)
    gold_bag_insides = part_two_fluffer('shiny gold') - 1
    print(gold_bag_insides)


if __name__ == '__main__':
    # print(part_one())
    print(part_two())
