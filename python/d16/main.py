import re
import itertools

def main():
    d16('input_test')
    d16('input_1')

re_line = re.compile(r"Valve (\w{2}) has flow rate=(\d+); tunnels? leads? to valves? (.+)")

class Valve:
    def __init__(self, args):
        name, rate, links = args
        self.name = name
        self.rate = rate
        self.links = links
        self.linked: dict[str: (int, Valve)] = dict()

    def __repr__(self) -> str:
        return f'Valve {self.name}, flow rate {self.rate}, linked to {[(k, v[0]) for k, v in self.linked.items()]}'

def d16(file):
    with open(file, "r", encoding="utf-8") as f:
        valve_args = [(groups[0], int(groups[1]), groups[2].split(", "))
                  for line in f
                  if (groups := re_line.match(line).groups())]

    valves = {valve[0]: Valve(valve) for valve in valve_args}
    openable = [v for v in valves if valves[v].rate > 0]
    link_valves(valves)
    rate, path, t = best_sub_rate(valves["AA"], openable, 30)
    print(f'{rate} {path} {t}')
    rate, path, path2, t, t2 = best_dual_sub_rate(valves, openable, 26)
    print(f'{rate} {path} {path2} {t} {t2}')

def link_valves(valves: dict[str, Valve]):
    for v_name, v in valves.items():
        dist = 1
        next = [(dist, l) for l in v.links]
        while len(next):
            dist += 1
            curr = next
            next = []
            for c_dist, c_valve_name in curr:
                if c_valve_name == v_name:
                    continue
                if c_valve_name in v.linked:
                    continue
                
                c_valve = valves[c_valve_name]
                v.linked[c_valve_name] = (c_dist, c_valve)
                next.extend([(dist, l) for l in c_valve.links])

def best_sub_rate(valve: Valve, openable, time):
    if len(openable) <= 0 or time <= 0:
        return 0, [], time
    
    if len(openable) == 1:
        open_valve_name = openable[0]
        dist, open_valve = valve.linked[open_valve_name]
        if dist < time:
            return (time - dist - 1) * open_valve.rate, [open_valve_name], time - dist - 1
        else:
            return 0, [], time

    best = 0, [], 0
    for open in openable:
        v_dist, next_v = valve.linked[open]
        r, p, _ = best_sub_rate(valve, [open], time)
        if p is []:
            continue
        sub_r, sub_p, t_left = best_sub_rate(next_v, list(filter(lambda x : x != open, openable)), time - 1 - v_dist)
        best_r, _, _ = best
        if best_r < r + sub_r:
            best = r + sub_r, p + sub_p, t_left

    return best

def best_dual_sub_rate(valves, openable, time):
    best = 0, None, None
    for i in range(1, (len(openable) + 1) // 2):
        iter = 0
        for openable_1 in itertools.combinations(openable, i):
            iter += 1
            openable_2 = list(filter(lambda x : x not in openable_1, openable))
            rate, path, t = best_sub_rate(valves["AA"], openable_1, time)
            rate2, path2, t2 = best_sub_rate(valves["AA"], openable_2, time)
            if rate + rate2 > best[0]:
                best = rate + rate2, path, path2, t, t2
    return best

if __name__ == "__main__":
    main()
