import sys

targets = []

for line in sys.stdin:
    line = line.strip()
    if not line: continue
    x, y = [int(x) for x in line.split(" ")]
    targets.append((x, y))

# Sort by (highest altitude, lowest score)
BAD = (-1, -1)

def find_min_power(x, y):
    ''' cannon at (0, 0) and fires at time 0. What is min_power to hit (x, y)
        returns -1 if not possible
    '''
    if x <= 0: return -1
    if y >= x: return -1
    if x == 1:
        return -1
    elif y >= x // 2:
        # Hitting on the flat part.
        return y
    else:
        # Hitting on downswing
        if (x + y) % 3 != 0:
            return -1
        power = (x + y) // 3
        f = power - y
        # Infeasible
        if f <= 0 or power <= 0:
            return -1
        return power


def get_vals(sx, sy, tx, ty, lt):
    value = sy + 1
    if ty - tx == sy - sx:
        ''' must hit at midpoint, but using min power '''
        hy = (sy + ty - lt) // 2
        power = (tx - lt) // 2
    else:
        # We know where collision must occur. The question is, what is the
        # lowest power which works (if any).
        hx = (tx - lt) // 2
        hy = ty - lt - hx
        dy = hy - sy # Relative to cannon. Can be negative.
        if hy < 0:
            return BAD
        power = find_min_power(hx, dy)
        if power <= 0: return BAD

    return hy, power * value

def best_vals(sx, sy, tx, ty):
    curr_best = BAD
    if ty - tx > sy - sx:
        return curr_best

    for lt in range(tx % 2, tx, 2):
        curr_best = max(curr_best, get_vals(sx, sy, tx, ty, lt), key = lambda x : (x[0], -x[1]))

    return curr_best

ans = 0
for tx, ty in targets:
    curr_best = BAD
    for sy in range(3):
        curr_best = max(curr_best, best_vals(0, sy, tx, ty), key = lambda x : (x[0], -x[1]))
    # print (curr_best)
    score = curr_best[-1]
    assert score > 0
    ans += score
print (ans)

