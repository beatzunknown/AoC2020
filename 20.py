import math

cw_rot = lambda l: list(map(list, zip(*reversed(l))))
flip = lambda l: [l[i][::-1] for i in range(len(l))]
# match vertical edge
vert_match = lambda a, b: all(a[i][-1] == b[i][0] for i in range(len(a)))
# match horizontal edge
hori_match = lambda a, b: all(a[-1][i] == b[0][i] for i in range(len(a)))

def transforms(tile):
    t = [tile]
    for i in range(3):
        t.append(cw_rot(t[-1]))
    t += [flip(x) for x in t]
    return t

data = {}

with open('20.txt', 'r') as f:
    for tile in f.read().split('\n\n'):
        if not tile:
            break
        tile = tile.splitlines()
        data[int(tile[0][5:-1])] = [c for c in tile[1:]]

edges = {}
img_size = int(math.sqrt(len(data)))
tile_size = len(list(data.values())[0])

# part 1 logic:
# find 4 tiles with only 2 edges that join with other tiles
# since corners have 2 edges touching, edge tiles have 3 edges
# touching, and the rest have 4 edges touching

for k, v in data.items():
    row_f = v[0]
    row_l = v[-1]
    col_f = ''.join([v[i][0] for i in range(tile_size)])
    col_l = ''.join([v[i][-1] for i in range(tile_size)])
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

img = [[None]*img_size for i in range(img_size)]
tile_variants = {k: transforms(v) for k, v in data.items()}

# find top left tile
for p in tile_variants.pop(corners[0]):
    if any(vert_match(p, t) for var in tile_variants.values() for t in var):
        if any(hori_match(p, t) for var in tile_variants.values() for t in var):
            first_tile = p
            break

for r in range(img_size):
    for c in range(img_size):
        if r == c == 0:
            img[0][0] = first_tile
            continue
        match = None
        for tile, variants in tile_variants.items():
            for var in variants:
                if r > 0:
                    if not hori_match(img[r-1][c], var):
                        continue
                if c > 0:
                    if not vert_match(img[r][c-1], var):
                        continue
                match = var
                break
            if match:
                break
        if match:
            img[r][c] = match
            tile_variants.pop(tile)

# strip tile borders
built_img = []
for row in img:
    for i in range(1, tile_size-1):
        new_row = ''
        for tile in row:
            new_row += ''.join(tile[i][1:-1])
        built_img.append(new_row)

tile_size -= 2
img_size *= tile_size

m = [
"                  # ",
"#    ##    ##    ###",
" #  #  #  #  #  #   "]
m_h = len(m)
m_w = len(m[0])
# monster points, with top left (0,0) as anchor point
m_pts = [(r, c) for r in range(m_h) for c in range(m_w) if m[r][c] == '#']

def found_monster(img, r, c):
    coords = set()
    for dr, dc in m_pts:
        if img[r+dr][c+dc] != '#':
            return set()
        coords.add((r+dr, c+dc))
    return coords

def get_monster_hashes(img):
    monster_hashes = set()
    # rotate and flip the img if no monsters found
    for i in range(2):
        for j in range(4):
            if monster_hashes:
                return monster_hashes
            for r in range(img_size - m_h):
                for c in range(img_size - m_w):
                    monster_hashes |= found_monster(img, r, c)
            img = cw_rot(img)
        img = flip(img)
    return monster_hashes

total_hashes = sum(row.count('#') for row in built_img)
part_2 = total_hashes - len(get_monster_hashes(built_img))

print("Part 1:", part_1)
print("Part 2:", part_2)