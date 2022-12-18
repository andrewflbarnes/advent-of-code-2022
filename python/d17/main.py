def main():
    d17('input_test')
    d17('input_1')

rocks = [
    [[1, 1, 1, 1]],             # -
    [[0,1,0],[1,1,1],[0,1,0]],  # +
    [[0,0,1],[0,0,1],[1,1,1]],  # ┘
    [[1],[1],[1],[1]],          # |
    [[1,1],[1,1]]               # □
]

def d17(file):
    with open(file, "r", encoding="utf-8") as f:
        jet = [j for j in f.readline()]

    print(drop_rocks(2022, jet))
    print(drop_rocks(1_000_000_000_000, jet))

def drop_rocks(num_rocks, jet):
    grid = []
    # frame(grid)
    jet_idx = 0
    jet_restarted = False
    truncated = 0
    truncations_info = dict()
    break_condition = -1
    for i in range(0, num_rocks):
        if i == break_condition:
            break
        rock = rocks[i % len(rocks)]
        jet_next_idx = drop(rock, grid, jet, jet_idx)
        if jet_next_idx < jet_idx:
            jet_restarted = True
        jet_idx = jet_next_idx
        # Only keep the fewest number of rows of grid possible i.e. where at some point each x
        # position is blocked (or down to the floor)
        grid, removed, hash = truncate(grid)
        # High num_rocks processing:
        #
        # Every time the grid is succesfully truncated we store the hash (basically the truncated
        # grid) against how many iterations there have been and the current number of truncations.
        #
        # We can then wait until we see this same hash and know that we have a "cycle" which is
        # the number of iterations between when these hashes were seen. The difference in
        # truncations is how many were performed in that cycle.
        #
        # We can then find the number of complete cycles remaining and then multiply this by the
        # number of removals per cycle only iterating over the remainder.
        #
        # Calculating any size cycle reduces this to a relatively trivial number of iterations so
        # there is no need to search for a large cycle, as long as we have processed the jet stream
        # in full at least once.
        if hash != 0 and break_condition < 0:
            if hash in truncations_info:
                if jet_restarted:
                    last_iter, last_truncated = truncations_info[hash]
                    cycle_iters = i - last_iter
                    cycle_removed = truncated - last_truncated
                    cycles = (num_rocks - i) // cycle_iters
                    continuation = (num_rocks - i) % cycle_iters
                    projected = cycles * cycle_removed
                    truncated += projected
                    break_condition = i + continuation
            else:
                truncations_info[hash] = (i, truncated)
        truncated += removed
        # frame(grid)
    # frame(grid)
    return truncated + len(grid)

def drop(rock, grid, jet, jet_idx):
    origin = 2, len(grid) + 3
    while True:
        jet_adj = -1 if jet[jet_idx] == '<' else 1
        if not collide(rock, origin, grid, (jet_adj, 0)):
            origin = origin[0] + jet_adj, origin[1]
        jet_idx = 0 if jet_idx == len(jet) - 1 else jet_idx + 1
        if collide(rock, origin, grid, (0, -1)):
            update_grid(rock, origin, grid)
            return jet_idx
        origin = origin[0], origin[1] - 1

def collide(rock, origin, grid, movement):
    m_x, m_y = movement
    o_x, o_y = origin
    n_x = o_x + m_x
    if (n_x < 0 or n_x + len(rock[0]) > 7):
        return True
    n_y = o_y + m_y
    if n_y < 0:
        return True
    check = []
    rock_height = len(rock)
    for r_y in range(0, rock_height):
        rock_line = rock[r_y]
        for r_x in range(0, len(rock_line)):
            if rock_line[r_x] == 1:
                check.append((n_x + r_x, n_y + rock_height - r_y - 1))

    for x, y in check:
        if len(grid) > y and len(grid[y]) > x and grid[y][x] == 1:
            return True
    return False

def update_grid(rock, origin, grid):
    o_x, o_y = origin
    r_height = len(rock)
    for r_y in range(0, r_height):
        for r_x in range(0, len(rock[r_y])):
            y = o_y + r_height - r_y - 1
            x = o_x + r_x

            while len(grid) <= y:
                grid.append([0,0,0,0,0,0,0])
            if rock[r_y][r_x] == 1:
                grid[y][x] = 1

def truncate(grid):
    found = [0] * 7

    y = len(grid)
    while sum(found) != len(found):
        y -= 1
        if y < 0:
            return grid, 0, 0

        found = [a|b for a,b in zip(found, grid[y])]
    if y > 0:
        return grid[y:], y, str(y) + ''.join([''.join([str(i) for i in line]) for line in grid])

    return grid, 0, 0

def frame(grid):
    height = max(10, len(grid))
    for i in range(height, -1, -1):
        if len(grid) > i:
            print(f'|{"".join(["#" if j == 1 else "." for j in grid[i]])}|')
        else:
            print('|.......|')
    print('+-------+')

if __name__ == "__main__":
    main()
