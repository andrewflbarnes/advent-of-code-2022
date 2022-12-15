import re

def main():
    d05('input_test', 3)
    d05('input_1', 9)

def d05(file, size):
    instruction_pat = re.compile(r"move (\d+) from (\d+) to (\d+)")
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
            num, fr, to = (int(x) for x in match.groups())
            in_point = len(stacks_2[to - 1])
            for _ in range(0, num):
                stacks[to - 1].append(stacks[fr - 1].pop())
                stacks_2[to - 1].insert(in_point, stacks_2[fr - 1].pop())
    
    last = [stack[-1] for stack in stacks if (len(stack))]
    print(''.join(last))
    last_2 = [stack[-1] for stack in stacks_2 if (len(stack))]
    print(''.join(last_2))

if __name__ == "__main__":
    main()
