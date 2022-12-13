from functools import cmp_to_key

def main():
    d13('input_test')
    d13('input_1')

def d13(file):
    with open(file, "r", encoding="utf-8") as f:
        blocks = f.read().split("\n\n")

    correct = [i for i, block in enumerate(blocks, start=1)
               if (lines := block.strip().split("\n")) and compare(parse_line(lines[0]), parse_line(lines[1])) == -1]
    print(sum(correct))

    all = [[[2]],[[6]]]
    for block in blocks:
        all += [parse_line(line) for line in block.strip().split("\n")]

    allsort = sorted(all, key=cmp_to_key(compare))
    decode = [i for i, packet in enumerate(allsort, start=1) if packet == [[2]] or packet == [[6]]]
    print(decode[0] * decode[1])


def compare(left, right):
    l_len = len(left)
    r_len = len(right)
    for i in range(0, max(l_len, r_len)):
        if i >= l_len:
            return -1
        if i >= r_len:
            return 1

        l = left[i]
        r = right[i]
        if not isinstance(l, list) and not isinstance(r, list):
            if l < r:
                return -1
            if r < l:
                return 1
        else:
            l = l if isinstance(l, list) else [l]
            r = r if isinstance(r, list) else [r]
            if (sub_compare := compare(l, r)) is not None:
                return sub_compare


def parse_line(line):
    return parse([c for c in line])

def parse(chars):
    packet = []

    sym = ""
    while len(chars):
        c = chars.pop(0)
        match c:
            case "[":
                packet.append(parse(chars))
            case "]":
                if len(sym):
                    packet.append(int(sym))
                return packet
            case ",":
                if len(sym):
                    packet.append(int(sym))
                    sym = ""
            case digit:
                sym += c
    return packet[0]


if __name__ == "__main__":
    main()
