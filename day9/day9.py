class Rope:
    directions = {
        'R': (1,0),
        'L': (-1, 0),
        'U': (0, 1),
        'D': (0, -1),
    }
    
    def __init__(self):
        self.head = (0,0)
        self.tail = (0,0)
        self.tail_moves = set()
        self.tail_moves.add(self.tail)
        
    def move(self, direction, num):
        for _ in range(num):
            dx, dy = self.directions[direction]
            hx, hy = self.head
            self.head = (hx + dx, hy + dy)
 
            if not self.is_adj():
                self.tail = (hx, hy)
                self.tail_moves.add(self.tail)
            
    def is_adj(self):
        hx, hy = self.head
        tx, ty = self.tail
        return abs(hx-tx) <= 1 and abs(hy - ty) <= 1
    
with open('input.txt') as f:
    rope = Rope()
    for line in f.readlines():
        direction, number = line.strip().split()
        rope.move(direction, int(number))
    print(len(rope.tail_moves))
