from console import Console

with open('08.txt', 'r') as f:
	instructions = [l.rstrip().split() for l in f.readlines()]

console = Console(instructions)
part_1, exit_code = console.execute()

part_2 = 0
for i in range(len(instructions)):
	new_instructions = [[op, arg] for op, arg in instructions]
	if instructions[i][0] == 'nop':
		new_instructions[i][0] = 'jmp'
	elif instructions[i][0] == 'jmp':
		new_instructions[i][0] = 'nop'
	console = Console(new_instructions)
	part_2, exit_code = console.execute()
	if exit_code == 0:
		break

print("Part 1:", part_1)
print("Part 2:", part_2)