from functools import cmp_to_key

def main():
    d14('input_test')
    d14('input_1')

debug = False
debug_steps = 0
sand_src = 500

def d14(file):
    with open(file, "r", encoding="utf-8") as f:
        lines = [[list(map(int, coords.split(","))) for coords in line.strip().split(" -> ")] for line in f]

    paths = get_paths(lines)
    x_min, x_max, _, y_max = get_min_max(paths)

    sand_drop = sand_src - x_min

    # part 1
    pour_sand(paths, sand_drop, x_min, x_max, y_max, False)
    # part 2
    pour_sand(paths, sand_drop, x_min, x_max, y_max, True)

def pour_sand(paths, sand_drop, x_min, x_max, y_max, has_floor):
    rocks = set([(point[0]-x_min, point[1]) for path in paths for point in path])

    debug_step = 0
    settled = 0
    new_settled = 1
    sands = []
    while new_settled > 0:
        new_settled = drop_sand(rocks, sands, sand_drop, x_min, x_max, y_max)
        settled += new_settled
        debug_step += 1
        if debug_steps > 0 and debug_step >= debug_steps:
            break
    print(settled)

def get_paths(lines):
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
    return paths

def get_min_max(paths):
    x_min = min([min([point[0] for point in path]) for path in paths])
    x_max = max([max([point[0] for point in path]) for path in paths])
    y_min = min([min([point[1] for point in path]) for path in paths])
    y_max = max([max([point[1] for point in path]) for path in paths])
    return (x_min, x_max, y_min, y_max)

def drop_sand(rocks, sands, sand_drop, x_start, x_end, y_end):
    sand = (sand_drop, -1)
    while True:
        x = sand[0]
        # print(f'{sand} {sands}')
        frame(rocks, sands, y_end, x_start, x_end, sand)
        next_y = sand[1] + 1
        if next_y > y_end:
            return 0
        
        check = (x, next_y)
        if check not in sands and check not in rocks:
            sand = (x, next_y)
            continue

        for next_x in [x - 1, x + 1]:
            if next_x < 0 or next_x > x_end:
                return 0

            check = (next_x, next_y)
            if check not in sands and check not in rocks:
                sand = check
                break
        else:
            sands.append(sand)
            return 1


def frame(rocks, sands, y_end, x_start, x_end, s = (-1, -1)):
    if not debug:
        return
    for y in range(0, y_end+1):
        for x in range(0, x_end-x_start+1):
            p = (x,y)
            print("o" if p in sands or p == s else "#" if p in rocks else ".", end="")
        print()
    print()


if __name__ == "__main__":
    main()
