def main():
    d9('input_test')
    d9('input_test_2')
    d9('input_1')

def d9(file):
    d9_part(file, 2)
    d9_part(file, 10)

def d9_part(file, rope_size):
    with open(file, 'r', encoding='utf-8') as f:
        commands = [[comm[0], int(comm[1])] for comm in [line.strip().split(" ") for line in f]]

    rope = [(0, 0) for _ in range(0, rope_size)]
    visited = set()

    for [dir, dist] in commands:
        match dir:
            case "R":
                move = (1, 0)
            case "L":
                move = (-1, 0)
            case "U":
                move = (0, 1)
            case "D":
                move = (0, -1)

        for _ in range(0, dist):
            prev = [i for i in rope]
            for i in range(rope_size - 1, 0, -1):
                t = rope[i-1]

                if i == rope_size - 1:
                    h_old = prev[i]
                    rope[i] = (h_old[0] + move[0], h_old[1] + move[1])
                h = rope[i]

                if abs(h[0] - t[0]) <= 1 and abs(h[1] - t[1]) <= 1:
                    pass
                elif h[0] == t[0]:
                    rope[i-1] = (t[0], int((t[1] + h[1]) / 2))
                elif h[1] == t[1]:
                    rope[i-1] = (int((t[0] + h[0]) / 2), t[1])
                else:
                    movex = 1 if h[0] > t[0] else -1
                    movey = 1 if h[1] > t[1] else -1
                    rope[i-1] = (t[0] + movex, t[1] + movey)

            visited.add(rope[0])

    print(len(visited))

if __name__ == "__main__":
    main()
