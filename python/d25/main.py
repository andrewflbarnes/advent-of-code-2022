def main():
    d24('input_test')
    d24('input_1')


fuel_digits = {
    '2': 2,
    '1': 1,
    '0': 0,
    '-': -1,
    '=': -2,
}


def d24(file):
    with open(file, "r", encoding="utf-8") as f:
        fuel = sum([sum(fuel_digits[c] * (5 ** i)
                        for i, c in enumerate(l.strip()[::-1]))
                    for l in f])

    print(convert(fuel))


def convert(num):
    pos_vals = [1]
    while range_lim(pos_vals[-1]) < abs(num):
        pos_val = positional_val(len(pos_vals))
        pos_vals.append(pos_val)

    calc = 0
    snafu = ""
    pos_vals = pos_vals[::-1]
    for p, val in enumerate(pos_vals):
        rlim_next = range_lim(pos_vals[p + 1] if p + 1 < len(pos_vals) else 0)
        left = num - calc
        i = 0
        while abs(left) > rlim_next:
            if not -2 <= i <= 2:
                raise ValueError(f"i incremeneted too far! {i}")
            if left < 0:
                calc -= val
                i -= 1
            else:
                calc += val
                i += 1
            left = num - calc
        snafu += (str(i) if i >= 0 else "-" if i == -1 else "=")

    return snafu


def range_lim(v):
    return (2 * v) + (2 * v) // 4


def positional_val(pos):
    return 5 ** pos


if __name__ == "__main__":
    main()
