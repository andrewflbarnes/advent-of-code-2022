import re

stress_modulo = 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19
stress_modulo_test = 13 * 17 * 19 * 23

def main():
    d11('input_test', stress_modulo_test)
    d11('input_1')

class Monkey:
    def __init__(self, items, inspection, relief, stress_mod, condition):
        self.items = items
        self.inspection = inspection
        self.relief = relief
        self.stress_mod = stress_mod
        self.condition = condition
        self.inspected_count = 0

    def process_next(self):
        if not len(self.items):
            return None

        item = self.items.pop(0)
        stress = int(self.inspection(item) / self.relief) % self.stress_mod
        self.inspected_count += 1
        return self.condition(stress)

def d11(file, stress_mod = stress_modulo):
    d11_part(file, 3, 20, stress_mod)
    d11_part(file, 1, 10_000, stress_mod)

re_item = re.compile(r"^  Starting items: (.*)")
re_op = re.compile(r"^  Operation: new = (\S+) (\S) (\S+)")
re_test = re.compile(r"  Test: (\w+) by (\d+)")
re_throw = re.compile(r"    If \w+: throw to monkey (\d+)")

def d11_part(file, relief, rounds, stress_mod):
    with open(file, 'r', encoding='utf-8') as f:
        blocks = f.read().split("\n\n")

    monkeys = []
    for block in blocks:
        mdef = block.split("\n")
        items = [int(i) for i in re_item.search(mdef[1]).group(1).split(", ")]
        inspection = parse_inspection(mdef[2])
        condition = parse_condition(mdef[3], mdef[4], mdef[5])
        monkeys.append(Monkey(items, inspection, relief, stress_mod, condition))

    for _ in range(0, rounds):
        for monkey in monkeys:
            while (proc := monkey.process_next()):
                to_monkey, stress = proc
                monkeys[to_monkey].items.append(stress)

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
        return (int(to_monkey), stress % stress_modulo)

    return condition
        

if __name__ == "__main__":
    main()
