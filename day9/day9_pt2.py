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
                
    def move(self, direction):
        headx, heady = self.rope[0]
        
        dx, dy = self.directions[direction]
        self.rope[0] = (headx + dx, heady + dy)
        
        # print(f'\nMoving {direction}\n{self.rope}')
        for i in range(1, len(self.rope)):
            self.pull(i-1, i)
        self.tail_moves.add(self.rope[-1])
    
    def pull(self, hidx, tidx):
        hx, hy = self.rope[hidx]
        tx, ty = self.rope[tidx]
        if abs(hx-tx) <= 1 and abs(hy-ty) <= 1:
            return
        # print(f'Pulling rope[{hidx}]@{(hx, hy)} rope[{tidx}]@{tx, ty}')
        if hx > tx:
            tx += 1
        elif hx < tx:
            tx -= 1
        
        if hy > ty:
            ty += 1
        elif hy < ty:
            ty -= 1
        # print(f'Moving to {tx, ty}')
        self.rope[tidx] = (tx, ty)
    
    def is_adj(self, knot1, knot2):
        x1, y1 = knot1
        x2, y2 = knot2
        return 
    
with open('input.txt') as f:
    rope = Rope()
    for line in f.readlines():
        direction, number = line.strip().split()
        for _ in range(int(number)):
            rope.move(direction)
    # print(rope.rope, rope.tail_moves)
    print(len(rope.tail_moves))
