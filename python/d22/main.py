import numbers

def main():
    d22('input_test')
    d22('input_1')

def d22(file):
    with open(file, "r", encoding="utf-8") as f:
        raw = f.read().split("\n\n")

    path = [int(p) if p.isnumeric() else p
            for p in raw[1].replace("R", " R ").replace("L", " L ").split(" ")]
    layout = [[0 if p == " " else 1 if p == "." else 2 for p in l]
              for l in raw[0].split("\n")]
    max_cols = max(len(l) for l in layout)
    layout = [l + [0] * (max_cols - len(l)) for l in layout]

    start = (min(i for i, v in enumerate(layout[0]) if v == 1), 0)
    face = 'R'
    loc = start
    # frame(layout, loc)
    for instr in path:
        if isinstance(instr, numbers.Number):
            loc = walk(loc, layout, face, instr)
            # frame(layout, loc)
        else:
            face = turn(face, instr)
    print(get_pass(face, loc))

def turn(face, direction):
    match face:
        case "R":
            return "D" if direction == "R" else "U"
        case "U":
            return "R" if direction == "R" else "L"
        case "L":
            return "U" if direction == "R" else "D"
        case "D":
            return "L" if direction == "R" else "R"
        case _:
            raise ValueError(f"Unexpected face: {face}")

def walk(loc, layout, face, steps):
    x_size = len(layout[1])
    y_size = len(layout)
    x_dir, y_dir = walk_dir(face)
    x, y = loc
    for _ in range(steps):
        next_x = x + x_dir
        next_y = y + y_dir
        if x_dir != 0:
            if next_x < 0 or next_x >= x_size or layout[next_y][next_x] == 0:
                testx = next_x - x_dir
                while testx >= 0 and testx < x_size and layout[next_y][testx] != 0:
                    next_x = testx
                    testx = next_x - x_dir
        if y_dir != 0:
            if next_y < 0 or next_y >= y_size or layout[next_y][next_x] == 0:
                testy = next_y - y_dir
                while testy >= 0 and testy < y_size and layout[testy][next_x] != 0:
                    next_y = testy
                    testy = next_y - y_dir
        if layout[next_y][next_x] == 2:
            return x, y
        x = next_x
        y = next_y
    return x, y

def walk_dir(face):
    match face:
        case "R":
            return 1, 0
        case "U":
            return 0, -1
        case "L":
            return -1, 0
        case "D":
            return 0, 1
        case _:
            raise ValueError(f"Unexpected face for walk direction: {face}")

def get_pass(face, loc):
    x, y = loc
    face_val = -1
    match face:
        case 'R':
            face_val = 0
        case 'D':
            face_val = 1
        case 'L':
            face_val = 2
        case 'U':
            face_val = 3
        case _:
            raise ValueError(f'Unexpected face for determining pass: {face}')
    return 1000 * (y + 1) + 4 * (x + 1) + face_val

def frame(layout, loc):
    print()
    for y, line in enumerate(layout):
        line = layout[y]
        for x, v in enumerate(line):
            if (x, y) == loc:
                print('X', end="")
            else:
                match v:
                    case 0:
                        print(" ", end="")
                    case 1:
                        print(".", end="")
                    case 2:
                        print("#", end="")
        print()

if __name__ == "__main__":
    main()
