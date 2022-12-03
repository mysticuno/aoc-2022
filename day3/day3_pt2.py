import string

with open('input.txt') as rucks:
    total = 0
    elves = []
    for ruck in rucks:
        elves.append(ruck.strip())
        if len(elves) == 3:
            items = [set(elf) for elf in elves]
            # Get 3 elves and find intersection of 3 rucks
            badge = (items[0] & items[1] & items[2]).pop()
            # convert shared badge to priority
            total += string.ascii_letters.find(badge) + 1 # 0-indexed
            elves = []
    print(f'The sum of the priorities is {total}')
