import numbers

def main():
    d21('input_test', 'pppw', 'sjmn')
    d21('input_1', 'qmfl', 'qdpj')

def d21(file, p1, p2):
    with open(file, "r", encoding="utf-8") as f:
        raw = [l.strip().split(": ") for l in f]

    nums = {l[0]: int(l[1]) for l in raw if l[1].find(" ") < 0}
    find = {l[0]: l[1].split(" ") for l in raw if l[1].find(" ") > 0}
    part_1(nums.copy(), find.copy())
    part_2(nums.copy(), find.copy(), p1, p2)

def part_1(nums, find):
    while 'root' not in nums:
        for mn in list(find.keys()):
            process_op(nums, find, mn)

    print(nums['root'])

def part_2(nums, find, p1, p2):
    while 'humn' not in nums:
        for mn in list(find.keys()):
            process_op(nums, find, mn)

    test_nums = nums.copy()
    test_find = find.copy()
    test_nums['humn'] = 'humn'
    while p1 not in test_nums or p2 not in test_nums:
        for mn in list(test_find.keys()):

            m1, op, m2 = test_find[mn]
            if m1 in test_nums and m2 in test_nums:
                m1v = test_nums[m1]
                m2v = test_nums[m2]
                if isinstance(m1v, numbers.Number) and isinstance(m2v, numbers.Number):
                    process_op(test_nums, test_find, mn)
                else:
                    test_nums[mn] = f'({m1v} {op} {m2v})'
                    del test_find[mn]
    eqn = test_nums[p1]
    target = test_nums[p2]
    l_idx = 0
    r_idx = len(eqn) - 1
    while True:
        l_idx, r_idx, op, operand, flip = get_next_op(eqn, l_idx, r_idx)
        target = inverse_op(target, op, float(operand), flip)

        if eqn[l_idx:l_idx + 4] == 'humn':
            break

    print(target)

def get_next_op(eqn, l_idx, r_idx):
    if not eqn[l_idx] == "(" or not eqn[r_idx] == ")":
        raise ValueError(f"Missing expected parentheses at {l_idx}:{eqn[l_idx]} or {r_idx}:{eqn[r_idx]}")
    l_idx += 1
    r_idx -= 1
    if eqn[l_idx:l_idx + 4] == 'humn':
        _, op, operand = eqn[l_idx:r_idx + 1].split(" ")
        return l_idx, r_idx, op, operand, False
    elif eqn[l_idx] == "(":
        next_idx = seek(eqn, r_idx, ")", -1)
        parse = eqn[next_idx + 2:r_idx + 1].split(" ")
        return l_idx, next_idx, parse[0], parse[1], False
    elif eqn[r_idx] == ")":
        next_idx = seek(eqn, l_idx, "(", 1)
        parse = eqn[l_idx:next_idx - 1].split(" ")
        return next_idx, r_idx, parse[1], parse[0], True
    else:
        raise ValueError(f"Missing expected next parentheses at {l_idx}:{eqn[l_idx]} or {r_idx}:{eqn[r_idx]}")

def seek(eqn, idx, sym, dir):
    while True:
        idx += dir
        if eqn[idx] == sym:
            return idx

def process_op(nums, find, mn):
    calc = find[mn]
    m1, op, m2 = calc
    if m1 in nums and m2 in nums:
        match op:
            case "+":
                nums[mn] = nums[m1] + nums[m2]
            case "-":
                nums[mn] = nums[m1] - nums[m2]
            case "/":
                nums[mn] = nums[m1] / nums[m2]
            case "*":
                nums[mn] = nums[m1] * nums[m2]
            case _:
                raise ValueError(f'unrecognised symbol {op}')
        del find[mn]
    return calc

def inverse_op(target, op, operand, flip):
    match op:
        case "+":
            return target - operand
        case "-":
            return (target + operand) if not flip else (operand - target)
        case "/":
            return (target * operand) if not flip else (operand / target)
        case "*":
            return target / operand
        case _:
            raise ValueError(f'unrecognised symbol {op}')


if __name__ == "__main__":
    main()
