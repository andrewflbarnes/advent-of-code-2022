def main():
    d15('input_test', 10, 20)
    d15('input_1', 2_000_000, 4_000_000)

def d15(file, row, search):
    with open(file, "r", encoding="utf-8") as f:
        lines = [l for l in f]

    parsed = [[int(p) for p in l.strip().replace("Sensor at ", "").replace(", ", ",").replace(": closest beacon is at ",",").replace("x=", "").replace("y=","").split(",")] for l in lines]
    coords = [((p[0], p[1]), (p[2], p[3]), dist((p[0], p[1]), (p[2], p[3]))) for p in parsed]
    sensors = set([c[0] for c in coords])
    beacons = set([c[1] for c in coords])
    part_1(sensors, beacons, coords, row)
    part_2(sensors, beacons, coords, search)

def part_1(sensors, beacons, coords, row):
    max_m_dist = max([c[2] for c in coords])
    min_x = min(min([p[0] for p in sensors]), min(p[0] for p in beacons))
    max_x = max(max([p[0] for p in sensors]), max(p[0] for p in beacons))

    not_present = 0
    for x in range(min_x - max_m_dist, max_x + max_m_dist):
        p = (x, row)

        if p in beacons:
            continue

        for sensor, _, m_dist in coords:
            if dist(sensor, p) <= m_dist:
                not_present += 1
                break

    print(not_present)

def part_2(sensors, beacons, coords, search):

    for coord in coords:
        if (p := check_sensor_boundary(coord, coords, search)):
            x, y = p
            print(f'Found missing beacon at {p} with tuning freq {4000000 * x + y}')
            break

def check_sensor_boundary(coord, coords, search):
    sensor, _, m_dist = coord
    s_x, s_y = sensor

    boundary = set()
    boundary_tests = set()
    x_inc = 1
    y_inc = -1

    next = (s_x - m_dist, s_y)
    while not next in boundary:
        boundary.add(next)
        update_boundary_test(boundary_tests, next, x_inc, y_inc)
        x, y = next
        if x == s_x:
            y_inc = 1 if y < s_y else -1
            update_boundary_test(boundary_tests, next, x_inc, y_inc)
        elif y == s_y:
            x_inc = 1 if x < s_x else -1
            update_boundary_test(boundary_tests, next, x_inc, y_inc)

        next = (x + x_inc, y + y_inc)
    update_boundary_test(boundary_tests, next, x_inc, y_inc)
    #frame(boundary, boundary_tests, set([]))

    #print(f'testing boundary for {sensor} with m_dist {m_dist}')
    for p in boundary_tests:
        x, y = p
        if x < 0 or x > search or y < 0 or y > search:
            continue
        for sensor, _, m_dist in coords:
            if dist(sensor, p) <= m_dist:
                break
        else:
            return p

    return None

def update_boundary_test(all, p, x_inc, y_inc):
    x, y = p
    all.add((x, y - x_inc))
    all.add((x + y_inc, y))
    all.add((x + y_inc, y - x_inc))

def dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def frame(sensors, beacons, empty):
    min_x = min(min((p[0] for p in sensors), default=0), min((p[0] for p in beacons), default=0))
    max_x = max(max((p[0] for p in sensors), default=0), max((p[0] for p in beacons), default=0))
    min_y = min(min((p[1] for p in sensors), default=0), min((p[1] for p in beacons), default=0))
    max_y = max(max((p[1] for p in sensors), default=0), max((p[1] for p in beacons), default=0))
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            p = (x, y)
            if p in sensors:
                print("S", end="")
            elif p in beacons:
                print("B", end="")
            elif p in empty:
                print("#", end="")
            else:
                print(".", end="")
        print()

if __name__ == "__main__":
    main()
