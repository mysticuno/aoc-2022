import json
from functools import cmp_to_key

# Comparator: < is -1 = is 0 1 is >
def check_lists(llist, rlist):
    if type(llist) == int and type(rlist) == int:
        if llist < rlist:
            return 1
        elif llist == rlist:
            return 0
        else:
            return -1
    elif type(llist) == list and type(rlist) != list:
        return check_lists(llist, [rlist])
    elif type(llist) != list and type(rlist) == list:
        return check_lists([llist], rlist)
    else: # both are lists
        for i in range(min(len(llist), len(rlist))):
            ordered = check_lists(llist[i], rlist[i])
            if ordered != 0:
                return ordered
        if len(llist) < len(rlist):
            return 1
        elif len(llist) > len(rlist):
            return -1
        return 0


with open('input.txt') as f:
    index = 0
    count = 0
    lists = []
    for line in f:
        left = line.strip()
        right = f.readline().strip()
        f.readline() # skip new line
        index += 1
        
        llist, rlist = json.loads(left), json.loads(right)
        lists.extend([llist, rlist])
        
    # Add divider packets
    lists.extend([[[2]], [[6]]])
    sl = sorted(lists, key=cmp_to_key(check_lists), reverse=True)
    print((1+sl.index([[2]])) * (1+sl.index([[6]])))
