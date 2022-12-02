from typing import List

def main():
    d1("input_1")

def d1(file):
    d1_part1(file)
    d1_part2(file)

def d1_part1(file):
    track_highs(file, 1)

def d1_part2(file):
    track_highs(file, 3)

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