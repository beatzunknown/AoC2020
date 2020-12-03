import math

with open('03.txt', 'r') as f:
	data = [l.rstrip() for l in f.readlines()]

height = len(data)
width = len(data[0])

hit_tree = lambda x, y: data[y][x % width] == '#'

def run_slope(x_delta, y_delta):
	global height
	collisions = x = y = 0
	while y < height:
		collisions += hit_tree(x, y)
		x += x_delta
		y += y_delta
	return collisions

slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
part_2 = math.prod([run_slope(x, y) for x, y in slopes])

print("Part 1:", run_slope(3, 1))
print("Part 2:", part_2)