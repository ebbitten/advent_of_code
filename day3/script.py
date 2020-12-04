from itertools import cycle
from math import prod
from collections import namedtuple


Trajectory = namedtuple('Trajectory', 'rightoffset, downoffset')

TRAJECTORIES = [Trajectory(1,1), Trajectory(3,1), Trajectory(5,1), Trajectory(7,1), Trajectory(1,2)]

class SubscriptableCycle(cycle):
    def __getitem__(self, item):
        for i in range(item):
            self.__next__()
        return self.__next__()

def get_data():
    with open('data') as f:
        data = [SubscriptableCycle(line.strip()) for line in f.readlines()]
    return data


def helper(linenum, line, rightoffset):
    return_val = 1 if line[linenum*rightoffset] == "#" else 0
    print(return_val)
    return return_val

def outerloop(data, rightoffset, downoffset):
    filtered_data = [line for linenum, line in enumerate(data) if linenum % downoffset == 0]
    return sum([helper(linenum, line, rightoffset) for linenum, line in enumerate(filtered_data)])

def main():
    return prod([outerloop(get_data(), trajectory.rightoffset, trajectory.downoffset) for
                 trajectory in TRAJECTORIES])


if __name__ == '__main__':
    print(main())
