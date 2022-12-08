def vis_score(trees, row, col):
    total = 1
    tree = trees[row][col]
    
    # check tree to left
    vis = 0
    for c in range(col)[::-1]:
        vis += 1
        if trees[row][c] >= tree:
            break
    total *= vis

    # check tree to top
    vis = 0
    for r in range(row)[::-1]:
        vis += 1
        if trees[r][col] >= tree:
            break
    total *= vis
        
    # check tree to right
    vis = 0
    for c in range(col+1, len(trees[0])):
        vis+=1
        if trees[row][c] >= tree:
            break
    total *= vis
        
    # check tree to bot 
    vis = 0
    for r in range(row+1, len(trees)):
        vis += 1
        if trees[r][col] >= tree:
            break
    total *= vis
    
    return total
    

with open('input.txt') as f:
    grid = f.read().splitlines()
    trees = [[int(char) for char in row] for row in grid]
    
    highest = 0
    for row in range(1, len(trees)-1):
        for col in range(1, len(trees)-1):
            highest = max(highest, vis_score(trees, row, col))
            
    print(highest)