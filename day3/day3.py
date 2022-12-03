import string

with open('input.txt') as rucks:
    total = 0
    for ruck in rucks:
        # split line down the middle
        ruck = ruck.strip()
        sack1, sack2 = set(ruck[:len(ruck)//2]), set(ruck[len(ruck)//2:])
        # find intersection using sets
        item =  (sack1 & sack2).pop()
        # convert shared items to priorities
        total += string.ascii_letters.find(item) + 1 # 0-indexed
    print(f'The sum of the priorities is {total}')
