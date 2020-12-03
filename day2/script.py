from typing import List, Tuple

def load_data() -> List[str]:
    with open('data') as f:
        lines = [line.strip() for line in f.readlines()]
    return lines


def break_line(line: str) -> Tuple[str, str, str, str]:
    instruction, string = line.split(':')
    reqs, req_char = instruction.split(' ')
    min_req, max_req = reqs.split('-')
    return (min_req.strip(), max_req.strip(), req_char.strip(), string.strip())


def helper_one(line: str) -> int:
    min_req, max_req, req_char, string = break_line(line)
    count_of_chars = sum((lambda x: 1 if char == req_char else 0)(char) for char in string)
    return 1 if int(min_req) <= count_of_chars <= int(max_req) else 0


def helper_two(line: str) -> int:
    min_req, max_req, req_char, string = break_line(line)
    return 1 if ((string[int(min_req)-1] == req_char) != (string[int(max_req)-1] == req_char)) else 0


def main() -> int:
    lines = load_data()
    #return sum(helper_one(line) for line in lines)
    return sum(helper_two(line) for line in lines)


if __name__ == '__main__':
    print(main())

