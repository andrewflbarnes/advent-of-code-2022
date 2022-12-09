#!/usr/bin/env python

def main():
    d9('input_test')
    d9('input_1')

def d9(file):
    with open(file, 'r', encoding='utf-8') as f:
        commands = [[comm[0], int(comm[1])] for comm in [line.strip().split(" ") for line in f]]

    h = (0, 0)
    t = (0, 0)
    visited = set()

    for [dir, dist] in commands:
        for _ in range(0, dist):
            h_old = (h[0], h[1])

            match dir:
                case "R":
                    move = (1, 0)
                case "L":
                    move = (-1, 0)
                case "U":
                    move = (0, 1)
                case "D":
                    move = (0, -1)

            h = (h[0] + move[0], h[1] + move[1])
            t_old = (t[0], t[1])

            if abs(h[0] - t[0]) <= 1 and abs(h[1] - t[1]) <= 1:
                pass
            elif h[0] != t[0] and h[1] != t[1]:
                t = (h_old[0], h_old[1])
            else:
                t = (t[0] + move[0], t[1] + move[1])

            visited.add(t)

    print(len(visited))

if __name__ == "__main__":
    main()
