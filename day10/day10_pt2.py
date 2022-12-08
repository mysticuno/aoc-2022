with open('input.txt') as f:
    '''
    Start by figuring out the signal being sent by the CPU. The CPU has a single register, X, which starts with the value 1. It supports only two instructions:

    addx V takes two cycles to complete. After two cycles, the X register is increased by the value V. (V can be negative.)
    
    noop takes one cycle to complete. It has no other effect.
    '''
    x = 1
    cycle = 0
    lines = (line.strip().split() for line in f)
    adding = False
    pixels = []
    while True:
        try:
            # print(f"Start of loop, state: adding:{adding} cycle:{cycle} x:{x}")
            if adding:
                adding = False
                cycle += 1
                if cycle % 20 == 0:
                    # print(f"\tAdding to signal, state: line:{line} adding:{adding} cycle:{cycle} x:{x}")
                    signals.append([cycle, x, cycle*x])
                x += int(line[1])
                continue
            line = next(lines)
            # print(line)
            cycle += 1
            if cycle % 20 == 0:
                # print(f"\tAdding to signal, state: line:{line} adding:{adding} cycle:{cycle} x:{x}")
                signals.append([cycle, x, cycle*x])

            if len(line) == 1: #noop
                continue
            else: # addx <num>
                adding = True
        except StopIteration:
            break
    print(signals)
    print([signal[2] for signal in signals if signal[0] in range(20, 221, 40)])
    print(sum(signal[2] for signal in signals if signal[0] in range(20, 221, 40)))