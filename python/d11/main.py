import re

def main():
    d11('input_test')
    d11('input_1')

class Monkey:
    def __init__(self, items, inspection, condition):
        self.items = items
        self.inspection = inspection
        self.condition = condition
        self.inspected_count = 0

    def process_next(self):
        if not len(self.items):
            return None

        item = self.items.pop(0)
        #print(f'check {item}')
        stress = int(self.inspection(item) / 3)
        self.inspected_count += 1
        #print(f'stressed {stress}')
        return self.condition(stress)

re_item = re.compile(r"^  Starting items: (.*)")
re_op = re.compile(r"^  Operation: new = (\S+) (\S) (\S+)")
re_test = re.compile(r"  Test: (\w+) by (\d+)")
re_throw = re.compile(r"    If \w+: throw to monkey (\d+)")

def d11(file):
    with open(file, 'r', encoding='utf-8') as f:
        blocks = f.read().split("\n\n")

    monkeys = []
    for block in blocks:
        mdef = block.split("\n")
        items = [int(i) for i in re_item.search(mdef[1]).group(1).split(", ")]
        inspection = parse_inspection(mdef[2])
        condition = parse_condition(mdef[3], mdef[4], mdef[5])

        monkeys.append(Monkey(items, inspection, condition))

    for _ in range(0, 20):
        for monkey in monkeys:
            while (proc := monkey.process_next()):
                #print(f'relieved {proc}')
                to_monkey, stress = proc
                monkeys[to_monkey].items.append(stress)

    for monkey in monkeys:
        print(f'{monkey.inspected_count:<10} {monkey.items}')

    business = sorted([m.inspected_count for m in monkeys])[-2:]
    print(business[0] * business[1])

def parse_inspection(line):
    a, op, b = re_op.search(line).groups()
    def inspection(old):
        op_a = old if a == "old" else int(a)
        op_b = old if b == "old" else int(b)
        match op:
            case "*":
                return op_a * op_b
            case "/":
                return op_a / op_b
            case "-":
                return op_a - op_b
            case "+":
                return op_a + op_b
        raise ValueError("Unrecognised operator: " + op)
    return inspection

def parse_condition(cond, t, f):
    op, s_operand = re_test.search(cond).groups()
    operand = int(s_operand)
    monkey_t = re_throw.search(t).group(1)
    monkey_f = re_throw.search(f).group(1)

    match op:
        case "divisible":
            check = lambda stress: stress % operand == 0
        case _:
            raise ValueError("Invalid operation " + op)

    def condition(stress):
        to_monkey = monkey_t if (check(stress)) else monkey_f
        return (int(to_monkey), stress)

    return condition
        

if __name__ == "__main__":
    main()
