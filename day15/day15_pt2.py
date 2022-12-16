import re
"""
Radius diamond is defined by 4 line segments, 2 with slope 1, 2 with slope -1

Using point slope form (y-sy) = m(x-sx) we get the 2 lines that intersect at sensor
coordinates (sx, sy) with m=+-1
    (y-sy) = (x-sx) =>  y =  x - sx + sy
    (y-sy) = -(x-sx) => y = -x + sx + sy

A sensor has radius r (it's Manhattan distance to the closest beacon), so shifting 
the 2 lines by +r and -r we get 4 line segments defining our boundaries. The missing 
beacon would be outside that boundary, so along the lines

    y =  x - sx + sy + r + 1 => y = x + a where a = sy - sx + r + 1
    y =  x - sx + sy - r - 1 => y = x + a where a = sy - sx - r - 1
    
    y = -x + sx + sy + r + 1 => y = -x + b where b = sy + sx + r + 1
    y = -x + sx + sy - r - 1 => y = -x + b where b = sy + sx - r - 1
    
Given 2 line segments
    y =  x + a
    y = -x + b
they intersect at the point ((b-a)/2, (a+b)/2). We can gather all the possible
a and b values to get the intersection points, and cross referrence which intersection
point is outside the range of all scanners
"""

def nums(line):
    return [int(num) for num in re.findall('-?\d+', line)]

def distance(p1, p2): 
    return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])


with open('input.txt') as f:
    data = [nums(l) for l in f]

radius = {(sx, sy): distance((sx, sy), (bx, by)) for (sx,sy,bx,by) in data}

avals, bvals = set(), set()
for ((sx, sy), r) in radius.items():
    avals.add(sy - sx + r + 1)
    avals.add(sy - sx - r - 1)
    bvals.add(sy + sx + r + 1)
    bvals.add(sy + sx - r - 1)

bound = 4_000_000
coords = None
for a in avals:
    if coords: break
    for b in bvals:
        if coords: break
        px, py = ((b-a)//2, (a+b)//2)
        # check if the intersection is within the bounds
        if 0 < px < bound and 0 < py < bound:
            # check if all sensors would have missed this intersection
            if all(distance((px, py), (sx, sy)) > r for ((sx,sy), r) in radius.items()):
                print(f"Found {px,py}")
                coords = (px, py)
print(bound*coords[0]+coords[1])
