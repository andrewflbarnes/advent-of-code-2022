def main():
    d4('input_1')

def d4(file):
    d4_part1(file)

def d4_part1(file):
    with open(file, 'r') as f:
        sects = [[[int(i) for i in sections.split("-")] for sections in line.strip().split(',')] for line in f]
    spread = [[pair[0][x] - pair[1][x] for x in range(0, 2, 1)] for pair in sects]
    contained = [pair for pair in spread if pair[0] == 0 or pair[1] == 0 or pair[0] ^ pair[1] < 0]
    print(len(contained))

if __name__ == "__main__":
    main()
