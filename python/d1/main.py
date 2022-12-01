from typing import List

def main():
    d1_part1()
    d1_part2()

def d1_part1():
    track_highs('input_1', 1)

def d1_part2():
    track_highs('input_1', 3)

def track_highs(file, to_track):
    with open(file, 'r') as f:
        current = 0
        tracked: List[int] = []
        
        for line in f:
            stripped = line.strip()
            if stripped == "":
                if len(tracked) < to_track or tracked[0] < current:
                    tracked.append(current)
                    tracked.sort()
                    if len(tracked) > to_track:
                        tracked.pop(0)
                current = 0
            else:
                current += int(stripped)

        print(tracked)
        print(sum(tracked))


if __name__ == "__main__":
    main()