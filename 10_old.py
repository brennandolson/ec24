import sys
from collections import defaultdict as dd

lines = []
for line in sys.stdin:
    line = line.strip()
    if not line: continue
    lines.append(line)

def word(grid):
    h = len(grid)
    w = len(grid[0])
    assert h == 8
    assert w == 8
    
    cols = dd(set)
    rows = dd(set)
    
    for i in range(h):
        for j in range(w):
            if grid[i][j] in ".*": continue
            rows[i].add(grid[i][j])
            cols[j].add(grid[i][j])
    ans = [] 
    for i in range(h):
        for j in range(w):
            if grid[i][j] != ".": continue
            choices = rows[i].intersection(cols[j])
            assert len(choices) == 1
            ans.append(choices.pop())
    print ("".join(ans))
    return "".join(ans)

def score(word):
    ans = 0
    for i, c in enumerate(word):
        ans += (i + 1) * (1 + ord(c) - ord("A"))
    return ans

def gscore(grid):
    return score(word(grid))

vblocks = len(lines) // 8
hblocks = len(lines[0]) // 9 + 1

ans = 0
count = 0
for i in range(vblocks):
    for j in range(hblocks):
        si = i * 8
        sj = j * 9
        grid = []
        for x in range(si, si + 8):
            grid.append(lines[x][sj:sj+8])
        count += 1
        ans += gscore(grid)

print (ans)
print (count)
