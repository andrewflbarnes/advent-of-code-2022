from functools import cmp_to_key

def main():
    d14('input_test')
    #d14('input_1')

def d14(file):
    with open(file, "r", encoding="utf-8") as f:
        lines = [[list(map(int, coords.split(","))) for coords in line.strip().split(" -> ")] for line in f]


    paths = []
    for line in lines:
        path = []
        for i in range(0, len(line)-1):
            start = line[i]
            end = line[i+1]
            x_dir = 1 if end[0] >= start[0] else -1
            y_dir = 1 if end[1] >= start[1] else -1
            coords = [[x,y] for y in range(start[1], end[1]+y_dir, y_dir) for x in range(start[0], end[0]+x_dir, x_dir)]
            path.extend(coords[0 if i == 0 else 1:])
        paths.append(path)

    for p in paths:
        print(p)

    x_max = max([max([point[0] for point in path]) for path in paths])
    x_min = min([min([point[0] for point in path]) for path in paths])
    print(f'x from {x_min} to {x_max}')

    y_max = max([max([point[1] for point in path]) for path in paths])
    y_min = min([min([point[1] for point in path]) for path in paths])
    print(f'x from {x_min} to {x_max}')
    print(f'y from {y_min} to {y_max}')

    rocks = set([(point[0]-x_min, point[1]) for path in paths for point in path])
    print(rocks)

    for y in range(0, y_max+1):
        for x in range(0, x_max-x_min+1):
            print("#" if (x,y) in rocks else ".", end="")
        print()


if __name__ == "__main__":
    main()
