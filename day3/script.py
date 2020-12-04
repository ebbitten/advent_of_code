from itertools import cycle

class SubscriptableCycle(cycle):
    def __getitem__(self, item):
        for i in range(item):
            self.__next__()
        return self.__next__()

def get_data():
    with open('data') as f:
        data = [SubscriptableCycle(line.strip()) for line in f.readlines()]
    return data


def helper(linenum, line):
    return_val = 1 if line[linenum*3] == "#" else 0
    print(return_val)
    return return_val


def main():
    data = get_data()
    return sum([helper(linenum, line) for linenum, line in enumerate(data)])

if __name__ == '__main__':
    print(main())
