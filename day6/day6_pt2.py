with open('input.txt') as f:
    # need to find start of message marker
    # sequence of 14 characters that are all different
    # sliding window of 14 chars
    msg = f.read()
    idx = 0
    while idx < len(msg)-14:
        packet = msg[idx:idx+14]
        if len(set(packet)) == 14:
            print(f'The start of message marker is {packet} at position {idx+14}') # 1-index
            break
        idx+=1