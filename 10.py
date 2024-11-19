import sys
from collections import defaultdict as dd

lines = []
for line in sys.stdin:
    line = line.strip()
    if not line: continue
    lines.append(list(line))

def score(word):
    if "." in word: return 0
    ans = 0
    for i, c in enumerate(word):
        ans += (i + 1) * (1 + ord(c) - ord("A"))
    return ans

def resolve_dots(ci, cj):
    ''' input: top-left corner '''
    ''' output: num dots resolved '''
    cols = dd(set)
    rows = dd(set)
    changed = 0
    for di in range(8):
        for dj in range(8):
            i, j = ci + di, cj + dj
            if lines[i][j] in "*?": continue
            elif 2 <= min(di, dj) and max(di, dj) <= 5: continue
            cols[j].add(lines[i][j])
            rows[i].add(lines[i][j])
    for i in range(ci + 2, ci + 6):
        for j in range(cj + 2, cj + 6):
            if lines[i][j] != ".":
                continue
            choices = cols[j].intersection(rows[i])
            if len(choices) != 1: continue
            lines[i][j] = choices.pop()
            changed += 1
    return changed

def resolve_cols(ci, cj):
    ''' the final dot in a col '''
    changed = 0
    for j in range(cj + 2, cj + 6):
        letters = set()
        for i in [ci, ci+1, ci+6, ci+7]:
            letters.add(lines[i][j])
        if "?" in letters:
            continue
        if len(letters) != 4:
            continue
        
        grid_letters = set()
        doti, dotj = -1, -1
        for i in range(ci + 2, ci + 6):
            if lines[i][j] == ".": 
                doti = i
                dotj = j
                continue
            grid_letters.add(lines[i][j])
        if len(grid_letters) != 3: continue
        if doti == -1: continue
        if not grid_letters <= letters: continue
        c = (letters - grid_letters).pop()
        lines[doti][dotj] = c
        changed += 1
    return changed

def resolve_rows(ci, cj):
    changed = 0
    for i in range(ci + 2, ci + 6):
        letters = set()
        for j in [cj, cj+1, cj+6, cj+7]:
            letters.add(lines[i][j])
        if "?" in letters: continue
        if len(letters) != 4: continue

        grid_letters = set()
        doti, dotj = -1, -1
        for j in range(cj + 2, cj + 6):
            if lines[i][j] == ".":
                doti = i
                dotj = j
                continue
            grid_letters.add(lines[i][j])
        if len(grid_letters) != 3: continue
        if doti == -1: continue
        if not grid_letters <= letters: continue
        c = (letters - grid_letters).pop()
        lines[doti][dotj] = c
        changed += 1
    return changed

def resolve_q_cols(ci, cj):
    changed = 0
    for j in range(cj + 2, cj + 6):
        letters = set()
        qi, qj = -1, -1
        for i in [ci, ci+1, ci+6, ci+7]:
            if lines[i][j] == "?":
                qi, qj = i, j
                continue
            letters.add(lines[i][j])
        if len(letters) != 3:
            continue
        if qi == -1:
            continue
        
        grid_letters = set()
        for i in range(ci + 2, ci + 6):
            if lines[i][j] == ".": 
                continue
            grid_letters.add(lines[i][j])
        if len(grid_letters) != 4: continue
        if not letters <= grid_letters: continue
        c = (grid_letters - letters).pop()
        lines[qi][qj] = c
        changed += 1
    return changed

def resolve_q_rows(ci, cj):
    changed = 0
    for i in range(ci + 2, ci + 6):
        letters = set()
        qi, qj = -1, -1
        for j in [cj, cj+1, cj+6, cj+7]:
            if lines[i][j] == "?":
                qi, qj = i, j
                continue
            letters.add(lines[i][j])
        if len(letters) != 3: continue
        if qi == -1: continue

        grid_letters = set()
        for j in range(cj + 2, cj + 6):
            if lines[i][j] == ".":
                continue
            grid_letters.add(lines[i][j])
        if len(grid_letters) != 4: continue
        if not letters <= grid_letters: continue
        c = (grid_letters - letters).pop()
        lines[qi][qj] = c
        changed += 1
    return changed




H = (len(lines) - 2) // 6
W = (len(lines[0]) - 2) // 6

done = False
while not done:
    changes = 0
    for i in range(H):
        for j in range(W):
            changes += (resolve_dots(i * 6, j * 6))
            changes += (resolve_cols(i * 6, j * 6))
            changes += (resolve_rows(i * 6, j * 6))
            changes += (resolve_q_cols(i * 6, j * 6))
            changes += (resolve_q_rows(i * 6, j * 6))
    print (changes)
    done = (changes == 0)
    
def get_word(ci, cj):
    word = []
    for i in range(ci + 2, ci + 6):
        for j in range(cj + 2, cj + 6):
            word.append(lines[i][j])
    return "".join(word)

ans = 0
for i in range(H):
    for j in range(W):
        s = score(get_word(i*6,j*6))
        ans += s
        print ("score:", s)

print ("ans:", ans)
for line in lines:
    print ("".join(line))
