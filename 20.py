import math

data = {}

with open('20.txt', 'r') as f:
    for tile in f.read().split('\n\n'):
        if not tile:
            break
        tile = tile.splitlines()
        data[int(tile[0][5:-1])] = tile[1:]

edges = {}
h = len(list(data.values())[0])
w = len(list(data.values())[0][0])

# part 1 logic:
# find 4 tiles with only 2 edges that join with other tiles
# since corners have 2 edges touching, edge tiles have 3 edges
# touching, and the rest have 4 edges touching

for k, v in data.items():
    row_f = v[0]
    row_l = v[-1]
    col_f = ''.join([v[i][0] for i in range(h)])
    col_l = ''.join([v[i][-1] for i in range(h)])
    # flipped edges are the "same", so min() ensures 1 identifier for each edge
    edges[k] = set([min([row_f, row_f[::-1]]), min([row_l, row_l[::-1]]),
                   min([col_f, col_f[::-1]]), min([col_l, col_l[::-1]])])

corners = []
boundary_matches = {}

for tile, tile_edges in edges.items():
    joining_edges = 0
    for edge in tile_edges:
        tiles_w_edge = sum([edge in edges[k] for k in edges if k!=tile])
        # only 1 other tile has this edge
        joining_edges += (tiles_w_edge == 1)
    if joining_edges == 2:
        corners.append(tile)
part_1 = math.prod(corners)

monster = [
"                  # ",
"#    ##    ##    ###",
" #  #  #  #  #  #   "]


part_2 = 0

print("Part 1:", part_1)
print("Part 2:", part_2)