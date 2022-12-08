def is_tree_visible(trees, row, col):
    visible = True
    tree = trees[row][col]
    
    # check left to tree
    for c in range(col):
        if trees[row][c] >= tree:
            visible = False
    
    if visible:
        return True
        
    # check top to tree
    visible = True
    for r in range(row):
        if trees[r][col] >= tree:
            visible = False
    
    if visible:
        return True
    
    # check right to tree
    visible = True
    for c in range(col+1, len(trees[0])):
        if trees[row][c] >= tree:
            visible = False
    
    if visible:
        return True
    
    # check bot to tree
    visible = True
    for r in range(row+1, len(trees)):
        if trees[r][col] >= tree:
            visible = False
    
    return visible
    

with open('input.txt') as f:
    grid = f.read().splitlines()
    trees = [[int(char) for char in row] for row in grid]
    
    count = 4*len(trees)-4
    for row in range(1, len(trees)-1):
        for col in range(1, len(trees)-1):
            
            if is_tree_visible(trees, row, col):
                count += 1
            
    print(count)