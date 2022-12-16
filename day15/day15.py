import re

def nums(line):
    return [int(num) for num in re.findall('-?\d+', line)]

def distance(p1, p2): 
    return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])


with open('input.txt') as f:
    data = [nums(l) for l in f]

radius = {(sx, sy): distance((sx, sy), (bx, by)) for (sx,sy,bx,by) in data}
sensors = radius.keys()
beacons = set((bx, by) for (sx, sy, bx, by) in data)
max_radius = max(radius.values())
min_x = min(radius.keys(), key=lambda x:x[0])[0]
max_x = max(radius.keys(), key=lambda x:x[0])[0]
print(f"min x {min_x} max_x {max_x} max_rad {max_radius}")

y = 2_000_000
count = 0
for x in range(min_x - max_radius, max_x+max_radius):
    if x % 100_000 == 0:
        print(f"coord={x,y}")
    if (x,y) in sensors or (x,y) in beacons:
        continue
    for (sx, sy) in sensors:
        rad = radius[(sx, sy)]
        dist = distance((sx, sy), (x,y))
        if dist <= rad:
            # print(f"\t\tIncreasing count, {x,y} would be found by sensor {sx,sy} with rad={rad} and dist={dist}")
            count += 1
            break
print(count)