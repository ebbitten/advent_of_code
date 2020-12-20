from collections import namedtuple
from typing import List, Dict


class Seat:
    grid = dict(dict())
    xlist = []
    stable = False
    max_rows = 0
    max_columns = 0
    @classmethod
    def set_dimensions(cls, max_rows: int, max_columns: int):
        cls.max_rows = max_rows
        cls.max_columns = max_columns

    @classmethod
    def add_member(cls, seat):
        cls.grid.setdefault(seat.row,{})
        cls.grid[seat.row][seat.column] = seat
        cls.xlist.append(seat)

    @classmethod
    def populate_all_neighbors(cls):
        for seat in cls.xlist:
            seat.populate_neighbors()

    @classmethod
    def update_seats(cls):
        for seat in cls.xlist:
            seat.determine_next_state()
        for seat in cls.xlist:
            seat.update_state()

    @classmethod
    def check_stability(cls):
        if all([x.stable  for x in cls.xlist]):
            cls.stable = True
        else:
            cls.stable = False

    def __init__(self, status: str, row, column):
        self.status = status
        self.next_status: str = ""
        self.row = row
        self.column = column
        self.neighbors: List[Seat]
        self.stable = False
        Seat.add_member(self)

    def __repr__(self):
        return f'row: {self.row}, column: {self.column}, status: {self.status}, next_status: {self.next_status}'

    def populate_neighbors(self):
        neighbors = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                row = self.row + i
                column = self.column + j
                if i == j == 0:
                    continue
                row_group = Seat.grid.get(row)
                if row_group:
                    neighbor = row_group.get(column)
                    if neighbor:
                        neighbors.append(neighbor)
        self.neighbors = neighbors

    def determine_next_state(self):
        if self.status == ".":
            self.next_status = "."
        occupied_neighbors = sum([(lambda x: 1 if x.status == "#" else 0)(x) for x in self.neighbors])
        if self.status == "L":
            if occupied_neighbors == 0:
                self.next_status = "#"
            else:
                self.next_status = "L"
        if self.status == "#":
            if occupied_neighbors >= 5:
                self.next_status = "L"
            else:
                self.next_status = "#"

    def update_state(self):
        if self.status == self.next_status:
            self.stable = True
        else:
            self.stable = False
        self.status = self.next_status


def load_data():
    with open('data') as f:
        data = [line.strip() for line in f.readlines()]
    return data


def main():
    data = load_data()
    rows = len(data)
    columns = len(data[0])
    Seat.set_dimensions(rows, columns)
    for row, line in enumerate(data):
        for column, char in enumerate(line):
            Seat(char, row, column)
    Seat.populate_all_neighbors()
    loops = 0
    while not Seat.stable:
        loops += 1
        # print(loops)
        print(sum([(lambda x: 1 if x.status == "#" else 0)(x) for x in Seat.xlist]))
        Seat.update_seats()
        Seat.check_stability()
    print(sum([(lambda x: 1 if x.status == "#" else 0) (x) for x in Seat.xlist]))
    print([x.status for x in Seat.xlist])




if __name__ == '__main__':
    main()
