def main():
    d12('input_test')
    d12('input_1')

special_points = {
    "S": ord("a"),
    "E": ord("z"),
}

def d12(file):
    with open(file, "r", encoding="utf-8") as f:
        grid = [[[c, 0] for c in line.strip()] for line in f]

    start = get_point(grid, "S")
    end = get_point(grid, "E")

    process_grid(grid, end, start)
    print(grid[end[0]][end[1]][1])

def process_grid(grid, end, start):
    nexts = [(start, -1)]
    while len(nexts):
        # print((end, nexts[-1], len(nexts)))
        process_point(grid, end, nexts.pop(), nexts)

def process_point(grid, end, this, nexts):
    point, steps = this
    steps += 1
    row, col = point
    [point_l, point_steps] = grid[row][col]
    # print(f'Processing {this} vs {point_l} on {point_steps} steps')
    if (point_l == "S" and steps > 0) or (point_steps > 0 and point_steps <= steps):
        return

    grid[row][col][1] = steps

    if point == end:
        return

    for next in next_points(grid, point):
        nexts.append((next, steps))
    return

def get_point(grid, letter):
    for row in range(0, len(grid)):
        for col in range(0, len(grid[row])):
            if grid[row][col][0] == letter:
                return (row, col)

def next_points(grid, point):
    rows = len(grid)
    cols = len(grid[0])
    next = []
    row, col = point
    if row < rows - 1:
        next.append((row + 1, col))
    if row > 0:
        next.append((row - 1, col))
    if col < cols - 1:
        next.append((row, col + 1))
    if col > 0:
        next.append((row, col - 1))
    
    letter = get_ord(grid[row][col][0])

    # print(letter)
    # print(next)
    # print([(x[0], x[1], grid[x[0]][x[1]], ord(grid[x[0]][x[1]][0])) for x in next])
    return [x for x in next if letter + 1 >= get_ord(grid[x[0]][x[1]][0])]

def get_ord(letter):
    return ord(letter) if letter not in special_points else special_points[letter]

if __name__ == "__main__":
    main()
