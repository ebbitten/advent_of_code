import re

def load_data():
    with open('data') as f:
        data = [line for line in f.readlines()]
    return data


def solve():
    data = load_data()
    clumped = "".join(data)
    cleaned = [set(ele) - set("\n") for ele in clumped.split("\n\n")]
    print(sum([len(clean_set) for clean_set in cleaned]))

if __name__ == '__main__':
    solve()