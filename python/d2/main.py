def main():
    d2("input_1")

def d2(file):
    d2_part1(file)
    d2_part2(file)

def d2_part1(file):
    print(get_score(file, strat1))

def get_score(file, strat):
    with open(file, 'r') as f:
        return sum(strat(line.strip()) for line in f)

def strat1(line):
    if line == "A X":
        return 4
    elif line == "A Y":
        return 8
    elif line == "A Z":
        return 3
    elif line == "B X":
        return 1
    elif line == "B Y":
        return 5
    elif line == "B Z":
        return 9
    elif line == "C X":
        return 7
    elif line == "C Y":
        return 2
    elif line == "C Z":
        return 6

def d2_part2(file):
    print(get_score(file, strat2))

def strat2(line):
    if line == "A X":
        return 3
    elif line == "A Y":
        return 4
    elif line == "A Z":
        return 8
    elif line == "B X":
        return 1
    elif line == "B Y":
        return 5
    elif line == "B Z":
        return 9
    elif line == "C X":
        return 2
    elif line == "C Y":
        return 6
    elif line == "C Z":
        return 7

if __name__ == "__main__":
    main()