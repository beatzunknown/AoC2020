import re
import itertools

with open('14.txt', 'r') as f:
    data = [l.rstrip() for l in f.readlines()]

pattern = re.compile(r'mem\[(\d+)\] = (\d+)')

mask = ''
mem1 = {}
for l in data:
    if l[:4] == 'mask': mask = l.split()[-1]
    else:
        addr, val = pattern.search(l).groups()
        val = bin(int(val))[2:]
        val = [c for c in '0'*(36-len(val))+val]
        for i in range(len(val)):
            if mask[i] != 'X': val[i] = mask[i]
        mem[addr] = ''.join(val)
part_1 = sum(int(val, 2) for val in mem.values())

mask = ''
mem2 = {}
for l in data:
    if l[:4] == 'mask': mask = l.split()[-1]
    else:
        addr, val = pattern.search(l).groups()
        addr = bin(int(addr))[2:]
        addr = [c for c in '0'*(36-len(addr))+addr]
        for i in range(len(addr)):
            if mask[i] != 'X': addr[i] = str(int(mask[i]) | int(addr[i]))
            else: addr[i] = 'X'
        x_locs = [i for i, e in enumerate(addr) if e == 'X']
        perms = [''.join(seq) for seq in itertools.product('01', repeat=len(x_locs))]
        for perm in perms:
            new_addr = [c for c in addr]
            for i, e in enumerate(x_locs):
                new_addr[e] = perm[i]
            mem[''.join(new_addr)] = int(val)

part_2 = sum(mem.values())

print("Part 1:", part_1)
print("Part 2:", part_2)