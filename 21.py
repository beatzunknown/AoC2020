foods = []
allergen_map = {}

with open('21.txt', 'r') as f:
    lines = f.readlines()
    for i in range(len(lines)):
        l = lines[i].rstrip().split(' (contains ')
        ingredients = l[0].split()
        allergens = l[1][:-1].split(', ')
        for a in allergens:
            if a not in allergen_map:
                allergen_map[a] = set(ingredients)
            else:
                allergen_map[a] &= set(ingredients)
        foods.append((ingredients, allergens))

allergen_ingreds = set.union(*allergen_map.values())
part_1 = sum(sum(x not in allergen_ingreds for x in food) for food, a in foods)

occurrences = {}
for ingreds in allergen_map.values():
    for ingred in ingreds:
        if ingred not in occurrences:
            occurrences[ingred] = 0
        occurrences[ingred] += 1

def arrange(values):
    return sorted(values, key=lambda x: occurrences[x])

allergen_map = sorted([[k, arrange(v)] for k, v in allergen_map.items()], key=lambda x: len(x[1]))

final_mapping = {}
for i in range(len(allergen_map)):
    allergen, ingred = allergen_map[i]
    ingred = ingred.pop(0)
    final_mapping[allergen] = ingred
    for i in range(i, len(allergen_map)):
        if ingred in allergen_map[i][1]:
            allergen_map[i][1].remove(ingred)

part_2 = ','.join(final_mapping[a] for a in sorted(final_mapping))

print("Part 1:", part_1)
print("Part 2:", part_2)