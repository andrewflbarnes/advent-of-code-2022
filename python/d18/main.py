def main():
    d18('input_test_small')
    d18('input_test')
    d18('input_1')

def d18(file):
    with open(file, "r", encoding="utf-8") as f:
        drops = set([(int(c[0]), int(c[1]), int(c[2])) for l in f if (c := l.strip().split(","))])

    surface = []
    for drop in drops:
        for drop_side in drop_sides(drop):
            if drop_side not in drops:
                surface.append(drop_side)
    print(len(surface))

    x_min = min([d[0] for d in drops]) - 1
    x_max = max([d[0] for d in drops]) + 1
    y_min = min([d[1] for d in drops]) - 1
    y_max = max([d[1] for d in drops]) + 1
    z_min = min([d[2] for d in drops]) - 1
    z_max = max([d[2] for d in drops]) + 1

    exterior = set()
    next = set()
    next.add((x_min, y_min, z_min))

    while len(next):
        next_point = next.pop()
        if next_point in exterior or next_point in drops:
            continue
        exterior.add(next_point)
        for next_side in drop_sides(next_point):
            x, y, z = next_side
            if x_min <= x <= x_max and y_min <= y <= y_max and z_min <= z <= z_max:
                next.add(next_side)

    print(len(list(filter(lambda x : x in exterior, surface))))


def drop_sides(drop):
    x, y, z = drop
    return [(x - 1, y, z),
            (x + 1, y, z),
            (x, y - 1, z),
            (x, y + 1, z),
            (x, y, z - 1),
            (x, y, z + 1)]

if __name__ == "__main__":
    main()
