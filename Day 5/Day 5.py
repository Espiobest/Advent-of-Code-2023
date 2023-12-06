import math

with open('data.txt', 'r') as r:
    lines = r.read().split("\n\n")

seed_line = lines[0].split(": ")[1]

seeds = [*map(int, seed_line.split())]
new_seeds = []

maps = lines[1:]
min_location = math.inf

def follow_maps(seed, maps):
    for mp in maps:
        for line in mp.split("\n")[1:]:
            dest, src, num = [*map(int, line.split())]
            if src < seed < src + num:
                seed += dest - src
                break
    return seed

for seed in seeds:
    seed = follow_maps(seed, maps)
    min_location = min(min_location, seed)

print(min_location)

# Part 2
for i in range(0, len(seeds), 2):
    new_seeds.append((seeds[i], seeds[i] + seeds[i + 1]))

for mp in maps:
    next_range = []

    while new_seeds:
        start, end = new_seeds.pop()
        for line in mp.split("\n")[1:]:
            dest, src, num = [*map(int, line.split())]
            offset = dest - src

            range_start = start if src <= start else src
            range_end = end if src + num - 1 >= end else src + num - 1

            if range_start <= range_end:
                next_range.append((range_start + offset, range_end + offset))

                if range_start > start:
                    new_seeds.append((start, range_start - 1))
                if range_end < end:
                    new_seeds.append((range_end + 1, end))
                break
        else:
            next_range.append((start, end))
    
    new_seeds = next_range

print(min(new_seeds, key=lambda x: x[0])[0])
