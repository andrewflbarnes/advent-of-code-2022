import re

def main():
    d21('input_test')
    d21('input_1')

def d21(file):
    with open(file, "r", encoding="utf-8") as f:
        raw = [l.strip().split(": ") for l in f]

    nums = {l[0]: int(l[1]) for l in raw if l[1].find(" ") < 0}
    find = {l[0]: l[1].split(" ") for l in raw if l[1].find(" ") > 0}
    part_1(nums.copy(), find.copy())

def part_1(nums, find):
    while 'root' not in nums:
        for mn in list(find.keys()):
            process_op(nums, find, mn)

    print(nums['root'])

def process_op(nums, find, mn):
    m1, op, m2 = find[mn]
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
                raise ValueError(f'unrecognised symbol x{op}x')
        del find[mn]

if __name__ == "__main__":
    main()
