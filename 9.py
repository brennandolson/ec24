import sys

coins = [1,3,5,10,15,16,20,24,25,30,37,38,49,50,74,75,100,101]

targets = []
for line in sys.stdin:
    line = line.strip()
    if not line: continue
    targets.append(int(line))

M = max(targets) + 1
dp = [10**20] * M
dp[0] = 0
for i in range(M):
    for coin in coins:
        if i + coin >= M: continue
        dp[i+coin] = min(dp[i+coin], dp[i] + 1)

def best(n):
    lo = n // 2 - 55
    while lo <= 0:
        lo += 1
    hi = n - lo
    while abs(hi - lo) > 100:
        lo += 1
        hi -= 1

    ans = 10**20
    while lo <= hi:
        ans = min(ans, dp[lo] + dp[hi])
        lo += 1
        hi -= 1
    return ans

print (sum(best(i) for i in targets))
