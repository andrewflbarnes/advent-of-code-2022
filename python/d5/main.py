import re

def main():
    d5('input_1', 9)

def d5(file, size):
    instruction_pat = re.compile(r"move (?P<num>\d+) from (?P<from>\d+) to (?P<to>\d+)")
    stack_pat = re.compile(r".([^1o])" + r"...(.)" * (size  - 1) + ".")
    stacks = [[], [], [], [], [], [], [], [], []]

    with open(file, 'r') as f:
        lines = [line for line in f]

    for line in lines:
        if (match := stack_pat.match(line)):
            containers = [(i, container) for i in range(0, size, 1) if (container := match.group(i + 1)) and container != " "]
            for action in containers:
                stacks[action[0]].insert(0, action[1])
        elif (match := instruction_pat.match(line)):
            num = int(match.group("num"))
            fr = int(match.group("from")) - 1
            to = int(match.group("to")) - 1
            for i in range(0, num, 1):
                stacks[to].append(stacks[fr].pop())
    
    last = [stack[-1] for stack in stacks]
    print(''.join(last))

if __name__ == "__main__":
    main()
