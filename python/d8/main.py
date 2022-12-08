def main():
    d8('input_test')
    d8('input_1')

def d8(file):
    with open(file, 'r', encoding='utf-8') as f:
        trees = [[int(tree) for tree in line.strip()] for line in f]

    rows = len(trees)
    cols = len(trees[0])

    vis_mat = [[0 for i in range(0, cols)] for j in range(0, rows)]

    # rows
    for direction in [-1, 1]:
        for i in range(0, rows):
            highest = -1
            for j in range(0, cols)[::direction]:
                if vis_mat[i][j]:
                    break
                tree = trees[i][j]
                if tree > highest or highest == -1:
                    vis_mat[i][j] = 1
                    highest = tree
                if highest == 9:
                    break

    # cols
    for direction in [-1, 1]:
        # no need for first or last as already all visible in previous step
        for j in range(1, cols - 1):
            highest = -1
            for i in range(0, rows)[::direction]:
                tree = trees[i][j]
                # print(f'check {i}.{j} = {tree} vs {highest}')
                if tree > highest or highest == -1:
                    vis_mat[i][j] = 1
                    highest = tree
                if highest == 9:
                    break
               
    for line in vis_mat:
        print("".join([str(x) for x in line]))
    print(sum([sum(line) for line in vis_mat]))


if __name__ == "__main__":
    main()