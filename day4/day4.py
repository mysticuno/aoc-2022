with open('input.txt') as f:
    total = 0
    for line in f:
        rang1, rang2 = line.split(',')
        vals1 = list(map(int, rang1.split('-')))
        vals2 = list(map(int, rang2.split('-')))
        
        
        set1 = set(range(vals1[0], vals1[1]+1))
        set2 = set(range(vals2[0], vals2[1]+1))
        intersect = set1 & set2
        if intersect == set1 or intersect == set2:
            total +=1
    
    print(f'The total of pairs fully contained is {total}')
