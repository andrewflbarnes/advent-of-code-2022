def main():
    d12('input_test')
    d12('input_1')

special_points = {
    "S": ord("a"),
    "E": ord("z"),
}

def d12(file):
    with open(file, "r", encoding="utf-8") as f:
        grid = [[[c, -1, -1] for c in line.strip()] for line in f]

    start = get_point(grid, "S")
    end = get_point(grid, "E")

    process_grid(grid, end, start)
    print(grid[end[0]][end[1]][1])
    print(grid[end[0]][end[1]][2])

def process_grid(grid, end, start):
    nexts = [(start, -1, -1)]
    while len(nexts):
        process_point(grid, end, nexts.pop(), nexts)

def process_point(grid, end, this, nexts):
    point, steps, hike_steps = this
    steps += 1
    row, col = point
    [point_l, point_steps, point_hike_steps] = grid[row][col]
    hike_steps = 0 if point_l == "a" else hike_steps + 1
    # print(f'Processing {this} vs {point_l} on {point_steps}/{point_hike_steps} steps')
    if point_l == "S" and steps > 0:
        return

    if point_hike_steps > -1 and point_hike_steps <= hike_steps \
        and point_steps > -1 and point_steps <= steps:
        return

    if point_steps < 0 or steps < point_steps:
        grid[row][col][1] = steps
    if point_hike_steps < 0 or hike_steps < point_hike_steps:
        grid[row][col][2] = hike_steps

    if point == end:
        return

    for next in next_points(grid, point):
        nexts.append((next, steps, hike_steps))
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

    return [x for x in next if letter + 1 >= get_ord(grid[x[0]][x[1]][0])]

def get_ord(letter):
    return ord(letter) if letter not in special_points else special_points[letter]

if __name__ == "__main__":
    main()
