with open('data.txt', 'r') as r:
    lines = r.read().splitlines()

times = [*map(int,lines[0].split(": ")[1].split())]
distance = [*map(int,lines[1].split(": ")[1].split())]

# uncomment for part 2
# times = [int("".join(str(i) for i in times))]
# distance = [int("".join(str(i) for i in distance))]
total = 1

for i in range(len(times)):
    time = times[i]
    count = 0
    for j in range(time + 1):
        x = time - j
        dist = j * x
        if dist > distance[i]:
            count+=1
    if count:
        total *= count

print(total)
