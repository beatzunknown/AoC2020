with open('12.txt', 'r') as f:
    data = [(l[0], int(l.rstrip()[1:])) for l in f.readlines()]

DIR = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}
ROT = {'R': 1, 'L': -1}
FACES = ['E', 'S', 'W', 'N']

compass = 0
x = y = 0
for action, val in data:
    if action in DIR:
        dx, dy = DIR[action]
        x, y = x + dx*val, y + dy*val
    elif action in ROT:
        compass = (compass + (ROT[action]*(val//90))) % 4
    else:
        dx, dy = DIR[FACES[compass]]
        x, y = x + dx*val, y + dy*val

part_1 = abs(x) + abs(y)

compass = 0
x = y = 0
wx = 10
wy = 1
for action, val in data:
    if action in DIR:
        dx, dy = DIR[action]
        wx, wy = wx + dx*val, wy + dy*val
    elif action in ROT:
        val = (val//90) % 4
        if val == 2:
            wx, wy = -wx, -wy
        if (val == 1 and action == 'R') or (val == 3 and action == 'L'):
            wx, wy = wy, -wx
        elif (val == 1 and action == 'L') or (val == 3 and action == 'R'):
            wx, wy = -wy, wx
    else:
        x, y = x + wx*val, y + wy*val

part_2 = abs(x) + abs(y)

print("Part 1:", part_1)
print("Part 2:", part_2)