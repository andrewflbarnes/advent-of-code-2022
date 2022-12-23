import numbers

def main():
    d22('input_test', 4, [(0, 2, 0), (2, 3, 2), (2, 2, 2), (1, 1, 1), (1, 2, 0), (1, 0, 2)])
    d22('input_1', 50, [(0, 1, 0), (0, 2, 0), (2, 1, 2), (2, 0, 2), (1, 1, 0), (3, 0, 3)])
# layout is FRBLDU with clockwise 90deg clockwise rotations to make FRBL oriented to F
# and UD oriented
# U
# F
# D
# i.e. this gives us a consistent layout:
# U
# F R B L
# D
def d22(file, size, faces):
    with open(file, "r", encoding="utf-8") as f:
        raw = f.read().split("\n\n")

    path = [int(p) if p.isnumeric() else p
            for p in raw[1].replace("R", " R ").replace("L", " L ").split(" ")]
    layout = [[0 if p == " " else 1 if p == "." else 2 for p in l]
              for l in raw[0].split("\n")]
    max_cols = max(len(l) for l in layout)
    layout = [l + [0] * (max_cols - len(l)) for l in layout]
    
    d22_part1(path, layout)
    d22_part2(path, layout, size, faces)

def d22_part1(path, layout):
    start = (min(i for i, v in enumerate(layout[0]) if v == 1), 0)
    look ='R'
    loc = start
    # frame(layout, loc)
    for instr in path:
        if isinstance(instr, numbers.Number):
            loc = walk(loc, layout, look, instr)
            # frame(layout, loc)
        else:
            look = turn(look, instr)
    print(get_pass(look, loc))

def d22_part2(path, layout, size, faces):
    look ='R'
    face_layout = get_faces(layout, size, faces)
    start = (0, 0, 0)  # (face, x, y)
    loc = start
    # frame2(face_layout, loc)
    for instr in path:
        if isinstance(instr, numbers.Number):
            # print(f'walk {look} {instr}')
            loc, look = walk_2(loc, face_layout, look, instr)
            # frame2(face_layout, loc)
        else:
            look = turn(look, instr)
    f_idx, x, y = loc
    face = faces[f_idx]
    r, c, rot = face
    res_x = x
    res_y = y
    res_look = look
    for _ in range(rot):
        temp = res_y
        res_y = size - res_x - 1
        res_x = temp
        res_look = turn(res_look, 'L')
    res_x = c * size + res_x
    res_y = r * size + res_y
    print(get_pass(res_look, (res_x, res_y)))

def get_faces(layout, size, faces):
    face_layout = []
    for row, col, rot in faces:
        face = []
        for r in range(row * size, (row + 1) * size):
            fr = []
            face.append(fr)
            for c in range(col * size, (col + 1) * size):
                fr.append(layout[r][c])
        face_layout.append(rot_face(face, rot))
    return face_layout

def rot_face(face, rot):
    ret = face
    for _ in range(rot):
        ret = list(zip(*ret[::-1]))
    return ret


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

def walk_2(loc, face_layout, look, steps):
    f_idx, x, y = loc
    face = face_layout[f_idx]
    size = len(face)

    for _ in range(steps):
        x_dir, y_dir = walk_dir(look)
        next_x = x + x_dir
        next_y = y + y_dir
        next_face = face
        next_f_idx = f_idx
        next_look = look
        if next_x < 0 or next_x >= size or next_y < 0 or next_y >= size:
            next_f_idx, next_look, next_x, next_y = move_face(f_idx, look, x, y, size)
            # print(f'move face from {f_idx} {look} {(x,y)} to {next_f_idx} {next_look} {(next_x, next_y)}')
            next_face = face_layout[next_f_idx]

        if next_face[next_y][next_x] == 2:
            return (f_idx, x, y), look
        x = next_x
        y = next_y
        face = next_face
        f_idx = next_f_idx
        look = next_look
    return (f_idx, x, y), look

def move_face(f_idx, look, x, y, size):
    if f_idx < 4:
        if look == 'R':
            return (f_idx + 1) % 4, look, 0, y
        if look == 'L':
            return (f_idx - 1) % 4, look, size - 1, y

    if f_idx == 0:
        if look == 'U':
            return 5, look, x, size - 1
        if look == 'D':
            return 4, look, x, 0
    if f_idx == 1:
        if look == 'U':
            return 5, 'L', size - 1, size - 1 - x
        if look == 'D':
            return 4, 'L', size - 1, x
    if f_idx == 2:
        if look == 'U':
            return 5, 'D', size - 1 - x, 0
        if look == 'D':
            return 4, 'U', size - 1 - x, size - 1
    if f_idx == 3:
        if look == 'U':
            return 5, 'R', 0, x
        if look == 'D':
            return 4, 'R', 0, size - 1 - x

    if f_idx == 4:
        if look == 'R':
            return 1, 'U', y, size - 1
        if look == 'U':
            return 0, 'U', x, size - 1
        if look == 'L':
            return 3, 'U', size - 1 - y, size - 1
        if look == 'D':
            return 2, 'U', size - 1 - x, size - 1

    if f_idx == 5:
        if look == 'R':
            return 1, 'D', size - 1 - y, 0
        if look == 'U':
            return 2, 'D', size - 1 - x, 0
        if look == 'L':
            return 3, 'D', y, 0
        if look == 'D':
            return 0, 'D', x, 0



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

def frame2(layout, loc):
    for y, l in enumerate(layout[5]):
        for x, c in enumerate(l):
            if (5, x, y) == loc:
                print("X", end="")
            else:
                print("." if c == 1 else "#", end="")
        print()
    for y in range(len(layout[0])):
        for i in range(4):
            for x, c in enumerate(layout[i][y]):
                if (i, x, y) == loc:
                    print("X", end="")
                else:
                    print("." if c == 1 else "#", end="")
        print()
    for y, l in enumerate(layout[4]):
        for x, c in enumerate(l):
            if (4, x, y) == loc:
                print("X", end="")
            else:
                print("." if c == 1 else "#", end="")
        print()
    print()

if __name__ == "__main__":
    main()
