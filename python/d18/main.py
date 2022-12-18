def main():
    d18('input_test_small')
    d18('input_test')
    d18('input_1')

def d18(file):
    with open(file, "r", encoding="utf-8") as f:
        drops = set([(int(c[0]), int(c[1]), int(c[2])) for l in f if (c := l.strip().split(","))])

    surf_area = 0
    for drop in drops:
        x, y, z = drop
        surf_area += sum([
            0 if (x - 1, y, z) in drops else 1,
            0 if (x + 1, y, z) in drops else 1,
            0 if (x, y - 1, z) in drops else 1,
            0 if (x, y + 1, z) in drops else 1,
            0 if (x, y, z - 1) in drops else 1,
            0 if (x, y, z + 1) in drops else 1,
        ])
    print(surf_area)


if __name__ == "__main__":
    main()
