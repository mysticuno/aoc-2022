
from copy import deepcopy

with open('input.txt') as f:
    og_hills = []
    starts = []
    for row, line in enumerate(f.readlines()):
        if 'S' in line:
            starts.append((row, line.index('S')))
        if 'a' in line:
            starts.append((row, line.index('a')))
        line = [[c, 0] for c in line.strip()]
        og_hills.append(line)

def get_neighbors(r, c):
    height, width = len(og_hills), len(og_hills[0])
    dirs = (1, 0, -1, 0, 1)
    neighbors = []
    for i in range(4):
        dx, dy = dirs[i], dirs[i+1]
        if 0 <= c+dx < width and 0 <= r+dy < height:
            neighbors.append((r+dy, c+dx))
    return neighbors

lengths = []
for start in starts:
    queue= [start]
    hills = deepcopy(og_hills)

    while len(queue) != 0:
        # Pop from queue and inspect
        row, col = queue.pop(0)
        hill, dist = hills[row][col]

        # Found goal
        if hill == 'E':
            lengths.append(dist)
            break
        if hill == 'S':
            hill = 'a'
        neighbors = get_neighbors(row, col)
        for (r, c) in neighbors:
            neighbor, neighbor_dist = hills[r][c]
            if neighbor == 'S':
                neighbor = 'a'
            elif neighbor == 'E':
                neighbor = 'z'
            if ord(neighbor)-ord(hill) <= 1 and neighbor_dist == 0:# not seen and (r,c) not in seen:
                hills[r][c][1] = dist+1
                queue.append((r, c))

print(min(lengths))