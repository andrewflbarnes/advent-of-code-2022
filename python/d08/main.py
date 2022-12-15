def main():
    d08('input_test')
    d08('input_1')

def d08(file):
    with open(file, 'r', encoding='utf-8') as f:
        trees = [[int(tree) for tree in line.strip()] for line in f]

    rows = len(trees)
    cols = len(trees[0])

    vis_mat = [[0 for _ in range(0, cols)] for _ in range(0, rows)]
    scenic_mat = [[1 for _ in range(0, cols)] for _ in range(0, rows)]

    # rows
    for direction in [-1, 1]:
        for i in range(0, rows):
            highest = -1
            last_high = [0 if direction == 1 else rows - 1 for _ in range(0, 10)]
            for j in range(0, cols)[::direction]:
                tree = trees[i][j]
                if tree > highest or highest == -1:
                    vis_mat[i][j] = 1
                    highest = tree
                scenic_mat[i][j] *= max(0, direction * (j - last_high[tree]))
                for h in range(0, tree + 1):
                    last_high[h] = j

    # cols
    for direction in [-1, 1]:
        # no need for first or last as already all visible and scenic 0 in previous step
        for j in range(1, cols - 1):
            highest = -1
            last_high = [0 if direction == 1 else cols - 1 for _ in range(0, 10)]
            for i in range(0, rows)[::direction]:
                tree = trees[i][j]
                if tree > highest or highest == -1:
                    vis_mat[i][j] = 1
                    highest = tree
                scenic_mat[i][j] *= max(0, direction * (i - last_high[tree]))
                for h in range(0, tree + 1):
                    last_high[h] = i

    print(sum([sum(line) for line in vis_mat]))
    print(max([max(line) for line in scenic_mat]))

if __name__ == "__main__":
    main()
