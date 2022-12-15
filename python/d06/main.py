def main():
    d06('input_test')
    d06('input_1')


def d06(file):
    with open(file, 'r', encoding="UTF=8") as f:
        lines = [line for line in f]

    for line in lines:
        unique_occurrence(line, 4)
        unique_occurrence(line, 14)


def unique_occurrence(line, size):
    groups = [line[x-size:x] for x in range(size, len(line))]

    unique_indexes = [(i + size) for i in range(0, len(groups))
                      if len(set(groups[i])) == size]
    print(unique_indexes[0])


if __name__ == "__main__":
    main()
