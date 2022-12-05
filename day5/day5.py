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
        # multi moves are done one at a time
        for i in range(int(num)):
            # move num from from_stack to to_stack
            pack = stacks[int(from_stack)-1].pop()
            stacks[int(to_stack)-1].append(pack)

    tops = [stack[-1] for stack in stacks]
    print(f'The tops of the stacks are {"".join(tops)}')        
    