coord_dict = {}
with open('input.txt') as f:
    # for safeguarding
    min_x, max_y = 500, 0
    # build rocks
    for line in f:
        l = list(map(lambda x: x.split(','), line.strip().split(' -> ')))
        for i in range(len(l)-1):
            start, end = l[i], l[i+1]
            if start[0] == end[0]: # move in y
                x = int(start[0])
                min_x = min(x, min_x)
                low, high = int(min(start[1], end[1])), int(max(start[1], end[1]))
                for y in range(low, high+1):
                    if (x, y) not in coord_dict:
                        max_y = max(y, max_y)
                        coord_dict[(x, y)] = '#'
            else: # move in x
                y = int(start[1])
                max_y = max(y, max_y)
                low, high = int(min(start[0], end[0])), int(max(start[0], end[0]))
                for x in range(low, high+1):
                    if (x, y) not in coord_dict:
                        min_x = min(x, min_x)
                        coord_dict[(x, y)] = '#'
    
# Fall sand
count = 0

def fall(coord_dict):
    x,y = 500, 0
    falling = True
    while falling and x >= min_x and y <= max_y:
        if (x,y+1) not in coord_dict:
            y+=1
        # check left
        elif (x-1, y+1) not in coord_dict:
            x-=1
            y+=1
        # check right
        elif (x+1, y+1) not in coord_dict:
            x+=1
            y+=1
        # stop
        else:
            falling = False
    if not falling:
        return (x,y)
    return "BREAK"

while True:
    coord = fall(coord_dict)
    if coord == "BREAK":
        break
    coord_dict[coord] = 'o'

print(len(list(filter(lambda x: x=='o', coord_dict.values()))))
