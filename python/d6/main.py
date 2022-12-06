import re

def main():
    d6('input_test')
    d6('input_1')

def d6(file):
    with open(file, 'r', encoding="UTF=8") as f:
        lines = [line for line in f]

    for line in lines:
        unique_occurrence(line, 4)
        unique_occurrence(line, 14)

def unique_occurrence(line, size):
    groups = [line[x:x+size] for x in range(0, len(line) - size + 1)]

    unique_indexes = [(i + size) for i in range(0, len(groups)) if len(set(groups[i])) == size]
    print(unique_indexes[0])

if __name__ == "__main__":
    main()
