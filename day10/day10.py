with open('input.txt') as f:
    x = 1
    cycle = 0
    lines = (line.strip().split() for line in f)
    signals = []
    for line in lines:
        cycle += 1
        if (cycle+20) % 40 == 0:
            signals.append(cycle*x)
        if len(line) == 1: # noop
            continue
        else:
            cycle += 1
            if (cycle + 20) % 40 == 0:
                signals.append(cycle*x)
            x += int(line[1])

    print(sum(signals))