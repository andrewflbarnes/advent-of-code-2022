def main():
    d10('input_test')
    d10('input_1')

opcodes = {
    "noop": [1, 0, lambda regs, op : regs[0]],
    "addx": [2, 0, lambda regs, op : regs[0] + int(op[1])],
}

def d10(file):
    with open(file, 'r', encoding='utf-8') as f:
        commands = [line.strip().split(" ") for line in f]

    regs = [1]
    cycle = 0
    strength = 0
    crt = [[]]

    for command in commands:
        opcode = command[0]
        [cycles, outreg, instr] = opcodes[opcode]
        for _ in range(0, cycles):
            update_crt(crt, regs)
            cycle += 1
            if (cycle - 20) % 40 == 0:
                # print(f'{cycle} {regs} => {cycle * regs[0]}')
                strength += cycle * regs[0]
        
        regs[outreg] = instr(regs, command)
    
    print(strength)
    for line in crt:
        print(''.join(line))

def update_crt(crt, regs):
    current_line = crt[-1]
    if len(current_line) == 40:
        current_line = []
        crt.append(current_line)
    current_pixel = len(current_line)

    x = regs[0]
    next = "#" if x - 1 <= current_pixel <= x + 1 else "."
    current_line.append(next)
        


if __name__ == "__main__":
    main()
