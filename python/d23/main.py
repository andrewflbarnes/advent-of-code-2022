def main():
    d23('input_test_small', 3)
    d23('input_test', 10)
    d23('input_1', 10)


def d23(file, iterations):
    with open(file, "r", encoding="utf-8") as f:
        raw = [[0 if c == "." else 1 for c in l.strip()] for l in f]
    elves = {(x, y) for y in range(len(raw))
             for x in range(len(raw[0])) if raw[y][x] == 1}

    dir = 0  # 0:N, 1:S, 2:W, 3:E
    # frame(elves)
    for _ in range(iterations):
        # print(f'iteration {_} with dir {dir}')
        may_move = {e for e in elves if sum(1 if (x, y) in elves and (
            x, y) != e else 0 for x in range(e[0] - 1, e[0] + 2) for y in range(e[1] - 1, e[1] + 2)) > 0}
        proposed = dict()
        for e in may_move:
            if (move := propose_move(dir, e, elves)):
                if move is None:
                    raise ValueError("BLOOP")
                proposed[move] = None if move in proposed else e
        elves = {e for e in elves if e not in may_move}\
            .union({e for e in may_move if e not in proposed.values()})\
            .union({to for to, frm in proposed.items() if frm is not None})
        dir = (dir + 1) % 4
        # frame(elves)
    print(count_elf_rect(elves))


elf_checks = {
    0: lambda x, y: [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1)],
    1: lambda x, y: [(x - 1, y + 1), (x, y + 1), (x + 1, y + 1)],
    2: lambda x, y: [(x - 1, y + 1), (x - 1, y), (x - 1, y - 1)],
    3: lambda x, y: [(x + 1, y + 1), (x + 1, y), (x + 1, y - 1)],
}
elf_propose = {
    0: lambda x, y: (x, y - 1),
    1: lambda x, y: (x, y + 1),
    2: lambda x, y: (x - 1, y),
    3: lambda x, y: (x + 1, y),
}


def propose_move(dir, elf, elves):
    x, y = elf
    # print(f'check elf {elf}')
    for _ in range(4):
        # print(f'{dir}: {elf_checks[dir](x, y)}')
        if sum(1 if c in elves else 0 for c in elf_checks[dir](x, y)) == 0:
            # print(f'proposing {elf_propose[dir](x, y)}')
            return elf_propose[dir](x, y)
        dir = (dir + 1) % 4
    return None

def count_elf_rect(elves):
    min_x = min(x for x, _ in elves)
    max_x = max(x for x, _ in elves)
    min_y = min(y for _, y in elves)
    max_y = max(y for _, y in elves)
    return (max_x + 1 - min_x) * (max_y + 1 - min_y) - len(elves)


def frame(elves):
    min_x = min(x for x, _ in elves)
    max_x = max(x for x, _ in elves)
    min_y = min(y for _, y in elves)
    max_y = max(y for _, y in elves)

    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            print("#" if (x, y) in elves else ".", end="")
        print()
    print()


if __name__ == "__main__":
    main()
