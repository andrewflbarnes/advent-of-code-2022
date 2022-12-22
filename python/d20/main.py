def main():
    d20('input_test')
    d20('input_1')

deckey = 811589153

class MoveNum:
    def __init__(self, num: int):
        self.num = num
        self.nxt = None
    
    def set_nxt(self, nxt):
        self.nxt = nxt

    def __repr__(self) -> str:
        return f'{self.num}'

    def __str__(self) -> str:
        return f'{self.num}'

def d20(file):
    with open(file, "r", encoding="utf-8") as f:
        nums = [MoveNum(int(l.strip())) for l in f]

    for i in range(0, len(nums) - 1):
        nums[i].set_nxt(nums[i + 1])

    mix(nums.copy(), 1, 1)
    mix(nums.copy(), 10, deckey)


def mix(nums, iters, key):
    for num in nums:
        num.num = num.num * key
    size = len(nums)
    start = MoveNum(0) # dummy start node
    start.set_nxt(nums[0])
    for i in range(iters):
        node = start
        while (node := node.nxt):
            i = nums.index(node)
            nums.remove(node)
            move = (node.num + i) % (size - 1)
            if move == 0:
                move = size - 1
            elif move == size - 1:
                move = 0
            nums.insert(move, node)

    zero = 0
    for i, node in enumerate(nums):
        if node.num == 0:
            zero = i
            break
    print(sum(nums[(i + zero) % size].num for i in range(1000, 3001, 1000)))

if __name__ == "__main__":
    main()
