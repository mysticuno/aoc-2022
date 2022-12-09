with open('input.txt') as f:
    hills = []
    for row, line in enumerate(f.readlines()):
        if 'S' in line:
            start = (row, line.index('S'))
        line = [[c, 0] for c in line.strip()]
        hills.append(line)

queue= [start]

def get_neighbors(r, c):
    height, width = len(hills), len(hills[0])
    dirs = (1, 0, -1, 0, 1)
    neighbors = []
    for i in range(4):
        dx, dy = dirs[i], dirs[i+1]
        if 0 <= c+dx < width and 0 <= r+dy < height:
            neighbors.append((r+dy, c+dx))
    return neighbors

while len(queue) != 0:
    # Pop from queue and inspect
    row, col = queue.pop(0)
    hill, dist = hills[row][col]

    # Found goal
    if hill == 'E':
        print(f'Total distance {dist}')
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
        if ord(neighbor)-ord(hill) <= 1 and neighbor_dist == 0:
            hills[r][c][1] = dist+1
            queue.append((r, c))
