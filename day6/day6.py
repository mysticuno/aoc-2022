with open('input.txt') as f:
    # need to find start of packet marker
    # sequence of 4 characters that are all different
    # sliding window of 4 chars
    msg = f.read()
    idx = 0
    while idx < len(msg)-4:
        packet = msg[idx:idx+4]
        if len(set(packet)) == 4:
            print(f'The start of packet marker is {packet} at position {idx+4}') # 1-index
            break
        idx+=1