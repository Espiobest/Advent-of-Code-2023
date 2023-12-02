with open('data.txt', 'r') as r:
    lines = r.read().splitlines()

totalRed = 12
totalGreen = 13
totalBlue = 14

total = 0
totalProd = 0

def parseColor(game, color):
    if color not in game:
        return -1
    return int(game.split(" " + color)[0].split()[-1])

for i, line in enumerate(lines, start=1):
    
    games = line.split("; ")
    red = blue = green = -1
    maxRed = maxGreen = maxBlue = 0
    possible = True

    for game in games:
        red = parseColor(game, "red")
        green = parseColor(game, "green")
        blue = parseColor(game, "blue")

        if red > totalRed or green > totalGreen or blue > totalBlue:
            possible = False
        
        maxRed = max(maxRed, red)
        maxGreen = max(maxGreen, green)
        maxBlue = max(maxBlue, blue)
    
    totalProd += maxRed * maxGreen * maxBlue
    if possible:
        total += i

print("Part 1:", total)
print("Part 2:", totalProd)


