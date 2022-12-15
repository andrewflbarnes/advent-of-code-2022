def main():
    d03('input_1')

def d03(file):
    d3_part1(file)
    d3_part2(file)

def d3_part1(file):
    with open(file, 'r') as f:
        repeats = [get_repeated(line.strip()) for line in f]
    print(sum(repeats))

def get_repeated(line):
    mid = len(line)//2
    c1 = set(line[:mid])
    c2 = set(line[mid:])
    both = [x for x in c1 if x in c2][0]
    return pri(both)

def pri(item):
    base = 96 if item > 'Z' else 38
    return ord(item) - base

def d3_part2(file):
    with open(file, 'r') as f:
        lines = [line.strip() for line in f]
        groups = [lines[n:n+3] for n in range(0, len(lines), 3)]
    # repeats = [[group for group in groups if x in group[0] and x in group[1] and x in group[2]]]
    repeats =[[x for x in group[0] if x in group[1] and x in group[2]][0] for group in groups]
    print(sum([pri(x) for x in repeats]))

if __name__ == "__main__":
    main()
