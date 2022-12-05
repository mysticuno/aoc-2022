with open('input.txt') as f:
    # First half initial state
    initial_state, moves = f.read().split('\n\n')
    lines = initial_state.split('\n')
    
    # Keep crates as stacks
    stacks = [[] for _ in range(len(lines[0])//4 + 1)]

    for line in lines:
        stack_num = 0
        while stack_num < len(stacks):
            char = line[1+stack_num*4] # [X]
            if str(char).isalpha():
                stacks[stack_num].append(char)
            stack_num += 1
    stacks = list(map(lambda x: x[::-1], stacks))

    # Second half moves
    for move in moves.split('\n'):
        _, num, _, from_stack, _, to_stack = move.split(' ')
        # multi moves are done all at once
        # move num from from_stack to to_stack
        stack = stacks[int(from_stack)-1]
        packs = stack[-int(num):]
        new_stack = stack[:-int(num)]
 
        # update stacks
        stacks[int(from_stack)-1] = new_stack
        stacks[int(to_stack)-1].extend(packs)

    tops = [stack[-1] for stack in stacks]
    print(f'The tops of the stacks are {"".join(tops)}')        
    