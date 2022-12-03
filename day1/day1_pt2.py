import heapq

with open('input.txt') as f:
    # create a min heap
    max_elves = [0,0,0]
    heapq.heapify(max_elves)    
    calories = 0
    for line in f:
        if line == '\n':
            heapq.heappushpop(max_elves, calories)
            calories = 0
            continue
        calories += int(line)

print(f'Top 3 elf calories {max_elves} with total calories: {sum(max_elves)}')
