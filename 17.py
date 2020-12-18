# This solution has been generalised for n

import itertools

DIR = {}
cubes = {}

def get_input(n):
    cubes = {}
    bounds = [[0,1]]*n
    with open('17.txt', 'r') as f:
        data = f.readlines()
        bounds[0] = [0, len(data)]
        bounds[1] = [0, len(data[0].rstrip())]
        filler = tuple([0]*(n-2))
        for y in range(len(data)):
            for x in range(len(data[y].rstrip())):
                cubes[(x,y)+filler] = data[y][x]
    return (cubes, bounds)

add = lambda x, y: x + y

def neighbours(coord):
    global DIR
    n = len(coord)
    if n not in DIR:
        DIR[n] = list(set(itertools.product((-1,0,1),repeat=n)).difference({tuple([0]*n)}))
    return [tuple(map(add, coord, d)) for d in DIR[n]]

def active_neighbours(cubes, coord):
    return sum(cubes.get(n, '.')=='#' for n in neighbours(coord))

def expand(cubes, bounds, n, coord):
    if n >= 0:
        for x in range(*bounds[n]):
            new = [c for c in coord] + [x]
            expand(cubes, bounds, n-1, new)
    else:
        c = tuple(coord[::-1])
        if c not in cubes:
            cubes[c] = '.'

def simulate(n):
    cubes, bounds = get_input(n)
    for i in range(6):
        for i in range(n):
            bounds[i] = [bounds[i][0]-1, bounds[i][1]+1]
        old_cubes = cubes
        cubes = {}
        expand(old_cubes, bounds, n-1, [])
        for coord in old_cubes:
            if old_cubes[coord]=='#' and (2 <= active_neighbours(old_cubes, coord) <= 3):
                cubes[coord] = '#'
            elif old_cubes[coord]=='.' and active_neighbours(old_cubes, coord) == 3:
                cubes[coord] = '#'
            else:
                cubes[coord] = '.'
    return cubes

part_1 = sum(state == '#' for state in simulate(3).values())
part_2 = sum(state == '#' for state in simulate(4).values())

print("Part 1:", part_1)
print("Part 2:", part_2)