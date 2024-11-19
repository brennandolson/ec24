import sys
from collections import defaultdict as dd

children = dd(list)

for line in sys.stdin:
    line = line.strip()
    if not line: continue
    old, newlist = line.split(":")
    children[old] = newlist.split(",")

def count(start):
    curr = {start: 1}
    for day in range(20):
        nxt = dd(int)
        for old, cnt in curr.items():
            for new in children[old]:
                nxt[new] += cnt
        curr = nxt
    return sum(x[1] for x in curr.items())

vals = [count(c) for c in children.keys()]
print (max(vals) - min(vals))
