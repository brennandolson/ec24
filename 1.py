import sys

def cost(l):
    return l.count("B") + 3 * l.count("C")

def cost2(l):
    vals = {"A": 0, "x": 0, "B": 1, "C": 3, "D": 5}
    ans = sum(vals[c] for c in l)
    for i in range(0, len(l), 2): 
        if l[i] != "x" and l[i+1] != "x":
            ans += 1
    return ans
        

ans = 0
for line in sys.stdin:
    line = line.strip()
    if not line: continue
    # ans += cost(line)
    ans += cost2(line)
print (ans)
