import re

def main():
    d6('input_test')
    d6('input_1')

def d6(file):
    with open(file, 'r') as f:
        lines = [line for line in f]
    
    for line in lines:
        groups = [line[x:x+4] for x in range(0, len(line) - 3)]

        unique_indexes = [(i + 4) for i in range(0, len(groups)) if (len(set(groups[i])) == 4)]
        print(unique_indexes[0])

if __name__ == "__main__":
    main()
