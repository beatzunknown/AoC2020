# diagonal movement is 1 unit in x-dir and 1 unit in y-dir
# vertical/horizontal movement is 2 units in y/x direction

DIR = {'e': (2, 0), 'w': (-2, 0), 'se': (1, -1),
       'sw': (-1, -1), 'nw': (-1, 1), 'ne': (1, 1)}

with open('24.txt', 'r') as f:
    steps = [l.rstrip() for l in f.readlines()]

# (x, y): False/True (true if flipped, ie black tile)
flipped = {}
for step in steps:
	x = y = 0
	while step:
		move = next(k for k in DIR if step.startswith(k))
		dx, dy = DIR[move]
		x, y = x + dx, y + dy
		step = step[len(move):]
	flipped[(x, y)] = not flipped.get((x, y), False)

part_1 = sum(flipped.values())

adj_black = lambda x,y,d: sum(d.get((x+dx, y+dy), False) for dx,dy in DIR.values())

x_vals = [v[0] for v in flipped]
y_vals = [v[1] for v in flipped]
x_lo, x_hi = min(x_vals)-1, max(x_vals)+3
y_lo, y_hi = min(y_vals)-1, max(y_vals)+2
for _ in range(100):
	new_flipped = {}
	for x in range(x_lo, x_hi):
		for y in range(y_lo, y_hi):
			is_black = flipped.get((x, y), False)
			num_black = adj_black(x, y, flipped)
			if is_black and (num_black == 0 or num_black > 2):
				new_flipped[(x, y)] = False
			elif not is_black and num_black == 2:
				new_flipped[(x, y)] = True
			else:
				new_flipped[(x, y)] = is_black
	flipped = new_flipped
	x_lo, x_hi = x_lo-1, x_hi+2
	y_lo, y_hi = y_lo-1, y_hi+1

part_2 = sum(flipped.values())

print("Part 1:", part_1)
print("Part 2:", part_2)