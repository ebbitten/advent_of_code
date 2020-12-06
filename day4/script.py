import re

def byr(exp):
    return True if 1920 <= int(exp) <= 2002 else False

def iyr(exp):
    return True if 2010 <= int(exp) <= 2020 else False

def eyr(exp):
    return True if 2020 <= int(exp) <= 2030 else False


def hgt(exp):
    pass

def hcl(exp):
    pass

def ecl(exp):
    pass

def pid(exp):
    pass

REQUIRED_FIELDS = {'byr:': byr, 'iyr:': iyr, 'eyr:':eyr, 'hgt:':hgt, 'hcl:':hcl, 'ecl:':ecl, 'pid:':pid}


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