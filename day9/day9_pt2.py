class Rope:
    directions = {
        'R': (1,0),
        'L': (-1, 0),
        'U': (0, 1),
        'D': (0, -1),
    }
    
    def __init__(self):
        self.rope = [(0,0) for _ in range(10)]
        self.head = self.rope[0]
        self.tail = self.rope[-1]
        self.tail_moves = set()
        self.tail_moves.add(self.tail)
        
    def move(self, direction, index=0, delta_vector=None): #may need to pass dvec
        # calc delta vector before movement
        # after movement, if invariant broken, propagate to 
        # next knot until invariant holds while is_adj(knot1, knot2)
        # knot2 = self.rope(i) if i == len(rope) last move
        knot_index = index
        headx, heady = self.rope[knot_index]
        nextx, nexty = self.rope[knot_index+1]
        delta_vector = (headx - nextx, heady - nexty)
        print(f'\n\nindex={knot_index} moving {self.rope[0]} {direction} delta_vector {delta_vector}\nrope state {self.rope}')
        
        dx, dy = self.directions[direction]
        self.rope[knot_index] = (headx + dx, heady + dy)
        print(f'{"  "*knot_index}Moved index {index} to {self.rope[index]}')
        
            
        while not self.is_adj(self.rope[knot_index], self.rope[knot_index+1]):
            print(f'{"  "*knot_index}{self.rope}')
            print(f'{"  "*knot_index}knot {knot_index}@{self.rope[knot_index]} is not adjacent to knot {knot_index+1}@{self.rope[knot_index+1]} with delta_vector {delta_vector}')
            # headx, heady = self.rope[knot_index]
            nextx, nexty = self.rope[knot_index+1]

            self.rope[knot_index+1] = (nextx + delta_vector[0], nexty + delta_vector[1])            
            
            # tail moved
            if knot_index == len(self.rope) - 2:
                self.tail_moves.add(self.rope[knot_index+1])
                break
            knot_index += 1
        
    def move2(self, direction):
        headx, heady = self.rope[0]
        # nextx, nexty = self.rope[knot_index+1]
        # delta_vector = (headx - nextx, heady - nexty)
        # print(f'\n\nindex={knot_index} moving {self.rope[0]} {direction} delta_vector {delta_vector}\nrope state {self.rope}')
        
        dx, dy = self.directions[direction]
        self.rope[0] = (headx + dx, heady + dy)
        
        print(f'\nMoving {direction}\n{self.rope}')
        for i in range(1, len(self.rope)):
            self.pull(i-1, i)
        self.tail_moves.add(self.rope[-1])
    
    def pull(self, hidx, tidx):
        hx, hy = self.rope[hidx]
        tx, ty = self.rope[tidx]
        if self.is_adj((hx, hy), (tx, ty)):
            return
        print(f'Pulling rope[{hidx}]@{(hx, hy)} rope[{tidx}]@{tx, ty}')
        if hx > tx:
            tx += 1
        elif hx < tx:
            tx -= 1
        
        if hy > ty:
            ty += 1
        elif hy < ty:
            ty -= 1
        print(f'Moving to {tx, ty}')
        self.rope[tidx] = (tx, ty)
        # if hx == tx:
        #     # update y
        #     self.rope[tidx] = (tx, )
        # pass
    
    def is_adj(self, knot1, knot2):
        x1, y1 = knot1
        x2, y2 = knot2
        return abs(x1-x2) <= 1 and abs(y1-y2) <= 1
    
with open('input.txt') as f:
    rope = Rope()
    for line in f.readlines():
        direction, number = line.strip().split()
        for _ in range(int(number)):
            rope.move2(direction)
    print(rope.rope, '\n\n')
    print(rope.tail_moves, len(rope.tail_moves))
