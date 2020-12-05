import re

REQUIRED_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


def load_data():
    with open('data') as f:
        data = str(f.read())
        split = re.split(r'\n\n', data)
        return split


def helper(passport):
    for field in REQUIRED_FIELDS:
        if not re.search(f'{field}:', passport):
            # print(field, '\n', passport)
            return 0
    return 1


def outer():
    passports = load_data()
    return sum([helper(passport) for passport in passports])

print(outer())