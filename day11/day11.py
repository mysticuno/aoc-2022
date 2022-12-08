from operator import add, mul
class Monkey:
    def __init__(self, items, operation, divisible_by, true_monkey, false_monkey):
        self.num_inspections = 0
        self.items = items
        self.operate = self.make_op(operation)
        self.divisible_by = divisible_by
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey
        
    def inspect(self):
        self.num_inspections += 1
        old = self.items.pop(0)
        new = self.operate(old) // 3
        return new

    def make_op(self, operation):
        val = operation.split()[-1]
        if val == 'old':
            if '+' in operation:
                return lambda x: add(x, x)
            else:
                return lambda x: mul(x, x)
        val = int(val)
        if '+' in operation:
            return lambda x: add(x, val)
        else:
            return lambda x: mul(x, val)

    def test(self, worry):
        if worry % self.divisible_by == 0:
            return self.true_monkey
        return self.false_monkey

    def throw(self, item, monkey):
        monkey.catch(item)

    def catch(self, item):
        self.items.append(item)

    def has_items(self):
        return len(self.items) != 0


with open('input.txt') as f:
    monkeys = []
    # make monkeys
    for line in f:
        if line.startswith('Monkey'):
            items = [int(item) for item in f.readline().replace(',', '').split()[2:]]
            operation = f.readline().strip().split('= ')[-1]
            divisible_by = int(f.readline().strip().split('by ')[-1])
            true_monkey = int(f.readline().strip()[-1])
            false_monkey = int(f.readline().strip()[-1])
            monkeys.append(Monkey(items, operation, divisible_by, true_monkey, false_monkey))
    
# 20 rounds of throwing
for r in range(20):
    for index, monkey in enumerate(monkeys):
        while monkey.has_items():
            worry = monkey.inspect()
            receiver = monkey.test(worry)
            monkey.throw(worry, monkeys[receiver])
    x,y = sorted(monkey.num_inspections for monkey in monkeys)[-2:]
print(f'Monkey business is {x*y}')
