same = lambda a,b: len(a) == len(b) and all(e in a for e in b)
copy = lambda a: [x for x in a]

with open('22.txt', 'r') as f:
    op1, op2 = [list(map(int, p.splitlines()[1:])) for p in f.read().split('\n\n')]

p1, p2 = copy(op1), copy(op2)
while p1 and p2:
    c1, c2 = p1.pop(0), p2.pop(0)
    if c1 > c2:
        p1 += [c1, c2]
    else:
        p2 += [c2, c1]

part_1 = sum([(i+1)*e for i,e in enumerate((p1+p2)[::-1])])

def recurse_play(p1, p2):
    m1, m2 = [], []
    while p1 and p2:
        if any((same(a, p1) or same(b, p2)) for a,b in zip(m1, m2)):
            return True
        m1.append(copy(p1))
        m2.append(copy(p2))
        c1, c2 = p1.pop(0), p2.pop(0)
        p1_wins = c1 > c2
        if len(p1) >= c1 and len(p2) >= c2:
            p1_wins = recurse_play(copy(p1[:c1]), copy(p2[:c2]))
        if p1_wins:
            p1 += [c1, c2]
        else:
            p2 += [c2, c1]
    return len(p1)>0

p1, p2 = copy(op1), copy(op2)
recurse_play(p1, p2)
part_2 = sum([(i+1)*e for i,e in enumerate((p1+p2)[::-1])])

print("Part 1:", part_1)
print("Part 2:", part_2)