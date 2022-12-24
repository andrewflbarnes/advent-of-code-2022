def main():
    d24('input_test')
    d24('input_test_2')
    d24('input_1')


def d24(file):
    with open(file, "r", encoding="utf-8") as f:
        raw = [l.strip() for l in f]

    raw = [[b for x, b in enumerate(r) if 0 < x < len(r) - 1]
           for y, r in enumerate(raw) if 0 < y < len(raw) - 1]
    # for r in raw:
    #     print(r)
    blizzards = get_blizzards(raw)

    # states = [(0, 0, step) for step in range(start_steps) if not blizzard_has(tick_all(blizzards, step), (0, 0))]
    states = {(0, -1, 0)}
    

    y_size = len(raw)
    x_size = len(raw[0])
    leave = (x_size - 1, y_size - 1)

    step = 0
    done = False
    test_blizzards = blizzards
    # frame(test_blizzards, x_size, y_size)
    while not done:
        # if i % 1_0_000 == 0:
        #     print(f'iteration {i}: {len(states)} => {next_step} {(x, y)}')
        # print(f'states {step}: {states}')
        step += 1
        # frame(test_blizzards, x_size, y_size)
        test_blizzards = tick_all(blizzards, step)
        next_states = set()
        for state in states:
            x, y, _ = state
            test_states = [(x, y), (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
            for test_state in test_states:
                next_x, next_y = test_state
                if not (next_x, next_y) == (0, -1) and (not 0 <= next_x < x_size or not 0 <= next_y < y_size):
                    continue
                # print(f'Checking step {next_step} {(next_x, next_y)} // {x_size} {y_size}')
                if not blizzard_has(test_blizzards, (next_x, next_y)):
                    next_states.add((next_x, next_y, step))
                    if leave == (next_x, next_y):
                        done = True
        states = next_states
    # print(next_step + 1)
    print(step + 1)


def get_blizzards(raw):
    left = get_blizzards_x(raw, "<")
    right = get_blizzards_x(raw, ">")
    up = get_blizzards_y(raw, "^")
    down = get_blizzards_y(raw, "v")
    # print("->", up)
    return [left, right, up, down]


def get_blizzards_x(raw, blizz):
    return [{y for y, l in enumerate(raw) if l[x] == blizz} for x in range(len(raw[0]))]


def get_blizzards_y(raw, blizz):
    return [{x for x in range(len(raw[0])) if l[x] == blizz} for l in raw]


def blizzard_has(blizzards, point):
    x, y = point
    left, right, up, down = blizzards
    return y in left[x] or y in right[x] or x in up[y] or x in down[y]

def tick_all(blizzards, steps):
    left, right, up, down = blizzards
    return [tick(left, -1, steps), tick(right, 1, steps), tick(up, -1, steps), tick(down, 1, steps)]


def tick(blizzards, direction, steps=1):
    steps = steps % len(blizzards)
    nb = blizzards
    for _ in range(steps):
        if direction == 1:
            nb = [nb[-1]] + nb[:-1]
        else:
            nb = nb[1:] + [nb[0]]
    return nb

def frame(blizzards, xs, ys):
    for b in blizzards:
        print(b)
    for y in range(ys):
        for x in range(xs):
            print("#" if blizzard_has(blizzards, (x, y)) else ".", end="")
        print()
    print()

if __name__ == "__main__":
    main()
