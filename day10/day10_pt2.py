with open('input.txt') as f:
    x = 1
    cycle = 0
    lines = (line.strip().split() for line in f)
    pixels = []
    for line in lines:
        if abs(x - cycle%40) <= 1:
            pixels.append('#')
        else:
            pixels.append('.')
        cycle += 1
        if len(line) == 1: # noop
            continue
        else:
            if abs(x - cycle%40) <= 1:
                pixels.append('#')
            else:
                pixels.append('.')
            cycle += 1
            x += int(line[1])

    for i in range(6):
        print(''.join(pixels[i*40:(i+1)*40]))