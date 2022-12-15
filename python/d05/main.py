import re

def main():
    d05('input_test', 3)
    d05('input_1', 9)

def d05(file, size):
    instruction_pat = re.compile(r"move (?P<num>\d+) from (?P<from>\d+) to (?P<to>\d+)")
    stack_pat = re.compile(r".([^1o])" + r"...(.)" * (size  - 1) + ".")
    stacks = [[] for _ in range(0, size)]
    stacks_2 = [[] for _ in range(0, size)]

    with open(file, 'r') as f:
        lines = [line for line in f]

    for line in lines:
        if (match := stack_pat.match(line)):
            containers = [(i, container) for i in range(0, size, 1) if (container := match.group(i + 1)) and container != " "]
            for action in containers:
                stacks[action[0]].insert(0, action[1])
                stacks_2[action[0]].insert(0, action[1])
        elif (match := instruction_pat.match(line)):
            num = int(match.group("num"))
            fr = int(match.group("from")) - 1
            to = int(match.group("to")) - 1
            in_point = len(stacks_2[to])
            for i in range(0, num, 1):
                stacks[to].append(stacks[fr].pop())
                stacks_2[to].insert(in_point, stacks_2[fr].pop())
    
    last = [stack[-1] for stack in stacks if (len(stack))]
    print(''.join(last))
    last_2 = [stack[-1] for stack in stacks_2 if (len(stack))]
    print(''.join(last_2))

if __name__ == "__main__":
    main()
