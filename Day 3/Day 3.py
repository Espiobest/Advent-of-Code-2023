import re
import collections

with open('data.txt', 'r') as r:
    lines = r.read().splitlines()

total = 0
gears = collections.defaultdict(list)

def is_symbol(point):
    return (not point.isdigit() and point != '.')

def check_neighbors(lines, i, num, index):
    
    start = index - 1
    end = index + len(num)

    if start >= 0:
        if lines[i][start] == '*':
            gears[(i, start)].append(int(num))
        
        if is_symbol(lines[i][start]):
            return True

    if end < len(lines[i]):
        if lines[i][end] == '*':
            gears[(i, end)].append(int(num))
            
        if is_symbol(lines[i][end]):
            return True
    
    if start < 0:
        start = 0
    if end >= len(lines[i]):
        end = len(lines[i]) - 1
      
    neighboring_lines = []
    if i > 0:
        neighboring_lines.append((-1, lines[i-1]))
    if i < len(lines) - 1:
        neighboring_lines.append((1, lines[i+1]))

    for direction, line in neighboring_lines:
        for j, symbol in enumerate(line[start:end+1], start):
            if is_symbol(symbol):
                if symbol == "*":
                    gears[(i + direction, j)].append(int(num))
                return True
  
    return False
    
total = 0
gear_total = 0

for i, line in enumerate(lines):
    numbers = re.finditer("\d+", line)

    for match in numbers:
        num = match.group(0)
        if check_neighbors(lines, i, num, match.start()):
            total += int(num)

for gear in gears:
    if len(gears[gear]) == 2:
        x, y = gears[gear]
        gear_total += x * y

print("Part 1:", total)
print("Part 2:", gear_total)