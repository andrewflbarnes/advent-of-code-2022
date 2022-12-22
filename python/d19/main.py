import re

re_bpnt = re.compile(r"Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.")

def main():
    d19('input_test')
    d19('input_1')

def d19(file):
    with open(file, "r", encoding="utf-8") as f:
        input = [tuple(int(i) for i in re_bpnt.match(l.strip()).groups()) for l in f]

    bpnts = dict()
    for b in input:
        bpnts[int(b[0])] = ([b[1], 0, 0], [b[2], 0, 0], [b[3], b[4], 0], [b[5], 0, b[6]])

    mins = 24
    print(sum(quality_level(bpnts, i, mins)  for i in bpnts))

def quality_level(bpnts, id, mins):
    final_mat, final_rate = best_bpnt_sub_mine(bpnts[id], mins)
    # print(f'{final_mat} <= {final_rate}')
    return id * final_mat[3]

def best_bpnt_sub_mine(bpnt, mins):
    mat = [0, 0, 0, 0]
    rate = [1, 0, 0, 0]

    best = best_sub_mine(bpnt, mat, rate.copy(), mins, [bpnt[0], 0])
    sub_mine = best_sub_mine(bpnt, mat, rate.copy(), mins, [bpnt[1], 1])
    if best[0][3] < sub_mine[0][3]:
        best = sub_mine

    return best

def best_sub_mine(bpnt, mat, rate, mins, next_robot):
    if mins == 1:
        return inc_mat(mat, rate), rate

    req, robot = next_robot
    req_ore, req_clay, req_obs = req
    build = req_ore <= mat[0] and req_clay <= mat[1] and  req_obs <= mat[2]
    mat = inc_mat(mat, rate)
    mins -= 1

    if not build:
        return best_sub_mine(bpnt, mat, rate, mins, next_robot)

    rate[robot] += 1
    mat[0] -= req_ore
    mat[1] -= req_clay
    mat[2] -= req_obs

    best = None

    if rate[0] < max(r[0] for r in bpnt):
        best = best_sub_mine(bpnt, mat, rate.copy(), mins, [bpnt[0], 0])

    if rate[1] < max(r[1] for r in bpnt):
        sub_mine = best_sub_mine(bpnt, mat, rate.copy(), mins, [bpnt[1], 1])
        if best is None or best[0][3] < sub_mine[0][3]:
            best = sub_mine
    if rate[1] > 0 and rate[2] < max(r[2] for r in bpnt):
        sub_mine = best_sub_mine(bpnt, mat, rate.copy(), mins, [bpnt[2], 2])
        if best is None or best[0][3] < sub_mine[0][3]:
            best = sub_mine
    if rate[2] > 0:
        sub_mine = best_sub_mine(bpnt, mat, rate.copy(), mins, [bpnt[3], 3])
        if best is None or best[0][3] < sub_mine[0][3]:
            best = sub_mine
    return best
        

def inc_mat(mat, rate):
    return [mat[0] + rate[0], mat[1] + rate[1], mat[2] + rate[2], mat[3] + rate[3]]
    # return list(map(lambda x : x[0] + x[1], zip(ore, rate)))


if __name__ == "__main__":
    main()
