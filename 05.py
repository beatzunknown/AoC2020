with open('05.txt', 'r') as f:
    data = [l.rstrip() for l in f.readlines()]

lower = lambda a,b: (a, (a+b)//2)
upper = lambda a,b: ((a+b)//2, b)

ops = {'F': lower,
       'B': upper,
       'L': lower,
       'R': upper}

def run_binary(lo, hi, partition):
    for m in partition[:7]:
        lo, hi = ops[m](lo, hi)
    return hi

def calc_pos(partition):
    row = run_binary(0, 127, partition[:7])
    col = run_binary(0, 7, partition[7:])
    return (row, col)

rc_data = [calc_pos(p) for p in data]
ids = [r*8 + c for r, c in rc_data]

part_1 = max(ids)
part_2 = 0

for r in range(1,127):
    for c in range(8):
        if (r, c) not in rc_data:
            if (ID := r*8+c)+1 in ids and ID-1 in ids:
                part_2 = ID

print("Part 1:", part_1)
print("Part 2:", part_2)