# creds to AoC reddit for idea of dict to map
# a cup with the next cup

inp = [int(x) for x in '315679824']

def run(cups, num_cups, iters):
	cups = cups + [x for x in range(len(cups)+1, num_cups+1)]
	next_cup = {}
	for i in range(num_cups-1):
		next_cup[cups[i]] = cups[i+1]
	next_cup[cups[num_cups-1]] = cups[0]
	curr = cups[0]
	for _ in range(iters):
		cup1 = next_cup[curr]
		cup2 = next_cup[cup1]
		cup3 = next_cup[cup2]
		next_cup[curr] = next_cup[cup3]
		dest = curr - 1
		while dest in [cup1, cup2, cup3] or not dest:
			if not dest:
				dest = num_cups
			else:
				dest -= 1
		next_cup[dest], next_cup[cup3] = cup1, next_cup[dest]
		curr = next_cup[curr]
	return next_cup

next_cup = run([x for x in inp], 9, 100)
curr = next_cup[1]
part_1 = ''
while curr != 1:
	part_1 += str(curr)
	curr = next_cup[curr]

next_cup = run([x for x in inp], 1000000, 10000000)
a = next_cup[1]
b = next_cup[a]
part_2 = a*b

print("Part 1:", part_1)
print("Part 2:", part_2)