def main():
    d1_part1()

def d1_part1():
    with open('input_1', 'r') as f:
        current = 0
        highest = 0
        
        for line in f:
            stripped = line.strip()
            if stripped == "":
                highest = max(current, highest)
                current = 0
            else:
                current += int(stripped)

        highest = max(highest, current)
        print(highest)

if __name__ == "__main__":
    main()