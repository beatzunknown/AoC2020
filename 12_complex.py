# After hearing how others solved Day 12 with complex
# numbers, I gave it a try

with open('12.txt', 'r') as f:
    data = [(l[0], int(l.rstrip()[1:])) for l in f.readlines()]

DIR = {'N': 1, 'S': -1, 'E': 1j, 'W': -1j}
ROT = {'R': 1, 'L': -1}

compass = 1j
pos = 0
for action, val in data:
    if action in DIR: pos += DIR[action]*val
    elif action in ROT: compass *= 1j ** (ROT[action]*(val//90))
    else: pos += compass*val
part_1 = int(abs(pos.real) + abs(pos.imag))

pos = 0
wp = 1 + 10j
for action, val in data:
    if action in DIR: wp += DIR[action]*val
    elif action in ROT: wp *= 1j ** (ROT[action]*(val//90))
    else: pos += wp*val
part_2 = int(abs(pos.real) + abs(pos.imag))

print("Part 1:", part_1)
print("Part 2:", part_2)