groups = []
groups_or = []
groups_and = []
first = True

with open('06.txt', 'r') as f:
	group = []
	group_or = set()
	group_and = set()
	for line in f.readlines():
		if (stripped := line.rstrip()):
			group.append(stripped)
			group_or = group_or | set(stripped)
			if first:
				group_and = set(stripped)
				first = False
			else:
				group_and = group_and & set(stripped)
		else:
			groups.append(group)
			groups_or.append(group_or)
			group_or = set()
			groups_and.append(group_and)
			group_and = set()
			group = []
			first = True

part_1 = sum([len(g) for g in groups_or])
part_2 = sum([len(g) for g in groups_and])

print("Part 1:", part_1)
print("Part 2:", part_2)
