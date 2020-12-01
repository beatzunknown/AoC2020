with open('01.txt', 'r') as f:
	data = set([int(l.rstrip()) for l in f.readlines()])

target = 2020

def findTwo(data, target):
	hTable = {}
	for x in data:
		diff = target-x
		if diff in hTable:
			print(diff,x)
			return (diff, x)
		hTable[x] = diff
	return (-1, -1)

a, b = findTwo(data, target)
part_1 = a * b

for x in data:
	y, z = findTwo(data - set([x]), target-x)
	if y > 0 and x > 0:
		part_2 = x*y*z
		break

print("Part 1:", part_1)
print("Part 2:", part_2)
