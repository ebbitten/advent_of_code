
def load_data():
    with open('data') as f:
        data = [line.strip() for line in f.readlines()]
    return data


def row_helper(row):
    map = {'F': 0, 'B': 1}
    print(list(enumerate(row)))
    print((sum([2**(6-position) * map[char] for position, char in enumerate(row)])))
    return (sum([2**(6-position) * map[char] for position, char in enumerate(row)]))*8


def column_helper(column):
    map = {'R': 1, 'L' :0}
    print(list(enumerate(column)))
    print(sum([2**(2-position) * map[char] for position, char in enumerate(column)]))
    return sum([2**(2-position) * map[char] for position, char in enumerate(column)])


def outer():
    data = load_data()
    positions = [row_helper(line[0:7]) + column_helper(line[7:10]) for line in data]
    print(positions)
    return max(positions)


def outer_part_2():
    data = load_data()
    positions = sorted([row_helper(line[0:7]) + column_helper(line[7:10]) for line in data])
    for idx, val in enumerate(positions):
        if abs((next_val := positions[idx+1]) - val) == 2:
            return (next_val + val)/2



def test():
    line = 'BBFFBBFRLL'
    print(row_helper(line[0:7]) + column_helper(line[7:10]))

# test()
# print(outer())
print(outer_part_2())