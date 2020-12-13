from typing import List


class BootDriveOne:
    def __init__(self, datafile):
        self.datafile = datafile
        self.lines: List[str] = []
        self.current_line_index = 0
        self.lines_visited = set()
        self.accumulator = 0
        print('parsing')
        self.parse_lines()

    def parse_lines(self):
        with open(self.datafile) as f:
            self.lines = [line.strip() for line in f.readlines()]

    def boot(self):
        print(self.lines)
        while self.current_line_index not in self.lines_visited:
            self.lines_visited.add(self.current_line_index)
            line = self.lines[self.current_line_index]
            cmd = line[0:3]
            if cmd == 'nop':
                self.current_line_index += 1
                continue
            elif cmd == 'acc':
                self.current_line_index += 1
                self.accumulator += int(line[4:])
            elif cmd == 'jmp':
                self.current_line_index += int(line[4:])
        print(self.accumulator)
        return self.accumulator


def part_one():
    boot = BootDriveOne('data')
    print(boot.boot())

class BootDriveTwo:
    def __init__(self, datafile, line_change):
        self.datafile = datafile
        self.line_change = line_change
        self.lines: List[str] = []
        self.current_line_index = 0
        self.lines_visited = set()
        self.accumulator = 0
        print('parsing')
        self.parse_lines()

    def parse_lines(self):
        with open(self.datafile) as f:
            self.lines = [line.strip() for line in f.readlines()]

    def boot(self):
        while self.current_line_index not in self.lines_visited:
            self.lines_visited.add(self.current_line_index)
            line = self.lines[self.current_line_index]
            cmd = line[0:3]
            if self.current_line_index == self.line_change:
                if cmd == 'jmp':
                    cmd = 'nop'
                elif cmd == 'nop':
                    cmd = 'jmp'
            if cmd == 'nop':
                self.current_line_index += 1
            elif cmd == 'acc':
                self.current_line_index += 1
                self.accumulator += int(line[4:])
            elif cmd == 'jmp':
                self.current_line_index += int(line[4:])
            print(self.current_line_index)
            if self.current_line_index == len(self.lines):
                print('accumulated', self.accumulator)
                return self.accumulator
        return 0

def part_two():
    bootone = BootDriveOne('data')
    attempts = [BootDriveTwo('data', i).boot() for i in range(len(bootone.lines))]
    print(attempts)
    print(sum(attempts))


if __name__ == '__main__':
    part_two()



