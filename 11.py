DIR = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

with open('11.txt', 'r') as f:
    data = [[c for c in l.rstrip()] for l in f.readlines()]

def in_range(grid, x, y):
    return (0 <= x < len(grid[0])) and (0 <= y < len(grid))

def do_nothing(grid, x, y, adj):
    return grid[y][x]

def handle_empty(grid, x, y, adj):
    if adj:
        pos = [(x+dx, y+dy) for dx, dy in DIR if in_range(grid, x+dx, y+dy)]
        pos = [grid[y][x] == '#' for x, y in pos]
        return 'L' if any(pos) else '#'
    else:
        for dx, dy in DIR:
            for i in range(1, 1000):
                x2, y2 = x+(dx*i), y+(dy*i)
                if not in_range(grid, x2, y2): break
                if grid[y2][x2] == 'L': break
                if grid[y2][x2] == '#': return 'L'
    return '#'

def handle_occupied(grid, x, y, adj):
    if adj:
        pos = [(x+dx, y+dy) for dx, dy in DIR if in_range(grid, x+dx, y+dy)]
        pos = [grid[y][x] == '#' for x, y in pos]
        return 'L' if sum(pos) >= 4 else '#'
    else:
        pos = []
        for dx, dy in DIR:
            for i in range(1, 1000):
                x2, y2 = x+(dx*i), y+(dy*i)
                if not in_range(grid, x2, y2): break
                if grid[y2][x2] == 'L': break
                if grid[y2][x2] == '#':
                    pos.append(True)
                    break
        return 'L' if sum(pos) >= 5 else '#'


def grids_same(a, b):
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] != b[i][j]:
                return False
    return True

change_ops = {
    '.': do_nothing,
    'L': handle_empty,
    '#': handle_occupied
}

def run_simulation(data, adj):
    grid = [[elem for elem in row] for row in data]
    old_grid = [[0 for elem in row] for row in grid]
    i=0
    while not grids_same(grid, old_grid):
        old_grid = [[elem for elem in row] for row in grid]
        for y in range(len(old_grid)):
            for x in range(len(old_grid[0])):
                grid[y][x] = change_ops[old_grid[y][x]](old_grid, x, y, adj)
    return sum([sum([elem == '#' for elem in row]) for row in grid])

print("Part 1:", run_simulation(data, adj=True))
print("Part 2:", run_simulation(data, adj=False))