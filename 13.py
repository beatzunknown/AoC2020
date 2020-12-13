import math

with open('13.txt', 'r') as f:
    time = int(f.readline().rstrip())
    buses = f.readline().rstrip().split(',')
    ids = {int(e):-t for t,e in enumerate(buses) if e != 'x'}

d_times = {bus: ((time-1)//bus + 1)*bus for bus in ids}
part_1 = (min(d_times.values())-time) * min(d_times, key=d_times.get)

# extended euclidean algo / gcd
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b%a,a)
    return (g, x - (b//a) * y, y)

# modular inverse, a*x (mod m) = 1 (mod m), solve for x
def modinv(a, m):
    g, x, y = egcd(a, m)
    return x % m

# timestamp =(congruent) -bus_pos (mod bus_id)
# since (timestamp + bus_pos) % bus_id = 0
# ie x =(congruent) a_k (mod n_k)
# for coprime n_1 - n_k positive integers
# and a_1 - a_k integers making a system of simultaneous
# congruences.
# solved by Chinese Remainder Theorem
def chinese_remainder_theorem(rems, mods):
    sol = 0
    prod = math.prod(mods)

    for rem, mod in zip(rems, mods):
        p = prod // mod
        sol += rem * modinv(p, mod) * p

    return sol % prod

part_2 = chinese_remainder_theorem(ids.values(), ids.keys())

print("Part 1:", part_1)
print("Part 2:", part_2)