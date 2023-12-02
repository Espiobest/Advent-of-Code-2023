import os

for i in range(1, 26):
    os.mkdir(f"Day {i}")
    template = '''with open('data.txt', 'r') as r:
    lines = r.read().splitlines()'''
    with open(os.path.join(f'Day {i}', f'Day {i}.py'), 'w') as f:
            f.write(template)        
    open(os.path.join(f'Day {i}', f'data.txt'), 'w').close()

print("Created folders!")
